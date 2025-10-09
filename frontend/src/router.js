import { createMemoryHistory, createRouter } from "vue-router";

import Authors from "./components/authors.vue";
import Books from "./components/books.vue";
import Publishers from "./components/publishers.vue";
import BookDetail from "./components/BookDetail.vue"

const routes = [
    {path: "/"},
    {path: "/authors", component: Authors},
    {path: "/publishers", component: Publishers},
    {path: "/books", component: Books},
    {path: "/books/:id/", name: 'BookDetails', component: BookDetail}
]

const router = createRouter({
    history: createMemoryHistory(),
    routes,
})

export default router