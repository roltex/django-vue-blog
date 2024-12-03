<template>
  <div>
    <Menu /> <!-- Top Menu Component -->
    <router-view /> <!-- Render Pages Based on Route -->
  </div>
</template>

<script setup>
import Menu from './components/Menu.vue';
</script>
