<template>
  <article>
    <h1>Lista de Autores</h1>
    <table>
      <thead>
        <th> Nome </th>
        <th> Sobrenome </th>
        <th> Data de Nascimento </th>
        <th> Nacionalidade </th>
      </thead>
      <tr v-for="author in authors" :key="authors.id">
        <td> {{author.nome }} </td>
        <td> {{author.sobrenome}} </td>
        <td> {{author.data_nascimento}}</td>
        <td> {{author.nacionalidade}} </td>
      </tr>
    </table>
  </article>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const authors = ref([]);

async function getAuthors() {
  const response = await fetch('http://127.0.0.1:8000/api/viewAuthor/');
  const data = await response.json();
  authors.value = data;
}

onMounted(() => {
  getAuthors();
})

defineExpose({
  authors
})
</script>

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