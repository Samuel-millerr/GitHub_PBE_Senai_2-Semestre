<template>
  <div id="mainLibrary">
    <h1> Biblioteca </h1>

    <button @click="activeData = 'authors'">Autores</button>
    <button @click="activeData = 'publishers'">Editoras</button>
    <button @click="activeData = 'books'">Livros</button>

    <Authors v-if="activeData === 'authors'" :data="authors" title="Lista de Autores" />
    <Publishers v-if="activeData === 'publishers'" :publishers="posts" title="Lista de Editoras" />
    <Books v-if="activeData === 'books'" :data="books" title="Lista de Editoras" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import Authors from './components/authors.vue'
import Publishers from './components/publishers.vue'
import Books from './components/books.vue'

const activeData = ref('users')

const books = ref([])
const authors = ref([])
const publishers = ref([])

async function getData() {
  const resBooks = await fetch('http://127.0.0.1:8000/api/viewBook/')
  books.value = await resBooks.json()

  const resAuthors = await fetch('http://127.0.0.1:8000/api/viewAuthor/')
  authors.value = await resAuthors.json()

  const resPublishers = await fetch('http://127.0.0.1:8000/api/viewPublisher/')
  publishers.value = await resPublishers.json()
}

onMounted(() => {
  getData()
})
</script>
