<template>
  <div class="container">
    <div class="row">
      <h1> List of Posts
      <button class="btn btn-success">Add Post</button>
      </h1> 
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Title</th>
            <th scope="col">Author</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="p in posts">
            <th scope="row">${p.id}</th>
            <th scope="row">${p.title}</th>
            <th scope="row">${p.author}</th>
          </tr>
        </tbody>
      </table>
    </div> 
  </div>
</template>

<script>
  // <div class="loading" v-if="loading===true">Loading &#8230;</div>
</script>

<style>
  h1 {
    color: red;
  }
</style>