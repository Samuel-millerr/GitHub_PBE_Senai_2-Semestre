<template>
  <div>
    <h1>Lista de Livros</h1>
    <ul>
      <li v-for="publisher in publishers" :key="publishers.id">
        {{publisher.nome }} - {{publisher.cnpj}}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const publishers = ref([])

async function getPublishers() {
  const response = await fetch('http://127.0.0.1:8000/api/viewPublisher/')
  const data = await response.json()
  publishers.value = data
}

onMounted(() => {
  getPublishers()
})

defineExpose({
  publishers
})
</script>
