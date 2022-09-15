<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'my-button'
}
</script>

<style scoped>
.btn {
  /*align-self: flex-end;*/
  padding: 10px 15px;
  background: seagreen;
  color: white;
  border: 2px solid teal;
  border-radius: 4px;
  transition: 0.5s;

}
.btn:hover{
  background: #b3e7f1;
  color: black;
  cursor: pointer;
}

</style>