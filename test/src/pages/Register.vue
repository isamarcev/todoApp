<template>
  <div>
    <div class="auth">
      <div class="auth__content">
          <h1 style="text-align: center; margin-bottom: 40px">Registration Page</h1>
        <div class="error">
          <h2 style="color: darkred; text-align: center">Error text...</h2>
        </div>
        <form @submit.prevent="register">
        <div class="row">
          <my-input
              v-model="email"
              id="email"
              class="auth-input"
          placeholder="Login(Email)"
          />
          <my-input
          class="auth-input"
          v-model="password"
          type="password"
          id="password"
          placeholder="Password"
          />
          <my-input
          class="auth-input"
          v-model="repeatPassword"
          type="password"
          id="repeatPassword"
          placeholder="Repeat Password"
          />
        </div>
    <div class="row">
      <my-button
        style="width: 200px"
        type="submit"
        @click="login"
        >Enter</my-button>
      </div>
        </form>
        <div class="row" style="margin-top: 20px">
              <span>Уже зарегестрированы? <a @click.prevent="gotosignin" href="">Войти </a></span>
      </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";
import router from "@/router/router";
export default {
  data () {
    return {
      email: "",
      password: "",
      repeatPassword: "",
      url: 'http://127.0.0.1:8000/api/v1/users/'
    }
  },
  beforeCreate () {
    if (this.$store.state.isAuthenticated === true) {
      this.$router.push('/')
    }
  },
  components: {},
  methods: {
    register() {
      axios.post(this.url,
          {headers: {'Content-type': 'application/json'},'email': this.email, 'password': this.password}).
      then(response => {
        console.log(response); router.push('/auth')}).catch(err => { console.error(err)})
    },
    gotosignin () {
      this.$router.push('/auth')
    }
    // setLogined(token) {
    //   console.log(token)
    // }
  }

}
</script>

<style scoped>
.auth {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.2);
  position: fixed;
  display: flex;
}
.auth__content {
  margin: auto;
  background: #f1e6ed;
  border-radius: 12px;
  min-height: 400px;
  min-width: 300px;
  padding: 50px;

}

.auth-input {
  width: 80%;
  margin: 20px auto;
  background: #bfb5bb;
  text-align: center;
  border: 2px solid #000817;
  font-weight: bold;
  border-radius: 7px;
}

.auth-input:focus {
  background: white;
}
.row {
  text-align: center;
}

</style>