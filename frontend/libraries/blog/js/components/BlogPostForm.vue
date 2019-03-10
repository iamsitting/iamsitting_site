<template>
  <div>
    <p>Title</p>
    <input type="text" placeholder="Hello" v-model="title">
    <p>Subtitle</p>
    <input type="text" placeholder="From the other side" v-model="subtitle">
    <p>Body</p>
    <input type="text" placeholder="From the other side" v-model="body">
    <p>Category</p>
    <input type="text" placeholder="From the other side" v-model="category">
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
        category: 0,
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