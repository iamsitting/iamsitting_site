import React from "react";

export const BlogPostForm = ({...props}) => {
  return (
    <React.Fragment>
      <form onSubmit={props.postPost}>
        <label> Title </label>
        <input type="text" name="title" />
        <label> Subtitle </label>
        <input type="text" name="subtitle" />
        <label> Body </label>
        <textarea name="body"></textarea>
        <label> Category </label>
        <select></select>
        <button type="submmit">Submit</button>
      </form>
    </React.Fragment>
  );
}

