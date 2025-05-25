<template>
  <div>
    <h2>考勤管理</h2>
    <el-table :data="[]">
      <el-table-column prop="id" label="ID" />
      <el-table-column prop="employee" label="员工" />
      <el-table-column prop="date" label="日期" />
      <el-table-column prop="status" label="状态" />
    </el-table>
  </div>
</template>

<script setup>
// 这里可以添加获取考勤数据的逻辑
</script> 