<template>
    <div v-if="props.source" v-html="markdown.render(props.source)" />
  </template>
  
  <script setup>
  import MarkdownIt from "markdown-it";
  const props = defineProps(['source']);
  const markdown = new MarkdownIt()
  

  </script>