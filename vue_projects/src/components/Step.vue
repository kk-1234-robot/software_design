<script setup>
import {defineProps} from 'vue';

const props = defineProps({
  stepNumber: {
    type: Number,
    required: true
  },
  stepText: {
    type: String,
    required: true
  }
});
</script>

<template>
  <div class="Step">
    <!-- 根据 props.stepNumber 的值显示不同的样式 -->
    <div :class="['step-item', `step-item-${props.stepNumber}`]">
      <i class="iconfont icon-font">Step {{ props.stepNumber }}</i>
      <p>{{ props.stepText }}</p>
    </div>
  </div>
</template>

<style scoped>
.Step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5%;
  height: 100%;
  width: 100%;
}

.step-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.step-item-1 {
  color: lightblue;
}

.step-item-2 {
  color: lightgreen;
}

.step-item-3 {
  color: lightcoral;
}

.step-item i {
  font-size: 20px;
  transition: color 0.3s ease, transform 0.3s ease;
}

.step-item p {
  font-size: 20px;
}

@media (min-width: 1024px) {
  .Step {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>