import { createStore } from "vuex";

export default createStore({
    state: {
        token: '',
        isAuthenticated: false,
        email: ''

    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
        },
        removeToken(state) {
            state.token = ''
            state.isAuthenticated = false
        },
        setEmail(state, email) {
            state.email = email
        }
    },
    actions: {

    },
    modules: {

    }
})