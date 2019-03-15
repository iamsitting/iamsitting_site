<template>
  <div class="blog-app">
    <blog-navigation/></blog-navigation>
    <div class="view-container">
      <router-view/>
    </div>
    <blog-footer/></blog-footer>
  </div>
</template>

<script>
  import 'bootstrap'
  import BlogFooter from 'blog/js/components/footer/BlogFooter.vue'
  import BlogNavigation from 'blog/js/components/BlogNavigation.vue'
  export default {
    name: "App",
    components:  {
      BlogFooter,
      BlogNavigation
    }
  }
</script>

<style lang="scss">
  @import "~bootstrap/scss/bootstrap";

  .blog-app {
    background: url(~base_theme/images/bg.jpg) no-repeat center center fixed;
    color: white;
  }
</style>
