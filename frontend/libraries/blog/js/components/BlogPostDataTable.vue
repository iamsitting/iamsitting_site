<template>
  <div class="container blog-table__container">
    <datatable :columns="columns" :rows="rows"></datatable>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  export default {
    name: 'BlogPostDataTable',
    props: ['row', 'column'],
    data() {
      return {
        columns: [
          { label: 'Title', field: 'title' },
          //{ label: 'Category', field: 'category'}
        ],
        page: 1,
        per_page: 10
      }
    },
    computed: mapState({
      rows: state => state.blogPosts.blogPosts
    }),
    created() {
      this.$store.dispatch('blogPosts/getBlogPosts')
    }
  }
</script>

<style lang="scss" scoped>
  .blog-table {
    @at-root #{&}__container {
      padding: 5%;
      background-color: white;
    }
  }
</style>