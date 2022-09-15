<template>
    <form @submit.prevent id="add-form" >
      <h3 style="width: 80%; margin: 20px auto; font-size: 25px">new TODO</h3>
      <div class="add-form">
        <my-input
               style="width: 40%; font-size: 15px"
               v-model="post.title"
               type="text"
               placeholder="Создание поста"
        />
        <div class="color">
          <div class="choose-color blue"
          @click="this.post.color='#9fc5f8'"
          ></div>
          <div class="choose-color green"
               @click="this.post.color='#93c47d'"
          >
          </div>
          <div class="choose-color sand"
               @click="this.post.color='#f9cb9c'"
          ></div>

        </div>
        <div class="buttons">
        <my-button
        @click="createToDo"
        >Save</my-button>
        <my-button>Cancel</my-button>
        </div>
      </div>
    </form>
</template>

<script>
export default {
  data() {
    return {
      post: {
        title: '',
        color: null,
        // sub: [],
        // user: this.
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
        // user: this.post.user.id
      }
    },
  }
}
</script>

<style scoped>

.add-form {
  border: 2px solid grey;
  background: #c4f5e3;
  height: 80px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  text-align: center;
  width: 80%;
  margin: 25px auto;
  padding-left: 30px;

}

h3 {
  width: 80%;
}

.buttons {
  width: 150px;
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
}

#add-form {
  width: 80%;
  margin: 0 auto;



}

.color {
  display: flex;
  flex-direction: row;
  width: 20%;
  justify-content: space-between;
}

.choose-color {
  width: 50px;
  height: 50px;
  border-radius: 25px;
  transition: .5s;
}
.choose-color:hover {
  cursor: pointer;
  box-shadow: 0 0 2px 2px #7a7d6c;
  transition: 0.5s;

}

.blue {
  background: #9fc5f8;
}
.green {
  background: #93c47d;
}
.sand {
  background: #f9cb9c;
}

/*">#9fc5f8</div>*/
/*          <div class="choose-color green">#93c47d</div>*/
/*          <div class="choose-color sand">#f9cb9c</div>*/

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