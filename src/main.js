import './assets/main.css'

//引入CreateApp用于创建应用
import {createApp} from 'vue'
import App from './MY_APP.vue'
import './assets/iconfont/iconfont.css'

const app = createApp(App)

// app.use(router)

app.mount('#app')