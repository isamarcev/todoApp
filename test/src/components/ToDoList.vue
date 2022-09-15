<template>
  <div class="todo-list">
    <h3 >added TODO</h3>
    <to-do-item
      v-for="post in toDo"
      :post="post"
      :key="post.id"
      @remove="$emit('remove', post)"
    >
    <slot></slot>
    </to-do-item>
  </div>
</template>

<script>
import ToDoItem from "@/components/ToDoItem";
export default {
  components: {ToDoItem},
  props: {
    toDo: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style>
.todo-list {
  width: 80%;
  margin: 30px auto!important;
}

.todo-list h3 {
  font-size: 35px;
}

</style>