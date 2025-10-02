<template>
  <main id="mainLibrary">
      <header>
      <h1 @click="activeData = ''"> Biblioteca </h1>

      
      <div>
        <button @click="activeData = 'authors'">Autores</button>
        <button @click="activeData = 'publishers'">Editoras</button>
        <button @click="activeData = 'books'">Livros</button>    
      </div>
    </header> 
      <Authors v-if="activeData === 'authors'" :data="authors" title="Lista de Autores" />
      <Publishers v-if="activeData === 'publishers'" :publishers="posts" title="Lista de Editoras" />
      <Books v-if="activeData === 'books'" :data="books" title="Lista de Editoras" />
  </main>
</template>

<script setup>
import { ref, onMounted, onDeactivated } from 'vue'

import Authors from './components/authors.vue'
import Publishers from './components/publishers.vue'
import Books from './components/books.vue'

const activeData = ref('')

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
  gap: 0.25rem;
  width: 100%;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

header {
  display: flex;
  justify-content: space-between;
  width: 100%;
  background-color: #2c3e50;
  color: white;
  padding: 2rem 3rem 2rem 3rem;
}

div {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

button {
  max-height: 2.5rem;
  padding: 0.4rem 1rem 0.4rem 1rem;
  font-size: 24px;
  font-weight: 500;
  border: none;
  background-color: transparent;
  color: white;
  transition: 1s;
  cursor: pointer;
}

button:hover {
  transform: translateY(-4px);
}

h1 {
  font-size: 38px;
  cursor: pointer;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.4s ease;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>