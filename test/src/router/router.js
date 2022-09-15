import Auth from "@/pages/Auth";
import {createRouter, createWebHistory} from "vue-router";
import UserPage from "@/pages/UserPage";
import Register from "@/pages/Register";


const routes = [
    {
        path: '/',
        component: UserPage,
    },
    {
        path: "/auth",
        component: Auth,
    },
    {
        path: "/register",
        component: Register,
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.HOME)
})

export default router;