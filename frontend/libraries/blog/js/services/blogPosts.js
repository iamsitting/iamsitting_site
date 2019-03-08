import blogService from './blogService'

const state = {
  blogPosts: []
}

const getters = {
  blogPosts: state => {
    return state.blogPosts
  }
}

const actions = {
  getBlogPosts({commit}) {
    blogService.getPosts()
      .then(posts => {
       commit('setBlogPosts', posts) 
      })
  }
}

const mutations = {
  setBlogPosts(state, posts) {
    state.blogPosts = posts
  },
  addBlogPost(state, post) {
    state.blogPosts.push(post)
  }
  deleteBlogPost(state, id) {
    state.BlogPosts = state.posts.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}