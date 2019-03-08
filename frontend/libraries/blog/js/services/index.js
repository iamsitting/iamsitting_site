import Vue from 'vue'
import Vuex from 'vuex'
import blogPosts from './blogPosts'

Vue.use(vuex)

export default new Vuex.Store({
  modules: {
    blogPosts
  }
})
