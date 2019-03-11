<template>
  <div>
    <p>Title</p>
    <input type="text" placeholder="Topic" v-model="title">
    <p>Subtitle</p>
    <input type="text" placeholder="Part 1" v-model="subtitle">
    <p>Body</p>
    <input type="text" placeholder="Lorem impsum..." v-model="body">
    <p>Category</p>
    <input type="text" placeholder="General" v-model="category">
    <br><br>
    <input
      type="submit"
      value="Add"
      @click="addBlogPost({ title: title, body: body, subtitle: subtitle, category: category, author:2 })"
      :disabled="!title || !body">
  </div>
</template>
<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    name: 'BlogPostForm',
    data() {
      return {
        title: "",
        subtitle: "",
        body: "",
        category: "",
        author: 0
      };
    },
    computed: mapState({
      blogPosts: state => state.blogPosts.blogPosts
    }),
    methods: mapActions('blogPosts', [
      'addBlogPost',
    ])
  }
</script>