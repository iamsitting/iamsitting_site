<template>
  <div class="more-info">
    <p>{{content}}</p>
  </div>
</template>

<script>
  export default {
    name: 'MoreInfoPanel',
    props: [
      'content'
    ]
  }
</script>

<style lang="scss" scoped>
  .more-info {
    //padding: 10% 0 5% 25%;
    margin-top: 12%;
    padding-top: 5%;
    text-align: center;
    border: 1px solid white;
  }
</style>
