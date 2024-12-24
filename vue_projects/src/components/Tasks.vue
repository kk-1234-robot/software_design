<script setup>
import {Button} from 'ant-design-vue';
import Uploader from './Uploader.vue';

// import {watch, ref} from 'vue';

// const Name = ref < string > ('');
// const Number = ref < number > (0);

// watch(Name, () => {
//   console.log(Name.value);
// });
//
// watch(Number, () => {
//   console.log(Number.value);
// });

</script>


<template>
  <div class="Container">

    <div class="Task_Name">
      <label for="taskName">标注任务名称</label>
      <input type="text" id="taskName" v-model="taskName"/>

      <label for="round">轮次</label>
      <input type="text" id="round" v-model="round"/>
    </div>

    <div class="Task_Upload">
      <Uploader/>
      <Button> 确认上传</Button>
    </div>

  </div>
</template>


<style scoped>

.Container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around; /* Distribute space evenly */
  height: 100%;
  gap: 20px;
  background-color: white;
}

.Task_Upload {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5%;
  width: 85%;
}

.Task_Name {
  display: flex;
  flex-direction: column; /* Align items vertically */
  align-items: center;
}

.Task_Upload button {
  background-color: lightskyblue;
  color: white;
  border: none;
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"] {
  width: 100%;
  padding: 8px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
}


</style>


<script>
export default {
  data() {
    return {
      taskName: '',
      round: ''
    };
  }
};
</script>