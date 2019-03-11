<template>
  <div>
    <blog-post-view/></blog-post-view>
  </div>
</template>

<script>
  import BlogPostView from 'blog/js/components/BlogPostView.vue'
  export default {
    name: 'BlogHome',
    components: {
      BlogPostView
    }
  }
</script>
