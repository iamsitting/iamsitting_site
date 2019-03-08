<template>
  <div>
     <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
      <div class="container">
        <a class="navbar-brand" href="#">Blog</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home
                <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'home'}">Vue</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'blog-posts'}">Django Rest</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Tab 2</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="view-container">
      <router-view/>
    </div>
  </div>
</template>

<style lang="scss">
  @import "~bootstrap/scss/bootstrap";
  .hidden {
    display: none;
  }
  .view-container {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>