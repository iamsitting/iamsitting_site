<template>
  <div class="blog-view">
    <h1>{{blogPost.title}}</h1>
    <h2>{{blogPost.subtitle}}</h2>
    <p>{{blogPost.body}}</p>
    <p>-{{blogPost.author}}</p>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    name: 'BlogPostView',
    data() {
      return {
        title: "",
        category: "",
        author: "",
        id: 0,
      };
    },
    computed: mapState({
      blogPost: state => {
        return state.blogPosts.blogPost
      }
    }),
    created() {
      this.$store.dispatch('blogPosts/getBlogPost', this.$route.params.id)
    }
  }
</script>

<style scoped>
  .blog-view {
    color: white;
  }
</style>
