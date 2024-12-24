<script setup>
import {defineProps} from 'vue';
import Home_content from "@/components/Home_content.vue";
import Tasks from "@/components/Tasks.vue";
import Mark from "@/components/Mark.vue";

// 从父组件接收 selectedContent
const props = defineProps({
  selectedContent: {
    type: String,
    required: true
  }
});
</script>

<template>
  <div class="Right_Frame">
    <div class="top">
      <i class="iconfont icon-font"></i>
    </div>
    <div class="bottom">
      <div v-if="selectedContent === 'home'">
        <Home_content/>
      </div>
      <div v-else-if="selectedContent === 'tasks'">
        <Tasks/>
      </div>
      <div v-else-if="selectedContent === 'marking'">
        <Mark/>
      </div>
      <div v-else>
        <p>请选择一个菜单项</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.Right_Frame {
  display: grid;
  grid-template-rows: 10% 90%;
  height: 100%;
}

.top {
  display: flex;
  justify-content: flex-end; /* 将子元素推到右边 */
  align-items: center; /* 垂直居中对齐 */
  height: 100%; /* 设置顶部区域的高度 */
  padding-right: 1rem; /* 可选：设置右侧内边距 */
  background-color: floralwhite;
}

.Right_Frame .top i {
  font-size: 30px; /* 设置图标大小 */
  color: #2c3e50; /* 设置图标颜色 */
  cursor: pointer; /* 改变鼠标为手型 */
  transition: color 0.3s ease, transform 0.3s ease; /* 平滑过渡效果 */
}

.bottom {
  height: 100%;
  background-color: white;
  border-radius: 0 0 1rem 0;
}

@media (min-width: 1024px) {
  .Right_Frame {
    grid-template-rows: 10% 90%;
  }
}

</style>