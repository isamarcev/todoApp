import { createApp } from "vue";
import App from './App'
import components from "@/components/UI";
import router from "@/router/router";
import store from "@/store";
import axios from "axios";

const app = createApp(App)

axios.defaults.baseURL = "http://127.0.0.1:8000"

components.forEach(component => {
    app.component(component.name, component)
})

app
    .use(router)
    .use(store)
    .mount("#app");
