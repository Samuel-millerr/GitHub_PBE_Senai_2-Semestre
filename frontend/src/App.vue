<template>
  <main id="mainLibrary">
    <h1> Biblioteca </h1>

    <div>
      <button @click="activeData = 'authors'">Autores</button>
      <button @click="activeData = 'publishers'">Editoras</button>
      <button @click="activeData = 'books'">Livros</button>
    </div>

    <section>
      <Authors v-if="activeData === 'authors'" :data="authors" title="Lista de Autores" />
      <Publishers v-if="activeData === 'publishers'" :publishers="posts" title="Lista de Editoras" />
      <Books v-if="activeData === 'books'" :data="books" title="Lista de Editoras" />
    </section>
  </main>
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

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  height: 100vh;
  width: 100%;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

section {
  margin-top: 1rem;
  background-color: skyblue;
  color: white;
  padding: 1rem 1.5rem 1rem 1.5rem;
  border-radius: 0.25rem;
}

div {
  display: flex;
  justify-content: space-between;
  width: 25%;
}

button {
  padding: 0.5rem 1rem 0.5rem 1rem;
  border-radius: 0.25rem;
  font-size: 18px;
  font-weight: 500;
  border: none;
  background-color: white;
  color: black;
  box-shadow: 0 0 5px 1px black;
  transition: 1s;
}

button:hover {
  transform: translateY(-2px);
}

article {
  font-size: 22px;
}
</style>