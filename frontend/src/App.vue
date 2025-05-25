<script setup>
import { useRouter } from 'vue-router'
import { logout } from './api/auth'
import { ElMessage } from 'element-plus'

const router = useRouter()

const handleLogout = async () => {
  try {
    await logout()
    localStorage.removeItem('token')
    ElMessage.success('退出成功')
    router.push('/login')
  } catch (error) {
    ElMessage.error(error.message || '退出失败')
  }
}
</script>

<template>
  <el-container style="height: 100vh">
    <el-header>
      <el-menu :default-active="$route.path" mode="horizontal" router>
        <el-menu-item index="/employee">员工管理</el-menu-item>
        <el-menu-item index="/department">部门管理</el-menu-item>
        <el-menu-item index="/attendance">考勤管理</el-menu-item>
        <el-menu-item index="/performance">绩效管理</el-menu-item>
        <div style="float: right; margin-top: 15px;">
          <el-button type="danger" @click="handleLogout">退出登录</el-button>
        </div>
      </el-menu>
    </el-header>
    <el-main>
      <router-view />
    </el-main>
  </el-container>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>

<style>
body {
  margin: 0;
}
</style>
