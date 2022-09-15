<template>
  <div class="task">
        <div class="main-task"
             v-bind:style="{ backgroundColor: post.color }">
          <div class="plus"
          ></div>
          <div><strong>{{ post.title }}</strong></div>
          <my-button
          @click="$emit('remove', post)"
          >Remove</my-button>
        </div>

          <slot></slot>
        </div>

</template>

<script>
import ToDoSubItem from "@/components/ToDoSubItem";
import axios from "axios";
export default {
  components: {
    ToDoSubItem
  },
  props: {
    post: {
      type: Object,
      required: true,
    }
  },
  methods: {
    removeSub(id) {
      console.log(this.post)
      // this.post
      // id = 0
        axios.delete(`http://127.0.0.1:8000/api/subtasks/${id}/`).then((responce) => {
        console.log(responce);
        //
        });
        // this.$forceUpdate();
    },
  buildForm(id) {
      const x = id
    console.log(x)
  }
  }

}
</script>

<style scoped>

.plus {
  display:inline-block;
  margin-left: 10px;
  width:70px;
  height:70px;
  background:
    linear-gradient(#4771cf,#4771cf),
    linear-gradient(#4771cf,#4771cf);
  background-position:center;
  background-size: 50% 5px,5px 50%; /*thickness = 2px, length = 50% (25px)*/
  background-repeat:no-repeat;
  transition: 1s;
        border-radius: 40px;


}

.plus:hover {
  cursor: pointer;
  outline: 3px solid blue;
  transition: 1s;
  border-radius: 40px;



}

.main-task {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  height: 80px;
  border-radius: 10px;
  /*background-color: #42b983;*/
  padding-right: 30px;
  border: 2px solid grey;
  align-items: center;
  font-size: 20px;
  margin: 25px;
}
.main-task button {
  align-self: center;
  background: red;
}

.task {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-end;
  height: auto;

  /*width: 100%;*/
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

.add-form-sub {
  border: 2px solid grey;
  background: #c4f5e3;
  height: 80px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  text-align: center;
  width: 100%;
  margin: 0 10%;
  padding-left: 30px;
}



.sub button {
  background: red;
}
</style>