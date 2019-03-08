import blogService from 'blog/js/services/blogService'

const state = {
  blogPosts: []
}

const getters = {
  blogPosts: state => {
    return state.blogPosts
  }
}

const actions = {
  getBlogPosts({ commit }) {
    blogService.getPosts()
      .then(posts => {
       commit('setBlogPosts', posts)
      })
  },
  addBlogPost({ commit }, post) {
    blogService.createPost(post)
      .then(() => {
        commit('addBlogPost', post)
      })
  },
  deleteBlogPost({ commit }, id) {
    blogService.deletePost(id)
    commit('deleteBlogPost', id)
  }
}

const mutations = {
  setBlogPosts(state, posts) {
    state.blogPosts = posts
  },
  addBlogPost(state, post) {
    state.blogPosts.push(post)
  },
  deleteBlogPost(state, id) {
    state.blogPosts = state.blogPosts.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}