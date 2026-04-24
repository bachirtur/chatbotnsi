<script setup>
import { ref, nextTick } from "vue";
import DragDrop from './components/DragDrop.vue'
import Input from './components/Input.vue'
import MessageContainer from './components/MessageContainer.vue'
import Code from './components/Code.vue'
import {VueSpinnerDots} from 'vue3-spinners';

const active = ref(false);
const file = ref(null)
const imgSrc = ref(null);
const showCode= ref(false)
const response = ref(null)
const question = ref(null)
const isthinking = ref(false)
const isTitle = ref(true)
const code = ref(null)
const tab_q_r = ref([])
const itemRefs = ref([]);

const toggleActive = () => {
  active.value = !active.value;
};
const handelFileUpload = (e) => {
    active.value = false
    file.value = e.dataTransfer.files[0] || e.target.files[0]
    imgSrc.value = URL.createObjectURL(file.value);
};
const handelFileUploadInput = (e) => {
    file.value = e.target.files[0]
    imgSrc.value = URL.createObjectURL(file.value);
};
const noImage = () => {
  file.value = null;
  imgSrc.value = null;
  }
const uuidv4 = () => {
    return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, c =>
      (+c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> +c / 4).toString(16)
    );
}

const codeToggle = () =>
{
  showCode.value = ! showCode.value
}

const id = uuidv4()

const request = async (q) => {

  isTitle.value = false
  if (code.value) {
    question.value = "```python" + "\n" + code.value + "\n" + "```" + "\n" + q 
  }
  else {
    question.value=q
  }
  tab_q_r.value.push(question.value)
  await nextTick();
  scrollToBottom()
  isthinking.value = true
  const formData = new FormData()
  formData.append("id", id)
  formData.append("query", question.value)
  if (file.value) {
    formData.append("image", file.value)
  }
  await nextTick();
  scrollToBottom()
  try {
    const callChatbot = await fetch("https://dav74-chatbot-nsi.hf.space/request",{
      method : "POST",
      body : formData
        });
    const rep = await callChatbot.json();
    response.value = rep.response;
    code.value = null
        
  }
  catch (error) {
    console.log("erreur : ",error)
    response.value = "Désolé, suite à une erreur interne, je ne suis pas en mesure de répondre à votre question pour le moment" ;
  }
  if (response.value == "Attention, vous m'avez fourni autre chose qu'une image. Renouvelez votre demande avec une image."){
    file.value = null;
    imgSrc.value = null;
  }
  isthinking.value = false;
  showCode.value = false;
  code.value = null;
  tab_q_r.value.push(response.value)
  await nextTick();
  scrollToBottom()
}
const setItemRef = (el, index) => {
  if (el) {
    itemRefs.value[index] = el;
  }
}
const scrollToBottom = () => {
    nextTick(() => {
      const lastIndex = tab_q_r.value.length - 1
      setTimeout(() => {
        const el = itemRefs.value[lastIndex]
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      },100)
      
    })
}
</script>

<template>
  <DragDrop v-if="active" @dragleave.prevent="toggleActive" @dragover.prevent @drop.prevent="handelFileUpload"/>
  <div class="w-full h-screen mx-auto " @dragenter.prevent="toggleActive" @dragover.prevent>
    <div ref="container" :class="['no-scrollbar w-full lg:w-4/5 xl:w-3/5 px-10 mx-auto overflow-auto relative', showCode ? 'h-4/7' : 'h-5/7']">

        <h1 v-if="isTitle" class="pt-25 text-2xl sm:text-3xl md:text-4xl text-center">Chatbot NSI</h1>

        <p v-if="isTitle" class="mt-5 text-justify">Je suis un assistant spécialisé dans l'enseignement Numérique et Sciences Informatiques. Je suis là pour vous aider à réviser le cours en répondant à vos questions. 
          Je peux aussi vous proposer des exercices. Si vous avez besoin d'écrire du code (Python, SQL...), vous pouvez utiliser un éditeur de code en cliquant sur le bouton &lt/&gt ci-dessous. 
        Vous pouvez ajouter des images à votre conversation en glissant-déposant votre image ou en cliquant sur <img src="/image.png" class="w-[25px] inline">. Pour supprimer une image de votre conversation, vous devez cliquer sur <img src="/no-image.png" class="w-[25px] inline">.</p>
        
        <div v-for = "(q_r,index) in tab_q_r" :key="index" :ref="el => setItemRef(el, index)">
          <MessageContainer  :msg = "q_r" :index = "index" :isthink="isthinking"/>
        </div>
        <div v-if="isthinking" class="mb-5"><VueSpinnerDots size="50" color="black" /></div>
        
    </div>
    <div class="md:w-[750px] flex flex-col mx-auto pt-1 rounded-4xl shadow-[0px_4px_16px_rgba(17,17,26,0.1),_0px_8px_24px_rgba(17,17,26,0.1),_0px_16px_56px_rgba(17,17,26,0.1)]">
      <Transition name="fade">
        <Code class="mt-3" v-if="showCode" @update-code="c => code = c"/>
      </Transition>
      <Transition name="fade">
        <img :src="imgSrc" v-if="imgSrc" class="w-[75px] mt-1 ml-5 rounded-2xl"> 
      </Transition> 
      <div class="md:w-[700px] ml-4 mt-3"><Input :isthink = "isthinking" @update-question="question => request(question)"/></div>
      <div class="flex w-full">
        <label for="file-upload"><img src="/image.png" class="w-[40px] ml-10 pb-3 mt-1 hover:cursor-pointer"></label> 
        <input id="file-upload" type="file" class="hidden" accept="image/*" @change="(e) => handelFileUploadInput(e)"/> 
        <img src="/no-image.png" class="w-[40px] ml-6 pb-3 mt-1 hover:cursor-pointer" @click="noImage">
        <img src="/code.png" class="w-[40px] ml-6 pb-3 mt-1 hover:cursor-pointer" @click="codeToggle"> 
      </div> 
    </div>
  </div> 
</template>

<style>
  .fade-enter-from
  {
    opacity : 0;
  }
  .fade-enter-to
  {
    opacity : 1;
  }
  .fade-enter-active
  {transition : all 0.5s ease}
  
</style>

