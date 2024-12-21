<script lang="ts" setup>
import {ref, watch} from 'vue';
import type {TreeSelectProps} from 'ant-design-vue';

const value = ref<string>();
const treeData = ref<TreeSelectProps['treeData']>([
  {
    label: '词性',
    value: '词性',
    children: [
      {
        label: '名词',
        value: '动词',
      },
      {
        label: '动词',
        value: '动词',
      },
      {
        label: '形容词',
        value: '形容词',
      },
      {
        label: '副词',
        value: '副词',
      },
      {
        label: '代词',
        value: '代词',
      },
    ],
  },
  {
    label: '实体',
    value: '实体',
    children: [
      {
        label: '时间',
        value: '时间',
      },
      {
        label: '地点',
        value: '地点',
      },
      {
        label: '人物',
        value: '人物',
      },
    ],
  },
  {
    label: '情感',
    value: '情感',
    children: [
      {
        label: '中性',
        value: '中性',
      },
      {
        label: '正面',
        value: '正面',
      },
      {
        label: '负面',
        value: '负面',
      },
    ],
  }
]);
watch(value, () => {
  console.log(value.value);
});
const description = "Therr is a description";
</script>

<template>
  <main class="Container">
    <div class="left">
      <button> 人工标注</button>
      <button>智能标注</button>
    </div>

    <div class="center">
      <textarea v-model="description" rows="30" cols="30" readonly></textarea>
      <div class="center_bottom">
        <textarea v-model="description" rows="10" cols="30" readonly></textarea>
        <textarea v-model="description" rows="10" cols="30" readonly></textarea>
      </div>
      <div class="center_button">
        <button>分词</button>
        <button>翻译</button>
      </div>
      <div class="Mark_Select">
        <a-tree-select
            v-model:value="value"
            show-search
            style="width: 100%"
            :dropdown-style="{ maxHeight: '400px', overflow: 'auto' }"
            placeholder="Please select"
            allow-clear
            tree-default-expand-all
            :tree-data="treeData"
            tree-node-filter-prop="label">
          <template #title="{ value: val, label }">
            <b v-if="val === 'parent 1-1'" style="color: #08c">sss</b>
            <template v-else>{{ label }}</template>
          </template>
        </a-tree-select>
        <button style="margin-top: 1rem">确认</button>
      </div>
    </div>
    <div class="right">
      <button>上一份</button>
      <button>下一份</button>
    </div>
  </main>
</template>


<style scoped>

.Container {
  display: grid;
  width: 100%;
  height: 100%;
  grid-template-columns: 15% 70% 15%;
}

.left {
  display: flex;
  flex-direction: column; /* Arrange buttons vertically */
  align-items: flex-end; /* Align items to the right */
  margin-top: 2rem;
  gap: 2rem;
  margin-right: 2rem;
}

.right {
  display: flex;
  flex-direction: column; /* Arrange buttons vertically */
  align-items: flex-start; /* Align items to the left */
  margin-top: 2rem;
  gap: 2rem;
  margin-left: 2rem;
}

.center {
  display: flex;
  justify-content: flex-start; /* Center items horizontally */
  flex-direction: column;
  margin-top: 1rem;
}

.center_bottom {
  display: grid;
  justify-content: start;
  grid-template-columns: 45% 45%;
  gap: 10%;
  height: 100%;
  margin-top: 1rem;
}

.center_button {
  display: grid;
  grid-template-columns: 50% 50%;
  justify-content: center;
  margin-top: -7rem;
}

.Mark_Select {
  display: flex;
  justify-content: center;
  flex-direction: column;
  margin-top: 1rem;
}

button {
  background-color: lightskyblue;
  border-radius: 1rem;
  padding: 0.5rem 1rem;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

textarea {
  width: 100%; /* Set the width of the textarea */
  height: 60%; /* Set the height of the textarea */
  font-size: 0.8rem; /* Set the font size of the textarea */
  padding: 0.5rem; /* Add padding inside the textarea */
  border-radius: 0.5rem; /* Add border radius to the textarea */
  border: 1px solid #ccc; /* Add border to the textarea */
  resize: none; /* Disable resizing of the textarea */
}


</style>