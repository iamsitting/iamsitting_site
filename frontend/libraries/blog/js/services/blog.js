import blogService from './blogService'

const state = {
  blogs: []
}

const getters = {
  blogs: state => {
    return state.blogs 
  }
}

const actions = {
  getBlogPosts({commit}) {
    blogService.getPosts()
      .then(posts => {
       commit('setPosts', posts) 
      })
  }
}
