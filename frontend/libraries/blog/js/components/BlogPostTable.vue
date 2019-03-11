<template>
  <div>
    <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Category</th>
            <th>Author</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="post in blogPosts">
            <td>{{post.title}}</td>
            <td>{{post.category}}</td>
            <td>{{post.author}}</td>
            <td>{{post.id}}</td>
          </tr>
        </tbody>
      </table>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    name: 'BlogPostTable',
    data() {
      return {
        title: "",
        category: "",
        author: "",
        id: 0,
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