import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import axios from 'axios';
import router from './router'

axios.defaults.withCredentials = false;
axios.defaults.baseURL = 'http://localhost:3001/';

//Bootstrap imports
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import './assets/styles.css'


const app = createApp(App)
app.use(router)
app.mount('#app')