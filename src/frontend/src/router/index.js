import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: () => import('../views/Home.vue')
        },
        {
            path: '/book/:id',
            name: 'Book',
            component: () => import('../views/Book.vue')
        },
        {
            path: '/search',
            name: 'Search',
            component: () => import('../views/Search.vue')
        },
        {
            path:'/autocomplete',
            name: 'Autocomplete',
            component: () => import('../views/Autocomplete.vue')
        }
    ]
})

export default router