<template>
  <main class="Container">
    <div class="left">
      <button> 人工标注</button>
      <button @click = "annotation_api" >智能标注</button>
    </div>

    <div class="center">
      <textarea v-model="description" rows="30" cols="30" readonly></textarea>
      <div class="center_bottom">
        <textarea v-model="subDescription1" rows="10" cols="30" readonly></textarea>
        <textarea v-model="subDescription2" rows="10" cols="30" readonly></textarea>
      </div>
      <div class="center_button">
        <button>分词</button>
        <button @click = "translate_api">翻译</button>
        <button @click = "previous_sentences">上一句</button>
        <button @click="next_sentences">下一句</button>
      </div>
      <div class="Mark_Select">
        <div class="dropdown-container" @click.stop>
          <!-- 主按钮：点击可控制下拉菜单的显隐 -->
          <input v-model="DispWord" class="dropdown-btn" disabled>

          </input>

          <!-- 下拉菜单内容区域 -->
          <div v-if="isOpen" class="dropdown-menu">
            <!-- 子菜单 A -->
            <div class="submenu">
              <div class="submenu-title" @click="toggleSubmenu('A')">
                词性
              </div>
              <div v-if="submenuOpen.A" class="submenu-content">
                <div
                    v-for="(option, index) in submenuOptionsA"
                    :key="index"
                    class="submenu-option"
                >
                  <input
                      type="checkbox"
                      :id="`a-option-${index}`"
                      :value="option.value"
                      v-model="selectedOptionsA"
                  />
                  <label :for="`a-option-${index}`">
                    {{ option.label }}
                  </label>
                </div>
              </div>
            </div>

            <!-- 子菜单 B -->
            <div class="submenu">
              <div class="submenu-title" @click="toggleSubmenu('B')">
                实体
              </div>
              <div v-if="submenuOpen.B" class="submenu-content">
                <div
                    v-for="(option, index) in submenuOptionsB"
                    :key="index"
                    class="submenu-option"
                >
                  <input
                      type="checkbox"
                      :id="`b-option-${index}`"
                      :value="option.value"
                      v-model="selectedOptionsB"
                  />
                  <label :for="`b-option-${index}`">
                    {{ option.label }}
                  </label>
                </div>
              </div>
            </div>

            <!-- 提交按钮：收集已选值并发送到后端 -->
            <button @click.prevent="submitSelection" class="submit-btn">
              提交选择
            </button>
          </div>
        </div>
      </div>
      <div class="Submission_buttons">
        <button @click="previous_word">上一个词</button>
        <button @click="next_word">下一个词</button>
      </div>
      <button @click="submitAnnotations">提交标注</button>

    </div>
    <div class="right">
      <!-- 使用上一份和下一份维护1个变量n，初始化为1，点击上一份则减1，点击下一份则加1 -->
      <button @click="previous">上一份</button>
      <button @click="next">下一份</button>
    </div>
  </main>
</template>


<script lang="ts" setup>
import {ref, watch, onMounted, reactive} from 'vue';
import axios from "axios";
import type {TreeSelectProps} from 'ant-design-vue';

const value = ref<string>();
const treeData = ref<TreeSelectProps['treeData']>([
  {
    label: '词性',
    value: '词性',
    children: [
      {
        label: '名词',
        value: '名词',
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
const description = ref(""); // 主显示文本
const subDescription1 = ref(""); // 子显示文本1
const subDescription2 = ref(""); // 子显示文本2
const subDescription3 = ref(""); // 子显示文本3
const loading = ref(false); // 加载状态
const errorMessage = ref(""); // 错误信息


const number = ref(0);

const num_sentences = ref(0);

const num_words = ref(0);

const words = ref([])

const DispWord = ref('')
// 定义可选择的标注信息，视实际需求而定
const dropdownOptions = ref([
  // value 可以是 pos 值或 entity 值，还可以做层级子选项
  { label: '名词(pos)', value: 'NOUN' },
  { label: '动词(pos)', value: 'VERB' },
  { label: '地点(entity)', value: 'LOCATION' },
  { label: '实体(entity)', value: 'entity' },
  // ...
])






// onMounted(async () => {
//   // 1. 从后端接口获取该句子的所有分词
//   // 假设后端返回的数据结构形如：
//   // [
//   //   { id: 101, word: '我', pos: 'NOUN', entity: '', count: 3 },
//   //   { id: 102, word: '喜欢', pos: '', entity: '', count: 1 },
//   //   ...
//   // ]
//   // 前端可以自行给每个对象加上 selectedAnnotations (空数组)，以便在多选下拉中存储用户的标注
//   try {
//     const res = await axios.get('https://localhost:8080/get_words')
//     words.value = res.data.map(item => ({
//       ...item,
//       selectedAnnotations: []
//     }))
//   } catch (err) {
//     console.error('获取分词数据失败: ', err)
//   }
// })

async function submitAnnotations() {
  // 打包并发送到后端
  // 后端根据 id 来更新对应 word 的标注信息
  // 这里只是示例，真实逻辑需要根据您的标注字段(pos、entity、count)如何存储来做区分
  try {
    const payload = {
      words: words.value.map(w => ({
        id: w.id,
        selectedAnnotations: w.selectedAnnotations
      }))
    }
    await axios.post('https://localhost:8000/annotate_word', payload)
    alert('标注信息已成功更新至后端！')
  } catch (err) {
    console.error('标注信息提交失败: ', err)
  }
}

async function fetchData() {
  loading.value = true;  // 开始加载
  errorMessage.value = ""; // 清空错误信息
  try {
    const response = await axios.get("http://127.0.0.1:8000/view_train/", {
      params: {number: number.value},
    });
    description.value = response.data; // 将返回的数据绑定到 description
  } catch (error) {
    console.error("Error fetching data:", error);
    description.value = "获取数据失败，请稍后重试。";
  }
}

function next() {
  number.value++;
  fetchData(); // 调用获取数据函数
}

function previous() {
  if (number.value > 1) {
    number.value--;
    fetchData(); // 调用获取数据函数
  }
}


async function fetchData_split() {
  loading.value = true;  // 开始加载
  errorMessage.value = ""; // 清空错误信息
  try {
    const response = await axios.get("http://127.0.0.1:8000/split_sentences/", {
      params: {num_sentences: num_sentences.value, number: number.value},
    });
    subDescription1.value = response.data; // 将返回的数据绑定到 description
  }
  catch (error) {
    console.error("Error fetching data:", error);
    subDescription1.value = "获取数据失败，请稍后重试。";
  }
}

async function getWords()
{
  loading.value = true;  // 开始加载
  errorMessage.value = ""; // 清空错误信息
  try {
    const response = await axios.get("http://127.0.0.1:8000/get_words/", {
      params: { number: number.value,num_sentences: num_sentences.value, num_words: num_words.value},
    });
    DispWord.value = response.data;
}
  catch (error) {
    console.error("Error fetching data:", error);
  }
}

async function translate_api()//翻译一个句子
{
  loading.value = true;  // 开始加载
  errorMessage.value = ""; // 清空错误信息
  try {
    const response = await axios.get("http://127.0.0.1:8000/translate_sentence/", {
      params: {num_sentences: num_sentences.value, number: number.value},
    });
    subDescription2.value = response.data; // 将返回的数据绑定到 description
  }
  catch (error) {
    console.error("Error fetching data:", error);
    subDescription2.value = "获取数据失败，请稍后重试。";
  }
}

async function annotation_api() {
  loading.value = true;  // 开始加载
  errorMessage.value = ""; // 清空错误信息
  try {
    const response = await axios.get("http://127.0.0.1:8000/annotation_by_llm/", {
      params: {num_sentences: num_sentences.value, number: number.value},
    });
  }
  catch (error) {
    console.error("Error", error);
  }
}

function next_sentences() {
  num_sentences.value++;
  num_words.value = 1;
  fetchData_split(); // 调用获取数据函数
}

function previous_sentences() {
  if (num_sentences.value > 1) {
    num_sentences.value--;
    num_words.value = 1;
    fetchData_split(); // 调用获取数据函数
  }
}


//上一句
function previous_word() {
  if (num_words.value > 1) {
    num_words.value--;
    getWords();
  }
}

//下一句
function next_word() {
  num_words.value++;
  getWords();
}

// 初始化时获取第一份数据
fetchData();



// 控制主下拉的显隐
const isOpen = ref(true)

// 控制各子菜单的显隐
const submenuOpen = reactive({
  A: false,
  B: false
})

// 子菜单 A 的选项
const submenuOptionsA = ref([
  { label: '名词', value: 'n' },
  { label: '动词', value: 'v' },
  { label: '形容词', value: 'adj' },
  { label: '副词', value: 'adv' },
  { label: '代词', value: 'pron' },
])

// 子菜单 B 的选项
const submenuOptionsB = ref([
  { label: '人物', value: 'person' },
  { label: '时间', value: 'time' },
  { label: '地点', value: 'location' },
])

// 用于储存已选选项的数组
const selectedOptionsA = ref([])
const selectedOptionsB = ref([])

// 点击主按钮，展开/收起下拉菜单
const toggleDropdown = () => {
  isOpen.value = !isOpen.value
}

// 控制子菜单展开/收起
const toggleSubmenu = (type) => {
  submenuOpen[type] = !submenuOpen[type]
}

// 提交所选的选项
const submitSelection = async () => {
  // 将子菜单 A, B 的已选项合并或分开处理都可，这里示例为合并发送
  const payload = {
    selectedA: selectedOptionsA.value,
    selectedB: selectedOptionsB.value,
    number: number.value,
    num_sentences: num_sentences.value,
    num_words: num_words.value
  }

  try {
    // 使用 Axios 发送 POST 请求到 Django 后端
    const response = await axios.post('http://localhost:8000/GetSubmission/', payload)

    // 根据响应处理后续逻辑
    console.log('后端响应：', response.data)
    alert('提交成功！')
  } catch (error) {
    console.error('提交时出错:', error)
    alert('提交失败，请重试。')
  }
}


</script>


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
  justify-content: start;
  margin-top: -10rem;
}

.center_last {
  display: flex;
  justify-content: flex-start;
  margin-top: 1rem;
}

.center_last textarea {
  width: 100%;
  height: 40%;
}

.Mark_Select {
  display: flex;
  justify-content: center;
  flex-direction: row;
  margin-top: 1rem;
}


.Submission_buttons
{
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 4rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
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