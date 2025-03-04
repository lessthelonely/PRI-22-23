import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import axios from 'axios';
import router from './router'

axios.defaults.withCredentials = false;
axios.defaults.baseURL = 'http://localhost:8080/';

//Bootstrap imports
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import './assets/css/styles.css'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faAngleDoubleDown, faAngleDoubleUp, faStar, faSearch, faPlus, faUser, faTimes, faMinus, faArrowLeft, faArrowRight} from '@fortawesome/free-solid-svg-icons'

library.add(faAngleDoubleDown, faAngleDoubleUp,faStar, faSearch, faPlus, faUser, faTimes, faMinus, faArrowLeft, faArrowRight)

const app = createApp(App)
app.use(router)
app.component('FontAwesomeIcon', FontAwesomeIcon);
app.mount('#app')