<template>
  <div>
    <h2>绩效管理</h2>
    <el-table :data="[]">
      <el-table-column prop="id" label="ID" />
      <el-table-column prop="employee" label="员工" />
      <el-table-column prop="score" label="分数" />
      <el-table-column prop="comment" label="评价" />
    </el-table>
  </div>
</template>

<script setup>
// 这里可以添加获取绩效数据的逻辑
</script> 