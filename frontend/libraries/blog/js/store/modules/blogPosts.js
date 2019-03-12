import blogService from 'blog/js/services/blogService'

const state = {
  blogPosts: [],
  blogPost: {}
}

const getters = {
  blogPosts: state => {
    return state.blogPosts
  },
  blogPost: state => {
    return state.blogPost
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
  },
  getBlogPost({ commit }, id) {
    blogService.getPost(id)
      .then(post => {
        commit('setBlogPost', post)
      })
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
  },
  setBlogPost(state, post) {
    state.blogPost = post
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}