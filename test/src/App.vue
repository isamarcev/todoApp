<template>
  <div id="app">
      <router-view></router-view>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    console.log(token)
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common["Authorization"] = ''
    }
  }
}
</script>

<style >
#app {
  margin:0;
  padding: 0;
}

body {
  margin: 0!important;
  padding: 0!important;
  box-sizing: border-box!important;
  background: #eef5eb;
}
</style>