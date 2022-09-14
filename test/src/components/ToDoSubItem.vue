<template>
  <div v-for="su in subs" v-if="su">
  <div class="sub">
    <div class="sub-title">{{su.title}}
    </div>
      <my-button
      @click="$emit('removeSub', sub)"
      >Remove</my-button>
  </div>
              </div>

</template>

<script>
export default {
  props: {
    subs: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>

.sub {
  display: flex;
  width: 100%;
  padding: 10px 30px;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  font-size: 20px;
}

.sub button {
  background: red;
}
</style>