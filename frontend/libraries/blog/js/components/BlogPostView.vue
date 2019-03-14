<template>
  <div class="container">
    <div class="blog-view">
    <h1 class="blog-view__title--font">{{blogPost.title}}</h1>
    <h2 class="blog-view__subtitle--font">{{blogPost.subtitle}}</h2>
    <div class="blog-view__body--container">
      <p class="blog-view__body--font">
        {{blogPost.body}}
      </p>
      <p v-if="blogPost.author">author: <span class="blog-view__author--font">@{{blogPost.author.username}}</span></p>
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

    @at-root #{&}__title--font {
      font-size: 60px;
      font-family: sans-serif;
      padding-top: 5%;
      text-align: center;
    }

    @at-root #{&}__subtitle--font {
      font-size: 20px;
      font-style: italic;
      font-family: serif;
      padding-top: 10px;
      text-align: center;
    }

    @at-root #{&}__body{

      @at-root #{&}--container {
        text-align: justify;
        padding: 5% 10% 0 10%;
      }

      @at-root #{&}--font {
      font-family: 'Times New Roman', Times, serif;
      font-size: 16px;
      }
    }

    @at-root #{&}__author--font {
      font-family: 'Times New Roman', Times, serif;
      font-size: 16px;
      font-style: italic;
    }

  }
</style>
