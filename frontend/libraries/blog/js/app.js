import 'bootstrap'
import 'blog/sass/main.scss'
import Vue from 'vue'
import App from './App.vue'

new Vue({
  el: '#app',
  render: h => h(App),
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
  }
})