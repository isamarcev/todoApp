<template>
  <div v-if="renderComponent">
    <my-dialog
    style="display: none">
        <to-do-form
          @create="createToDo"
        />
    </my-dialog>
    <header>
      <my-button
      @click="formVisible"
      >Add ToDo</my-button>
      <p>Hello : <strong>{{ this.$store.state.email }}</strong></p>
      <my-button
      @click="logout"
      >Logout</my-button>
    </header>
    <to-do-form
        id="todoform"
        v-if="formToDo"
        style="display: block"
        @create="createToDo"
    />
    <div class="todo-list">
    <h3>added TODO</h3>
    <to-do-item
      v-for="post in toDo"
      :post="post"
      :key="post.id"
      @remove="removePost"
    >
     <div class="subtasks-list" v-if="post.sub" v-for="sub in post.sub">
          <div class="sub">
            <div class="sub-title">{{sub.title}}</div>
                <my-button
                :key="sub.id"
                @click="removeSub()"
                >Remove</my-button>
            </div>
        </div>
    </to-do-item>
  </div>
  </div>
</template>

<script>
import ToDoList from "@/components/ToDoList";
import ToDoForm from "@/components/ToDoForm";
import axios from "axios";
import MyDialog from "@/components/UI/MyDialog";
import MyButton from "@/components/UI/MyButton";
import ToDoItem from "@/components/ToDoItem";
import ToDoSubItem from "@/components/ToDoSubItem";
export default {
  components: {
    MyButton,
    MyDialog,
    ToDoList, ToDoForm, ToDoItem, ToDoSubItem
  },
  data() {
    return {
      toDo: [],
      dialogVisible: false,
      urlCreateTask: "http://127.0.0.1:8000/api/create-task/",
      url: "http://127.0.0.1:8000/api/tasks/",
      renderComponent: true,
      formToDo: false,
      subtitle: ""
    }
  },
  mounted() {
    this.getToDo();
    if (this.$store.state.isAuthenticated === false) {
      this.$router.push('/auth')
    }
    // console.log(this.id)
  },
  methods: {
    createToDo(post) {
      console.log(post)
      // this.toDo.push(post)
      this.dialogVisible = false;
      axios.post(this.urlCreateTask, post).then((response) => {
        console.log(response)
        if (response.statusText === 'Created') {
          this.getToDo()
        }
    })},
    removePost(post) {
      axios.delete(`http://127.0.0.1:8000/api/tasks/${post.id}/`).then((response) => {
        console.log(response.data)

      })
      this.toDo = this.toDo.filter(p => p.id !== post.id)
    },

    removeSub(sub) {
      console.log(sub)
      axios.delete(`http://127.0.0.1:8000/api/subtasks/${sub}/`).then((responce) => {
        console.log(responce)
        this.getToDo()
        this.forceRerender()
      })
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
        if (response.status === "401" ) {
          this.$router.push('/auth')
        }
        console.log(response)
        this.toDo = response.data;
      })
    },
    logout() {

      axios.post("http://127.0.0.1:8000/api/v1/token/logout/").then((response => {
        console.log(response);
          }
        ));
      localStorage.removeItem('token')
      delete axios.defaults.headers.common['Authorization']
      this.$store.state.isAuthenticated = false
      this.$store.state.email = ''
      this.$router.push('/auth')


    },
    forceRerender() {
        this.renderComponent = false;
        this.$nextTick(() => {
          this.renderComponent = true;
        });
  },
  formVisible() {
    // console.log(this)
    if (this.formToDo) {
      this.formToDo = false
    } else {
      this.formToDo = true
    }
    },
    updateSubInput(event) {
      this.subtitle = event.target.value

    },
    createSubTitle(i) {
      console.log(i)
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
body {
  margin:0;
  padding: 0;
  box-sizing: border-box!important;

}

.sub {
  display: flex;
  width: 100%;
  padding: 10px 30px;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  font-size: 20px;
}

.subtasks-list {
  display: flex;
  flex-direction: row;
  background: #d3d7bd;
  justify-content: space-between;
  width: 80%;
  height: 70px;
  border-radius: 20px;
  border: 2px solid grey;
  /*background-color: grey;*/
  margin: 20px 0;
  align-items: center;
}

* {
  margin:0;
  padding: 0;
}

.sub {
  display: flex;
  width: 100%;
  padding: 10px 30px;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  font-size: 20px;
}

.add-form-sub {
  border: 2px solid grey;
  background: #c4f5e3;
  height: 80px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border-radius: 25px;
  text-align: center;
  width: 100%;
  margin: 0 10%;
  padding-left: 30px;
}

</style>