import { createApp } from 'vue';
import router from './router';
import App from './App.vue';
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000'; // Django Backend URL
axios.defaults.headers.common['Content-Type'] = 'application/json';
const app = createApp(App);
app.use(router);
app.mount('#app');
