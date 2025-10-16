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
  <article>
    <h1>Lista de Livros</h1>
    <table>
      <thead>
        <tr>
          <th> Titulo </th>
          <th> ISBN </th>
          <th> Ano de Publicação </th>
          <th> Autor </th>
          <th> Editora </th>
          <th> Páginas </th>
          <th> Preço </th>
          <th> Estoque </th>
          <th> Disponível </th>
          <th> Peso </th>
          <th> Dimensões </th>
        </tr>
      </thead>
      <tr v-for="book in books" :key="book.id" @click="goToBookDetails(book.id)">
        <td> {{ book.titulo }} </td> 
        <td> {{ book.isbn }}</td>
        <td> {{book.ano_publicacao}} </td> 
        <td> {{book.autor.nome }}  </td> 
        <td> {{ book.editora.nome }} </td> 
        <td> {{ book.paginas}} </td>
        <td> R$ {{ book.preco }}</td>
        <td> {{ book.estoque }}</td>
        <td> {{ book.disponivel ? 'Sim' : 'Não' }} </td>
        <td> {{ book.peso }}</td>
        <td> {{ book.dimensoes }}</td>
      </tr>
    </table>
  </article>
</template>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 0.5rem;
  font-family: Arial, sans-serif;
  font-size: 0.85rem; 
  cursor: pointer;
}

table th,
table td {
  border: 1px solid #ccc;
  padding: 6px 8px;
  font-size: 20px;
  text-align: left;
  vertical-align: top;
}

table th {
  background-color: #2c3e50;
  color: white;
  font-weight: 600;
  font-size: 18px;
  padding: 0.5rem;
}

table tr:hover {
  background-color: #f1f1f1;
}

table td {
  color: #333;
  line-height: 1.3;
}
</style>