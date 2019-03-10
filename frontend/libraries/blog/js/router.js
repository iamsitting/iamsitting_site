import Vue from 'vue'
import Router from 'vue-router'
import BlogHome from './components/BlogHome.vue'
import BlogPostForm from './components/BlogPostForm.vue'
import BlogPostView from './components/BlogPostView.vue'
import BlogAdmin from './components/BlogAdmin.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: BlogHome
    },
    {
      path: 'view',
      name: 'view',
      component: BlogPostView
    },
    {
      path: 'blog-post',
      name: 'blog-post',
      component: BlogAdmin
    }
  ]
})
