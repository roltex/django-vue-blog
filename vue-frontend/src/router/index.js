import { createRouter, createWebHistory } from 'vue-router';
import BlogList from '../views/Home.vue';
import BlogDetailsView from '../views/BlogDetailsView.vue';

const routes = [
  { path: '/', name: 'Home', component: BlogList },
  { path: '/blog/:id', name: 'BlogDetails', component: BlogDetailsView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
