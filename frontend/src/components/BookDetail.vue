<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const book = ref({})

async function getBook(id) {
  const response = await fetch(`http://127.0.0.1:8000/api/viewBook/${id}`)
  const data = await response.json()
  book.value = data
  console.log(book)
}

onMounted(() => {
  getBook(route.params.id)
})
</script>

<template>
    <section id="book-detail-container">
        <div id="buttons-conteiner">
            <router-link to="/" id="button-back"> Voltar </router-link>
        </div>
        <article id="info">
            <aside id="cover">
                <img :src="book.capa" class="book-cover" alt="Capa do livro"></img>
            </aside>
            <section id="main-info">
                <header id="header-info">
                    <h2> {{ book.titulo }} </h2>
                    <h3> {{ book.subtitulo }}</h3>
                    <div id="book-chips">
                        <p> {{ book.idioma }} </p>
                        <p> {{ book.ano_publicacao }} </p>
                    </div>
                </header>
                <article id="description-info">
                    <h3> Descrição </h3>
                    <p> {{  book.descricao }} </p>
                </article>
                <div id="details-info">
                    <div>
                        <p> Dimensões: {{ book.dimensoes }}</p>
                        <p> Peso: {{ book.peso  }}</p>
                        <p> Disponível: {{ book.disponivel ? 'Sim': 'Não' }} </p>
                    </div>
                    <div>
                        <p id="price-info"> Preço: R$ {{ book.preco }}</p>
                    </div>
                </div>
            </section>
        </article>
    </section>
</template>

<style scoped>
#book-detail-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 87vh;
    padding: 5rem;
    background-color: #f9f7f4
}

#buttons-conteiner {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 50%;
    padding: 1rem 0 1rem 0;
}

#button-back {
    padding: 0.5rem 1rem 0.5rem 1rem;
    color: white;
    background-color: #2c3e50;
    font-size: 18px;
    border: none;
    box-shadow: 0 0 2px 1px #333;
    text-decoration: none;
    transition: all ease 2s;
}

#button-back:hover {
    background-color: #436e99;
}

#info {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-evenly;
    width: 50%;
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 0.25rem;
    gap: 0.5rem;
    box-shadow: 0 0 2px 1px #33333393;
}

#cover {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 16rem;
    height: 95%;
    border-radius: 0.25rem;
    box-shadow: 0 0 3px 1px #333;
}

.book-cover {
    border-radius: 0.25rem;
    width: 100%;
    height: 100%;
    max-width: 100%;
    max-height: 100%;
}

#main-info {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    width: 50%;
}

#header-info {
    display: flex;
    flex-direction: column;
    padding: 0.75rem;
    gap: 0.35rem;
    color: #333;
}
    
#book-chips {
    display: flex;
    gap: 0.5rem;
}

#book-chips > * {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0.45rem 0.6rem 0.45rem 0.6rem;
    border-radius: 0.5rem;
    background-color: #fbf8f5;
    border: 1px solid #efe8df;
    font-size: 16px;
}

#description-info {
    margin: 0.2rem;
    padding: 1rem;
    border-radius: 0.5rem;
    background-color: #fbf8f5;
}

#description-info p {
    font-size: 18px;
}

#details-info {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 17px;
    font-weight: 700;
    color: #333;
}

#price-info {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 85%;
    font-weight: 600;
    color: white;
    font-size: 18px;
    padding: 0.75rem 1rem 0.75rem 1rem;
    border-radius: 0.5rem;
    background-color: #2c3e50;
    cursor: default;
}
</style>