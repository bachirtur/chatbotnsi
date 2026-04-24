<script setup>
import MarkdownRenderer from './MarkdownRenderer.vue'
const props = defineProps(['msg','index', 'isthink'])
</script>

<template>
    <div :class="props.index%2 == 0 ? 'pt-5 flex justify-end ml-10' : 'w-full pt-5'" >
        <Transition name="fade"> 
            <span  :class="props.index%2 == 0 ? 'bg-blue-100 p-3 rounded-4xl max-w-3/4' : 'p-4 text-justify'"><MarkdownRenderer :source="props.msg" /></span>
        </Transition>
    </div>
</template>
<style>
  .fade-enter-from{
    opacity : 0;
  }
  .fade-enter-to{
    opacity : 1;
  }
  .fade-enter-active{transition : all 1s ease}
</style>