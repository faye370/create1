<template>
  <div>
    <h2>员工管理</h2>
    <el-table :data="[]">
      <el-table-column prop="id" label="ID" />
      <el-table-column prop="name" label="姓名" />
      <el-table-column prop="department" label="部门" />
      <el-table-column prop="position" label="职位" />
    </el-table>
  </div>
</template>

<script setup>
// 这里可以添加获取员工数据的逻辑
</script> 