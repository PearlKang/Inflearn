import { createRouter, createWebHistory } from "vue-router";

import Home from "../pages/Home.vue";
import Messages from "../pages/Messages.vue";
import Notifications from "../pages/Notifications.vue";
import Profile from "../pages/Profile.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/messages", component: Messages },
  { path: "/notifications", component: Notifications },
  { path: "/profile", component: Profile },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
