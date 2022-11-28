import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import axios from 'axios';
import router from './router'

axios.defaults.withCredentials = false;
axios.defaults.baseURL = 'http://localhost:3001/';

//Bootstrap imports

const app = createApp(App)
app.use(router)
app.mount('#app')