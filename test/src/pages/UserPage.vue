<template>
  <div>
    <my-dialog v-model:show="dialogVisible">
        <to-do-form
          @create="createToDo"
        />
    </my-dialog>
    <header>
      <my-button
      @click.stop="showDialog"
      >Add ToDo</my-button>
      <p>Hello : <strong>isfjasdfjsjf@fsmdfjas.com</strong></p>
      <my-button
      @click="logout"
      >Logout</my-button>
    </header>
    <to-do-form
        @create="createToDo"
    />
    <to-do-list
        @remove="removePost"
        :toDo="toDo"
        :key="toDo.id"
    />
    <my-button
    @click="fetchToDo"
    >Get posts</my-button>
  </div>
</template>

<script>
import ToDoList from "@/components/ToDoList";
import ToDoForm from "@/components/ToDoForm";
import axios from "axios";
import MyDialog from "@/components/UI/MyDialog";
import MyButton from "@/components/UI/MyButton";
export default {
  components: {
    MyButton,
    MyDialog,
    ToDoList, ToDoForm
  },
  data() {
    return {
      toDo: [],
      dialogVisible: false,
      url: "http://127.0.0.1:8000/api/tasks/",
    }
  },
  mounted() {
    this.getToDo();
    console.log(this.id)
  },
  methods: {
    createToDo(post) {
      console.log(post)
      this.toDo.push(post)
      this.dialogVisible = false;
      axios.post(this.url, post).then((response) => {
        console.log(response)
        this.getToDo();
      })
    },
    removePost(post) {
      this.toDo = this.toDo.filter(p => p.id !== post.id)
      console.log(this.toDo)
    },
    showDialog() {
      this.dialogVisible = true;
    },
    async fetchToDo() {
      try {
         const response = await axios.get(this.url)
        console.log(response)
      } catch (e) {
        alert('Error')
      }
    },
    getToDo() {
      axios.get(this.url).then((response) => {
        console.log(response)
        this.toDo = response.data;
      })
    },
    logout() {
      axios.post("http://127.0.0.1:8000/api-auth/login/", {
        username: 'admin',
        password: 'qwerty40req'
      })
    }
  }
}
</script>

<style scoped>

header {
  display: flex;
  flex-direction: row;
  background: #8dfffd;
  justify-content: space-between;
  padding: 10px 15px;
  border-bottom: 2px solid black;
}


</style>