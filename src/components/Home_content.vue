<script setup>
import Step from './Step.vue';
</script>

<template>
  <div class="Container">
    <Step :stepNumber="1" stepText="First step content"/>
    <Step :stepNumber="2" stepText="Second step content"/>
    <Step :stepNumber="3" stepText="Third step content"/>
  </div>
</template>

<style scoped>
.Container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5%;
  height: 100%;
  background-color: white;
}


</style>