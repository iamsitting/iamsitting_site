<template>
  <div class="container">
    <div class="row">
      <div class="col-sm post-form__container">
        <div class="form-group">
          <label for="title">Title</label>
          <input type="text" class="form-control" name="title" id="title" placeholder="Topic" v-model="title">
        </div>
        <div class="form-group">
          <label for="subtitle">Subtitle</label>
          <input type="text" class="form-control" name="subtitle" id="subtitle" placeholder="Part 1" v-model="subtitle">
        </div>
        <div class="form-group">
          <label for="body">Body</label>
          <input type="text" class="form-control" name="body" id="body" placeholder="Lorem impsum..." v-model="body">
        </div>
        <div class="form-group">
          <label for="category">Category</label>
          <input type="text" class="form-control" name="category" id="category" placeholder="General" v-model="category">
        </div>
        <br>
        <input
          type="submit"
          value="Add"
          class="btn btn-primary"
          @click="addBlogPost({ title: title, body: body, subtitle: subtitle, category: category, author:2 })"
          :disabled="!title || !body">
      </div>
    </div>
  </div>
</template>
<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    name: 'BlogPostForm',
    data() {
      return {
        title: "",
        subtitle: "",
        body: "",
        category: "",
        author: 0
      };
    },
    computed: mapState({
      blogPosts: state => state.blogPosts.blogPosts
    }),
    methods: mapActions('blogPosts', [
      'addBlogPost',
    ])
  }
</script>

<style scoped>
  .post-form__container {
    padding-top: 5%;
  }
</style>