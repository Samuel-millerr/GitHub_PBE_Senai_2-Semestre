<template>
  <article>
    <h1>Lista de Editoras</h1>
    <table>
      <thead>
        <th> Nome </th>
        <th> CNPJ </th>
        <th> Telefone </th>
        <th> Email </th>
        <th> Site </th>
      </thead>
      <tr v-for="publisher in publishers" :key="publishers.id">
        <td> {{publisher.nome }} </td>
        <td> {{publisher.cnpj}} </td>
        <td> {{publisher.telefone}} </td>
        <td> {{publisher.email}} </td>
        <td> {{publisher.site}} </td>
      </tr>
    </table>
  </article>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const publishers = ref([])

async function getPublishers() {
  const response = await fetch('http://127.0.0.1:8000/api/viewPublisher/');
  const data = await response.json();
  publishers.value = data;
}

onMounted(() => {
  getPublishers();
})

</script>

<style scoped>
article {
  width: 100%;
  padding: 1rem;
}
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
