import './assets/main.css'

//引入CreateApp用于创建应用
import {createApp} from 'vue';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import Antd from 'ant-design-vue';
import App from './MY_APP.vue';
import './assets/iconfont/iconfont.css';
import 'ant-design-vue/dist/reset.css';

const app = createApp(App)

// app.use(router)
app.use(ElementPlus)
app.use(Antd).mount('#app');