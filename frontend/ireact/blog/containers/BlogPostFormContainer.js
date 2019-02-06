import { BlogPostForm } from "../components/BlogPostForm"
import { connect } from "react-redux"
import { postPost } from '../utils/actions'

const mapStateToProps = (state) => {
  return {
    postForm: {
      title: state.postForm.title,
      subtitle: state.postForm.subtitle,
      body: state.postForm.body,
      category: state.postForm.category
    }
  };
}

const mapDispatchToProps = (dispath) => {
  return {
    postPost: (values) => { dispatch(postPost(values)) },
  };
}

export const BlogPostFormContainer = connect(mapStateToProps, mapDispatchToProps)(BlogPostForm)