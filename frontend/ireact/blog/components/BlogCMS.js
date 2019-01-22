import React from "react";
import {BlogPostFormContainer} from "../containers/BlogPostFormContainer";

export const BlogCMS = ({...props}) => {
  return (
    <div className="blog-cms">
      <BlogPostFormContainer />
    </div>
  );
}
