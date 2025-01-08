<template>
  <div>
    <!-- 展示软件使用步骤 -->
    <a-steps
        v-model:current="current"
        direction="vertical"
        size="default"
        :items="[
        {
          title: 'Step 1',
          description: '在标注任务页面中上传待标注的csv格式文件',
        },
        {
          title: 'Step 2',
          description: '在标注页面点击“下一份“选中文本，点击”下一句“选中文本中的句子，点击智能标注可以自动完成一个句子的标注。点击”下一个词“可以选中句子中的词，在下拉菜单中进行人工标',
        },
        {
          title: 'Step 3',
          description: '在结果页面中可以看到标注结果的图表，点击“导出结果”可以导出标注后的csv格式文件',
        },
      ]"
    ></a-steps>
  </div>
</template>
<script lang="ts" setup>
import {ref} from 'vue';

const current = ref<number>(0);

</script>

<style scoped>

</style>