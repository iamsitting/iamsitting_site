import 'bootstrap'
import 'blog/sass/main.scss'
import Vue from 'vue'
import App from './App.vue'
import Home from './components/Home.vue'

new Vue({
  el: '#app',
  template: '<App/>',
  components: {App},
  data: {
    posts: [],
    loading: false,
    currentPost: {},
  },
  mounted: function() {
    this.getPosts();
  },
  methods: {
    getPosts: function() {
      this.loading = true;
      this.$http.get("api/posts/")
        .then((response) => {
          this.posts = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    getPost: function(id) {
      this.loading = true;
      this.$http.get("api/post/${id}")
        .then((response) => {
          this.currentPost = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    createPost: function() {
      this.loading = true;
      this.$http.post("api/posts/")
        .then((response) => {
          this.loading = false;
          this.getPosts();
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    updatePost: function() {
      this.loading = true;
      this.$http.put("api/post/${this.currentPost.id}", this.currentPost)
        .then((response) => {
          this.loading = false;
          this.currentPost = response.data;
          this.getPosts();
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    deletePost: function(id) {
      this.loading = true;
      this.$http.delete("api/post/${id}")
        .then((response) => {
          this.loading = false;
          this.getPosts();
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    }
  }
})