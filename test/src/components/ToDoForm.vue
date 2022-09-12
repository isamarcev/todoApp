<template>
    <form @submit.prevent id="add-form">
      <h3>new TODO</h3>
      <div class="add-form">
        <my-input
               v-model="post.title"
               type="text"
               placeholder="Создание поста"
        />
        <my-button
        @click="createToDo"
        >Save</my-button>
        <my-button>Cancel</my-button>
      </div>
    </form>
</template>

<script>
export default {
  data() {
    return {
      post: {
      title: '',
        color: 'orange',
        user: 1,
    }
    }
  },
  methods: {
    createToDo() {
      // this.post.id = Date.now();
      this.$emit('create', this.post)
      this.post = {
        title: '',
        color: '',
        user: this.post.user.id
      }
    }
  }
}
</script>

<style scoped>

.add-form {
  border: 2px solid grey;
  background: #cfcfcf;
  height: 50px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.post {
  /*border: 2px solid grey;*/
  /*height: 50px;*/
  /*display: flex;*/
  /*flex-wrap: wrap;*/
  /*flex-direction: row;*/
  /*justify-content: flex-end;*/
  /*align-items: center;*/
}
</style>