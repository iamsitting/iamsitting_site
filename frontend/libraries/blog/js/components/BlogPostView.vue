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
        console.log(this);
        return state.blogPosts.blogPosts.filter(obj => obj.id !== 1)[0]
      }
    }),
    created() {
      console.log(this.$route.params.id);
      this.$store.dispatch('blogPosts/getBlogPosts')
    }
  }
</script>

<style scoped>
  .blog-view {
    color: white;
  }
</style>
