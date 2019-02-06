// Blog Post
export const RESET_POST_FORM = 'RESET_POST_FORM'
export const resetPostForm = () => {
  return {
    type: RESET_POST_FORM
  };
}

export const postPost = (values) => {
  let blogPost = {
    "title": values.title,
    "subtitle": values.subtitle,
    "body": values.body,
    "category": values.category
  }
  return function(dispatch) {
    let data = null;
    data = JSON.stringify(blogPost);

    return $.ajax({
      url: 'api/blog-post',
      type: 'POST',
      contentType: 'application/json',
      data: data,
      success: function(data, status, jqHXR) {
        dispatch(resetPostForm);
      }
    });
  }
}
