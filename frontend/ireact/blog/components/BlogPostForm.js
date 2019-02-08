import React from "react";
import Form from 'react-formal'
import * as yup from 'yup';

let modelSchema = (props) => {
  return yup.object({
    title: yup.string().required(),
    subtitle: yup.string().required(),
    body: yup.string().required(),
    category: yup.string().required(),
  });
}

export const BlogPostForm = ({...props}) => {
  let schema = modelSchema(props);
  return (
    <Form
      schema={schema}
      value={props.postForm}
      onSubmit={props.postPost}
      delay={100}
    >
    <Form.Button type='submit'>Submit</Form.Button>
    </Form>
  );
}

