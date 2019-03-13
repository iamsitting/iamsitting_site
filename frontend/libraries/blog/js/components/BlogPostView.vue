<template>
  <div class="container">
    <div class="blog-view">
    <h1>{{blogPost.title}}</h1>
    <h2>{{blogPost.subtitle}}</h2>
    <div class="blog-view__body--container">
      <p class="blog-view__body--font">
        {{blogPost.body}}
      </p>
      <p class="blog-view__author--font">author: {{blogPost.author}}</p>
    </div>
    <br>
  </div>
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
      let blogId = this.$route.params.id;
      if (!blogId) {
        blogId = '1';
      }
      this.$store.dispatch('blogPosts/getBlogPost', blogId)
    }
  }
</script>

<style lang="scss" scoped>
  .blog-view {
    color: black;
    background-color: white;
    border-radius: 10px;

    h1 {
      font-size: 60px;
      font-family: sans-serif;
      padding-top: 5%;
      text-align: center;
    }

    h2 {
      font-size: 20px;
      font-style: italic;
      font-family: serif;
      padding-top: 10px;
      text-align: center;
    }

    &__body{

      &--container {
        text-align: justify;
        padding: 5% 10% 0 10%;
      }

      &--font {
      font-family: 'Times New Roman', Times, serif;
      font-size: 16px;
      }
    }

    &__author--font {
      font-family: 'Times New Roman', Times, serif;
      font-size: 16px;
      font-style: italic;
    }

  }
</style>
