import { createRouter, createWebHistory } from 'vue-router';
import Restaurants from '../views/Restaurants.vue';
import EditRestaurants from '../views/EditRestaurants.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    redirect: { name: 'Restaurants' }
  },
  {
    path: '/restaurants',
    name: 'Restaurants',
    component: Restaurants
  },
  {
    path: '/edit-restaurants',
    name: 'EditRestaurants',
    component: EditRestaurants
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
