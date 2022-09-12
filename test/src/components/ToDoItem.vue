<template>
  <div class="task">
        <div class="main-task" v-bind:style="{ backgroundColor: post.color }">
          <div class="plus"></div>
          <div><strong>{{ post.title }} {{ post.color }}</strong></div>
          <my-button
          @click="$emit('remove', post)"
          >Remove</my-button>
        </div>
        <div class="subtask" v-if="post.subtask">
          <div style="width: 400px; background-color: aqua" >fasdf
          <my-button>Remove</my-button>
          </div>
        </div>
        <div class="add-form">
        <my-input class="input" type="text" placeholder="Создание подпостаф"/>
        <my-button>Save</my-button>
        <my-button>Cancel</my-button>
      </div>
      </div>
</template>

<script>
export default {
  props: {
    post: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style scoped>

.plus {
  display:inline-block;
  width:50px;
  height:50px;
  background:
    linear-gradient(#4771cf,#4771cf),
    linear-gradient(#4771cf,#4771cf);
  background-position:center;
  background-size: 50% 5px,5px 50%; /*thickness = 2px, length = 50% (25px)*/
  background-repeat:no-repeat;
}

.main-task {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 95%;
  /*background-color: #42b983;*/
  border: 2px solid grey;
}

.task {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-end;
  height: auto;

  /*width: 100%;*/
}

.subtask {
  display: flex;
  flex-direction: row;
  width: 90%;
  height: 50px;
  background-color: grey;
}
</style>