<script setup>
import {ref} from 'vue';
const question = ref('')
const emit = defineEmits(['updateQuestion'])
const props = defineProps(['isthink'])
const inputRef = ref(null)

const handler = ()=>{
  if (question.value.length > 0 && !props.isthink){
    emit('updateQuestion', question.value)
    question.value =""
  } 
}
window.addEventListener('keydown', (e) => {
      if (e.key == 'Enter') {
        handler()
      }
});
</script>

<template>
    <div class="w-full  mt-5 h-1/6 flex items-center justify-center relative">
      <div class="w-full"><input autofocus class=" mx-auto w-full min-h-11 rounded-xl bg-gray-100 p-3 border-gray-100 focus:outline-none focus:ring-0 border border-solid focus:border-black" v-model = "question" placeholder="À vous..."></div>
      <div class="relative right-10 hover:cursor-pointer opacity-50" @click="handler"><svg xmlns="http://www.w3.org/2000/svg" width="1.5em" height="1.5em" viewBox="0 0 448 384"><path fill="currentColor" d="M0 384V235l320-43L0 149V0l448 192z"/></svg></div>
    </div> 
</template>