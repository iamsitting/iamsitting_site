<template>
  <div class="container">
    <div class="row">
      <h1> List of Posts
      <button class="btn btn-success">Add Post</button>
      </h1> 
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Title</th>
            <th scope="col">Author</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="p in posts">
            <th scope="row">${p.id}</th>
            <th scope="row">${p.title}</th>
            <th scope="row">${p.author}</th>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'

  export default {
    name: "BlogPosts",
    data() {
      return {
        title: "",
      };
    },
    computed: mapState({
      blogPosts: state => state.blogPosts.posts
    }),
    methods: mapActions('blogPosts', [
      'addBlogPost',
      'deleteBlogPost'
    ]),
    created() {
      this.$store.dispatch('blogPosts/getBlogPosts')
    }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
  max-width: 65%;
}
.msg {
  margin: 0 auto;
  max-width: 30%;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}
.msg-index {
  color: #ccc;
  font-size: 0.8rem;
  /* margin-bottom: 0; */
}
img {
  width: 250px;
  padding-top: 50px;
  padding-bottom: 50px;
}
</style>
