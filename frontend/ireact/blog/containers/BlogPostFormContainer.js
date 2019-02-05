import { BlogPostForm } from "../components/BlogPostForm"
import { connect } from "react-redux"

const mapStateToProps = state => {
  return {
    'data': 'foo',
  };
}

const mapDispatchToProps = dispath => {
  return {
    doSomething: () => {},
  };
}

export const BlogPostFormContainer = connect(mapStateToProps, mapDispatchToProps)(BlogPostForm)