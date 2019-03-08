import api from './api'

export default {
  getPosts() {
    return api.get("posts/")
      .then(response => response.data)
      .catch(err => console.log(err))
  },
  getPost(id) {
    return api.get("post/${id}")
      .then(response => response.data)
      .catch(err => console.log(err))
  },
  createPost(payload) {
    return api.post("posts/", payload)
      .then(response => response.data)
      .catch(err => console.log(err))
  },
  updatePost(id, payload) {
    return api.put("post/${id}", payload)
      .then(response => response.data)
      .catch(err => console.log(err))
  },
  deletePost(id) {
    return api.delete("post/${id}")
      .then(response => response.data)
      .catch(err => console.log(err))
  }
}
