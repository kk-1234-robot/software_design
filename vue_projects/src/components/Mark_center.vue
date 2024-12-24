<script setup>

import {InboxOutlined} from '@ant-design/icons-vue';

const description = "txt";
</script>

<template>
  <div class="Container">
    <div class="left">
      <button> 人工标注</button>
      <button>智能标注</button>
    </div>

    <div class="center">

      
    </div>

    <div class="right">
      <button>上一份</button>
      <button>下一份</button>
    </div>
  </div>

</template>


<style scoped>

.Container {
  display: grid;
  width: 100%;
  height: 100%;
  grid-template-columns: 25% 50% 25%;
}

.left, .center, .right {
  display: flex;
  height: 100%;
  align-items: center;
  gap: 20px;
  margin-top: 20px;
}

.left, .right {
  flex-direction: column; /* Arrange buttons vertically */
  align-items: center;
  width: 25%;
  height: 25%;
}

.center {
  width: 25%;
  justify-content: center; /* Center items horizontally */
  flex-direction: column;
}


</style>