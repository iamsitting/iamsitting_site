export const BlogPost = {
  getPosts: () => {
    return $.ajax({
      method: "GET",
      url: "api/posts/"
    });
  },
  getPost: (id) => {
    return $.ajax({
      method: "GET",
      url: "api/posts/" + id
    });
  },
  createPost: () => {
    return $.ajax({
      method: "POST",
      url: "api/posts/"
    });
  },
  updatePost: (id) => {
    return $.ajax({
      method: "PUT",
      url: "api/posts/" + id
    });
  },
  deletePost: (id) => {
    return $.ajax({
      method: "DELETE",
      url: "api/posts/" + id
    });
  }

}