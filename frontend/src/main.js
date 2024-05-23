import { createApp } from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import { createPinia } from 'pinia';
import router from './router';
import keycloak from './keycloak';

const pinia = createPinia();

keycloak.init({ onLoad: 'login-required' }).then(() => {
  createApp(App)
    .use(vuetify)
    .use(pinia)
    .use(router)
    .mount('#app');
}).catch(error => {
  console.error('Keycloak initialization failed', error);
});
