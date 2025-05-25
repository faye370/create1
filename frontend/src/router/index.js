import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Employee from '../views/Employee.vue'
import Department from '../views/Department.vue'
import Attendance from '../views/Attendance.vue'
import Performance from '../views/Performance.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { 
    path: '/employee', 
    component: Employee,
    meta: { requiresAuth: true }
  },
  { 
    path: '/department', 
    component: Department,
    meta: { requiresAuth: true }
  },
  { 
    path: '/attendance', 
    component: Attendance,
    meta: { requiresAuth: true }
  },
  { 
    path: '/performance', 
    component: Performance,
    meta: { requiresAuth: true }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  
  if (to.meta.requiresAuth && !token) {
    // 需要登录但没有 token，重定向到登录页
    next('/login')
  } else if (to.path === '/login' && token) {
    // 已登录用户访问登录页，重定向到首页
    next('/employee')
  } else {
    next()
  }
})

export default router 