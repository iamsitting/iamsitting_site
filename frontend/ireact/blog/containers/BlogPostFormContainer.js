import BlogPostForm from "../components/BlogPostForm"
import { connect } from "react-redux"

const mapStateToProps = state => {
  return {
    'data': state.data,
  };
}

const mapDispatchToProps = dispath => {
  return;
}

export const BlogPostFormContainer = connect(mapStateToProps, mapDispatchToProps)(BlogPostForm)