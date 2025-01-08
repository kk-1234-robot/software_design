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
          description: '点击左侧标注任务框，跳转到标注任务界面，输入标注任务名称以及轮次，最后将.csv文件拖入上传文件框中（或点击上传文件框再选择文件路径），上传文件。',
        },
        {
          title: 'Step 2',
          description: '- 点击左侧标注框，跳转到标注界面。\n'+
'- 点击上一份或下一份按键切换标注的按键\n'+
'- 在案件文本框内修改案件后点击更新案件可以将案件信息更新\n'+
'- 点击上一句或下一句切换标注的句子\n'+
'- 开始标注\n'+
'  - 点击智能标注，可以将本句词语进行自动标注\n'+
'  - 点击上一个词或者下一个词可以查看本句中不同词语的标注情况，点击词性和实体按键可以看到其标注的词性和实体，勾选其下拉的选项后点击提交选择可以修改词性和实体标注情况',
        },
        {
          title: 'Step 3',
          description: '- 查看结果：点击左侧结果框，跳转到结果界面可以查看所有已标注案件中的词性和实体分别情况\n'+
'- 保存结果：在结果界面点击导出数据可以将标注的数据导出',
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