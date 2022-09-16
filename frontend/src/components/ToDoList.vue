<template>
  <div>
    <h3>added TODO</h3>
    <to-do-item
      v-for="post in toDo"
      :post="post"
      :key="post.id"
      @remove="$emit('remove', post)"
    />
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

<style scoped>


</style>