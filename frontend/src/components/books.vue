<template>
  <article>
    <h1>Lista de Livros</h1>
    <ul>
      <li v-for="book in books" :key="book.id">
        {{ book.titulo }} - {{book.subtitulo}} - ({{book.ano_publicacao}})
      </li>
    </ul>
  </article>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const books = ref([])

async function getBooks() {
  const response = await fetch('http://127.0.0.1:8000/api/viewBook/')
  const data = await response.json()
  books.value = data
}

onMounted(() => {
  getBooks()
})

defineExpose({
  books
})
</script>
