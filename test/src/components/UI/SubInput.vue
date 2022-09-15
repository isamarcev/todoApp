<template>
  <input :value="subtitle"
               @input="updateSubInput"
               class="input" type="text" placeholder="Создание подпостаф"/>
        <div style="width: 25%; display: flex;padding:0 30px; flex-direction: row; justify-content: space-between">
          <my-button
          @click:="$emit('createSubTitle', subtitle)"
          >Save</my-button>
          <my-button>Cancel</my-button>
        </div>
</template>

<script>
export default {
  name: 'my-sub-input',
  props: {
    subtitle: [String, Number]
  },
  methods: {
    updateSubInput(event) {
      this.subtitle = event.target.value
       // = event.target.value
    },
    gettter() {
      const post = this.subtitle
      return post
    }
  }
}
</script>

<style scoped>
.input {
  border: 1px solid teal;
  padding: 10px 15px;
  font-size: 15px;
  border-radius: 5px;
}

.input:focus {
  border: 1px solid teal;
}
</style>