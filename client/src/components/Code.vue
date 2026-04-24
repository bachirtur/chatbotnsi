<template>

  
  <div class="w-150 ml-10 max-h-50 overflow-auto">
    <select v-model="selected" @change="updateLang" class="mb-2">
      <option>Python</option>
      <option>SQL</option>
      <option>JavaScript</option>
      <option>HTML</option>
      <option>CSS</option>
      <option>C++</option>
    </select>
        <CodeMirror v-model="code" :lang="lang" :basic="basic" @change="update_code"/>
  </div>
    
  </template>
  <script setup>
  const selected = ref("Python");
  import { ref, onMounted, onUnmounted } from "vue";
  import CodeMirror from 'vue-codemirror6';
  import { python } from '@codemirror/lang-python';
  import { sql } from '@codemirror/lang-sql';
  import { javascript } from '@codemirror/lang-javascript';
  import { html } from '@codemirror/lang-html';
  import { css } from '@codemirror/lang-css';
  import { cpp } from '@codemirror/lang-cpp';

  const emit = defineEmits(['updateCode'])

  const code = ref("");
  const lang = ref(python());
  const basic=true;

  const update_code = () => {
    emit('updateCode', code.value)
  }

  const updateLang = () => {
    if (selected.value == "SQL") {
      lang.value = sql()
      code.value = ""
    }
    else if (selected.value == "JavaScript") {
      lang.value = javascript()
      code.value = ""
    }
    else if (selected.value == "HTML") {
      lang.value = html()
      code.value = ""
    }
    else if (selected.value == "CSS") {
      lang.value = css()
      code.value = ""
    }
    else if (selected.value == "C++") {
      lang.value = cpp()
      code.value = ""
    }
    else {
      lang.value = python()
      code.value = ""
    }
  }

  </script>