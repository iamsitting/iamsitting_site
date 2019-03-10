<template>
  <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
      <div class="container">
        <a class="navbar-brand" href="/">@iamsitting</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <router-link class="nav-link" :to="{ name: 'home'}">Blog</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'blog-posts'}">New Post</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Post Requests</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Sign Up</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
</template>
<script>
  export default {
    name: 'BlogNavigation'
  }
</script>