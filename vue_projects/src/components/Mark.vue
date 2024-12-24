<script setup>

import {Button} from 'ant-design-vue';
import Mark_top from "@/components/Mark_top.vue";
import Mark_center from "@/components/Mark_center.vue";
import Mark_bottom from "@/components/Mark_bottom.vue";

</script>


<template>

  <body class="Container">
  <div class="top">
    <Mark_top/>
  </div>
  <!--  <div class="bottom">-->
  <!--    <p>bottom</p>-->
  <!--  </div>-->
  </body>


</template>


<style scoped>


html, body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

.Container {
  display: grid;
  grid-template-rows: 100%;
  height: 100%;
}


.top {
  width: 100%;
  background-color: palegreen;
}

.center {
  width: 100%;
  background-color: #0077aa;
}

.bottom {
  width: 100%;
  background-color: #ffcc00;
}

</style>