<template>
  <div>
    <blog-post-form/></blog-post-form>
    <!-- <blog-post-table/></blog-post-table> -->
    <blog-post-data-table></blog-post-data-table>
  </div>
</template>

<script>
  import BlogPostTable from 'blog/js/components/BlogPostTable.vue'
  import BlogPostDataTable from 'blog/js/components/BlogPostDataTable.vue'
  import BlogPostForm from 'blog/js/components/BlogPostForm.vue'
  export default {
    name: 'BlogHome',
    components: {
      BlogPostForm,
      BlogPostTable,
      BlogPostDataTable
    }
  }
</script>

<style scoped>
</style>
