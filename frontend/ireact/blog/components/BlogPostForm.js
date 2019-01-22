import React from "react";

export const BlogPostForm = ({...props}) => {
  return (
    <React.Fragment>
      <form>
        <label> Title </label>
        <input type="text" name="title" />
        <button type="submmit">Submit</button>
      </form>
    </React.Fragment>
  );
}

