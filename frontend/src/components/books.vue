<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const books = ref([]);
const router = useRouter();

async function getBooks() {
  const response = await fetch('http://127.0.0.1:8000/api/viewBook/');
  const data = await response.json();
  books.value = data;
  console.log(books)
}

onMounted(() => {
  getBooks();
})

function goToBookDetails(bookId) {
  router.push({name: "BookDetails", params: {id: bookId}})
}
</script>

<template>
  <section>
    <h1 id="title">Livros</h1>
    <div class="livros-container">
      <div v-for="book in books" :key="books.id" class="livro-card" @click="goToBookDetails(book.id)">
        <img :src="book.capa" alt="Capa do livro">
        <div class="livro-info">
            <h3>{{ book.titulo }}</h3>
            <p class="autor">{{ book.autor.nome }} {{ book.autor.sobrenome }}</p>
            <p class="editora">{{ book.editora.nome }}</p>
            <p class="preco"> R$ {{ book.preco }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
section{
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 4vh;
    margin-bottom: 10rem;
}
 
#title{
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 32px;
}
 
.livros-container{
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    padding: 5vh;
    padding: 3vh;
    gap: 23px;
}
  .livro-card {
    width: 300px;
    background-color: #fff;
    border-radius: 15px;
    overflow: hidden;
    transition: all 0.3s ease;
    text-align: center;
    padding: 1rem;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
 
 
.livro-card img {
    width: 230px;
    height: 330px;
    object-fit: fill;
    display: block;
    border-radius: 0.25rem;
}
 
.livro-card .livro-info {
    padding: 12px;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 16px;
}
 
.livro-card h3 {
   
    margin: 8px 0 4px 0;
}
 
.livro-card .autor,
.livro-card .editora,
.livro-card .preco {
    font-size: 14px;
    margin: 2px 0;
    color: #555;
}
 
.livro-card:hover {
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    transform: translateY(-4px);
}
</style>