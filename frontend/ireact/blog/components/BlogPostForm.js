import React from "react";

const BlogPostForm = ({...props}) => {
  <React.Fragment>
    <form>
      <label> Title </label>
      <input type="text" name="title" />
      <button type="submmit">Submit</button>
    </form>
  </React.Fragment>
}

export default BlogPostForm
