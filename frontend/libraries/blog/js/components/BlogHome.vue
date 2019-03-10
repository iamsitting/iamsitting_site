<template>
  <div class="hello">
    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Category</th>
          <th>Author</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in blogPosts">
          <td>{{post.title}}</td>
          <td>{{post.category}}</td>
          <td>{{post.author}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    name: 'BlogHome',
    data() {
      return {
        title: "",
        category: "",
        author: "",
      };
    },
    computed: mapState({
      blogPosts: state => state.blogPosts.blogPosts
    }),
    methods: mapActions('blogPosts', [
      'addBlogPost',
      'deleteBlogPost'
    ]),
    created() {
      this.$store.dispatch('blogPosts/getBlogPosts')
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
table {
  color: white;
}
</style>
