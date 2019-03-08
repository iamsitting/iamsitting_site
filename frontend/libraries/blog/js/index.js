import 'bootstrap'
import 'blog/sass/main.scss'
import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#blog-app')
