import Auth from "@/pages/Auth";
import {createRouter, createWebHistory} from "vue-router";
import UserPage from "@/pages/UserPage";
import Register from "@/pages/Register";


const routes = [
    {
        path: '/',
        component: Auth,
    },
    {
        path: '/tasks',
        component: UserPage,
    },
    {
        path: '/register',
        component: Register,
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.HOME)
})

export default router;