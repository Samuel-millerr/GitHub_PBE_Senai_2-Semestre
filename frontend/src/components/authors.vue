<template>
  <div>
    <h1>Lista de Livros</h1>
    <ul>
      <li v-for="author in authors" :key="authors.id">
        {{author.nome }} - {{author.sobrenome}} - {{author.nacionalidade}}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const authors = ref([])

async function getAuthors() {
  const response = await fetch('http://127.0.0.1:8000/api/viewAuthor/')
  const data = await response.json()
  authors.value = data
}

onMounted(() => {
  getAuthors()
})

defineExpose({
  authors
})
</script>
