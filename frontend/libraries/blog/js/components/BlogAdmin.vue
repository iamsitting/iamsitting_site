<template>
  <div>
    <blog-post-form/></blog-post-form>
    <blog-post-table/></blog-post-table>
  </div>
</template>

<script>
  import BlogPostTable from 'blog/js/components/BlogPostTable.vue'
  import BlogPostForm from 'blog/js/components/BlogPostForm.vue'
  export default {
    name: 'BlogHome',
    components: {
      BlogPostForm,
      BlogPostTable
    }
  }
</script>

<style scoped>
</style>
