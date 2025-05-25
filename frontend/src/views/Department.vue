<template>
  <div>
    <h2>部门管理</h2>
    <el-table :data="[]">
      <el-table-column prop="id" label="ID" />
      <el-table-column prop="name" label="部门名称" />
      <el-table-column prop="manager" label="负责人" />
    </el-table>
  </div>
</template>

<script setup>
// 这里可以添加获取部门数据的逻辑
</script> 