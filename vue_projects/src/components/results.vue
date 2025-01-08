<template>
  <!-- The DOM element for ECharts -->
  <div class="container">
    <div class="chart">
      <div ref="chartPos" style="width: 400px; height: 400px;"></div>
      <div ref="chartEntity" style="width: 400px; height: 400px;"></div>
    </div>
    <button @click = "export_data" >导出数据</button>
  </div>


</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import axios from 'axios';
import * as echarts from 'echarts';

// Reference to the HTML element where the chart will be rendered
const chartPos = ref<HTMLElement | null>(null);
const chartEntity = ref<HTMLElement | null>(null);

// We'll store the fetched data in these refs
const PosData = ref([0,0,0,0,0]);
const EntityData = ref([0,0,0]);

// Load data and initialize the chart once the component is mounted
onMounted(async () => {
  try {
    // Fetch data from the API
    const response0 = await axios.get('http://localhost:8000/GetPos/');
    PosData.value = response0.data;
    const response1 = await axios.get('http://localhost:8000/GetEntity/');
    EntityData.value = response1.data;

    // Initialize the chart and set options
    if (chartPos.value && chartEntity.value) {
      const myChart = echarts.init(chartPos.value);
      const myChart1 = echarts.init(chartEntity.value);

      const option: echarts.EChartsOption = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: ['名词','动词','形容词','副词','代词'],
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Direct',
            type: 'bar',
            barWidth: '60%',
            data: PosData.value
          }
        ]
      };

      const option1: echarts.EChartsOption = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: ['人名','地名','地名'],
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Direct',
            type: 'bar',
            barWidth: '60%',
            data: EntityData.value
          }
        ]
      };

      myChart.setOption(option);
      myChart1.setOption(option1);

    }

  } catch (error) {
    console.error('Error fetching chart data:', error);
  }
});


async function export_data(){
  const response = await axios.get('http://localhost:8000/export_data/');
  console.log(response.data);
}
</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.chart {
  display: flex;
  justify-content: space-around;
  flex-direction: row;
  gap: 20px;
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
</style>