import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

import 'bootstrap/dist/css/bootstrap.min.css';
// import 'bootstrap-vue/dist/bootstrap-vue.css' // Uncomment if using BootstrapVue

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faUser, faEnvelope } from '@fortawesome/free-solid-svg-icons';
import { faGithub, faLinkedin, faSearchengin } from '@fortawesome/free-brands-svg-icons';


// Default API base URL
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL
})

// Add icons to the library
library.add(faUser, faEnvelope, faGithub, faLinkedin, faSearchengin);
console.log('Icons added:', { faUser, faEnvelope, faGithub, faLinkedin });

const app = createApp(App);
app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon); // Fixed typo
app.mount('#app');
app.provide("api", api)
