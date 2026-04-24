from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from typing import List

from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import AnyMessage, add_messages
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import END, StateGraph, START
from langgraph.checkpoint.memory import MemorySaver
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from PIL import Image
import base64
from io import BytesIO
import os 
import logging
import sys

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

loader_prem = UnstructuredMarkdownLoader("programme_NSI_premiere.md")
prog_prem = loader_prem.load()

loader_term = UnstructuredMarkdownLoader("programme_NSI_terminale.md")
prog_term = loader_term.load()

memory = MemorySaver()

system = """
Tu es un assistant spécialisé dans l'enseignement de la spécialité Numérique et sciences informatiques en classe de première et de terminal
Tu as un bon niveau en langage Python
Ton interlocuteur est un élève qui suit la spécialité nsi en première et en terminale
Ton unique thème de conservation doit être l'enseignement de l'informatique. Tu ne dois pas aborder d'autres thèmes que l'enseignement de l'informatique
Tu ne dois pas faire d'erreur, répond à la question uniquement si tu es sûr de ta réponse
si tu ne trouves pas la réponse à une question, tu réponds que tu ne connais pas la réponse et que l'élève doit s'adresser à son professeur pour obtenir cette réponse
si l'élève n'arrive pas à trouver la réponse à un exercice, tu ne dois pas lui donner tout de suite la réponse, mais seulement lui donner des indications pour lui permettre de trouver la réponse par lui même
Tu dois uniquement répondre en langue française
Tu ne dois pas commencer tes réponses par "Assistant :"
Tu trouveras ci-dessous les programmes de la spécialité NSI en première et terminale, tu devras veiller à ce que tes réponses ne sortent pas du cadre de ces programmes
Si la question posée ne rentre pas dans le cadre du programme de NSI tu peux tout de même répondre en précisant bien que cette notion est hors programme
si tu proposes un exercice, tu dois bien vérifier que toutes les notions nécessaires à la résolution de l'exercice sont explicitement au programme de NSI
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Voici le programme officiel de première de la spécialité NSI : \n {prem}"),
        ("human", "Voici le programme officiel de terminale de la spécialité NSI : \n {term}"),
        ("human", "Voici l'historique de la conversation entre l'assistant et l'élève : \n {historical} \n\n Voici l'intervention de l'élève : \n {question}"),
    ]
)

def format_historical(hist):
    historical = []
    for i in range(0,len(hist)-2,2):
        historical.append("Utilisateur : "+hist[i].content[0]['text'])
        historical.append("Assistant : "+hist[i+1].content[0]['text'])
    return "\n".join(historical[-10:])


class GraphState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


def chatbot(state : GraphState):
    question = prompt.invoke({'historical': format_historical(state['messages']), 'prem': prog_prem, 'term': prog_term,  'question' : state['messages'][-1].content[0]['text']})
    q = "".join([m.content for m in question.messages])
    if len(state['messages'][-1].content) > 1 :
        response = llm.invoke([HumanMessage(
            content=[
                {"type": "text", "text": q},
                state['messages'][-1].content[1]
            ])])
    else :
        response = llm.invoke([HumanMessage(
            content=[
                {"type": "text", "text": q}
            ])])
    return {"messages": [AIMessage(content=[{'type': 'text', 'text': response.content}])]}

workflow = StateGraph(GraphState)

workflow.add_node('chatbot', chatbot)

workflow.add_edge(START, 'chatbot')
workflow.add_edge('chatbot', END)

app_chatbot = workflow.compile(checkpointer=memory)

@app.post('/request')
def request(id:Annotated[str, Form()], query:Annotated[str, Form()], image:Optional[UploadFile] = None):
    config = {"configurable": {"thread_id": id}}
    if image:
        try:
            img = Image.open(image.file)
            img_buffer = BytesIO()
            img.save(img_buffer, format='PNG')
            byte_data = img_buffer.getvalue()
            base64_img = base64.b64encode(byte_data).decode("utf-8")
            message = HumanMessage(
            content=[
                {'type': 'text', 'text': query},
                {'type': 'image_url', 'image_url': {"url": f"data:image/jpeg;base64,{base64_img}"}}
            ])
        except:
            return {"response":"Attention, vous m'avez fourni autre chose qu'une image. Renouvelez votre demande avec une image."}
        rep = app_chatbot.invoke({"messages": message},config, stream_mode="values")
    else :
        rep = app_chatbot.invoke({"messages": [HumanMessage(content=[{'type': 'text', 'text': query}])]},config, stream_mode="values")
    return {"response":rep['messages'][-1].content[0]['text']}
