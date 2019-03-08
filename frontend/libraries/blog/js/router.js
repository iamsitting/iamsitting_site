import Vue from 'vue'
import Router from 'vue-router'
import BlogHome from './components/BlogHome.vue'
import BlogPosts from './components/BlogPosts.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: BlogHome
    },
    {
      path: '/blog-posts',
      name: 'blog-posts',
      component: BlogPosts
    }
  ]
})
