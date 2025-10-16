<script setup>
import { RouterView } from 'vue-router';
import Head from './components/Head.vue';
</script>

<template>
  <main id="mainLibrary">
    <Head/>
    <RouterView/>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
  width: 100%;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>