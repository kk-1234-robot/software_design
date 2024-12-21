<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import Left_Frame from "./components/Left_Frame.vue";
import Right_Frame from "./components/Right_Frame.vue";
import {ref} from "vue";

const selectedContent = ref('home'); // 默认显示首页内容
</script>

<template>
  <body class="Container">
  <div class="left">
    <Left_Frame :selectedContent="selectedContent" @update:selectedContent="selectedContent = $event"/>
  </div>
  <div class="right">
    <Right_Frame :selectedContent="selectedContent"/>
  </div>
  </body>
</template>

<style scoped>

html, body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.Container {
  display: grid;
  grid-template-columns: 10% 90%;
  width: 100%;
  padding-right: 1rem;
  border-radius: 1rem;
}

.left {
  background-color: #2c3e50;
  border-radius: 1rem;
}

.right {
  background-color: white;
  border-radius: 1rem;
}

@media (min-width: 1024px) {
  /*  header {
      display: flex;
      place-items: center;
      padding-right: calc(var(--section-gap) / 2);
    }*/
  .Container {
    display: grid;
    grid-template-columns: 10% 90%;
    width: 100%;
    padding-right: 1rem;
    border-radius: 1rem;
  }

  html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
  }

  .left {
    background-color: #2c3e50;
    border-radius: 1rem;
  }

  .right {
    background-color: white;
    border-radius: 1rem;
  }

  .logo {
    color: #795da3;
    font-size: 60px;
  }

  .iconfont {
    font-size: inherit;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>