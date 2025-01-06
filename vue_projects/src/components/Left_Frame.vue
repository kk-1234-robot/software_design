<script setup>
import {defineProps, defineEmits} from 'vue';

// 从父组件接收 selectedContent
const props = defineProps({
  selectedContent: {
    type: String,
    required: true
  }
});

// 定义一个事件来通知父组件改变内容
const emit = defineEmits(['update:selectedContent']);

function changeContent(content) {
  emit('update:selectedContent', content); // 触发事件，通知父组件改变 selectedContent
}
</script>

<template>

  <div class="Left_Frame">
    <i class="iconfont icon-font" @click="changeContent('home')">首页</i>
    <i class="iconfont icon-targets" @click="changeContent('tasks')">标注任务</i>
    <i class="iconfont icon-marking" @click="changeContent('marking')">标注</i>
    <i class="iconfont icon-results" @click="changeContent('results')">结果</i>
  </div>


</template>


<style scoped>

.Left_Frame {
  display: grid;
  height: 100vh;
  width: 100%;
  background-color: #2c3e50;
  gap: 10px;
  grid-template-rows: 10% 10% 10%; /* 将容器分为三行 */
}

.Left_Frame i {
  height: 20%; /* 每个 <i> 元素占容器的 10% 高度 */
  width: 100%;
  display: flex; /* 使 <i> 元素可灵活使用对齐方式 */
  align-items: center; /* 垂直居中对齐图标和文本 */
  justify-content: center; /* 水平居中对齐图标和文本 */
  cursor: pointer; /* 改变鼠标样式，表示该元素可点击 */
  transition: background-color 0.3s ease; /* 增加过渡效果，使背景颜色变化更平滑 */
}

.iconfont {
  font-size: 40px;
  color: white;
  border-radius: 1rem;
}

@media (min-width: 1024px) {
  .Container {
    background-color: #2c3e50;
    width: 50%;
    padding-right: 1rem;
  }
}

.Left_Frame {
  display: flex;
  height: 100vh;
  width: 100%;
  background-color: #2c3e50;
  gap: 10px;
  flex-direction: column;
  border-radius: 1rem 0 0 1rem;
}

.Left_Frame i {
  height: 10%; /* 每个 <i> 元素占容器的 10% 高度 */
  display: flex; /* 使 <i> 元素可灵活使用对齐方式 */
  align-items: center; /* 垂直居中对齐图标和文本 */
  justify-content: center; /* 水平居中对齐图标和文本 */
}

.iconfont {
  font-size: 15px;
  color: white;
}

/* 鼠标悬停时改变背景颜色 */
.Left_Frame i:hover {
  background-color: #34495e; /* 背景色变浅 */
}


/* 如果需要在选中的状态下改变背景颜色，可以添加额外的样式 */
.Left_Frame i.selected {
  background-color: #16a085; /* 选中时背景色 */
}

</style>


