import { createRouter, createWebHistory } from 'vue-router';
import Restaurants from '../views/Restaurants.vue';
import EditRestaurants from '../views/EditRestaurants.vue';
import keycloak from '../keycloak';

const routes = [
  {
    path: '/',
    name: 'Home',
    redirect: { name: 'Restaurants' }
  },
  {
    path: '/restaurants',
    name: 'Restaurants',
    component: Restaurants,
    meta: { requiresAuth: true }
  },
  {
    path: '/edit-restaurants',
    name: 'EditRestaurants',
    component: EditRestaurants,
    meta: { requiresAuth: true }
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!keycloak.authenticated) {
      keycloak.login();
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
