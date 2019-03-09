<template>
  <div>
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
    <div class="view-container">
      <router-view/>
    </div>
    <!-- Footer -->
    <footer class="page-footer">
      <form method="post" action="/contact-me/">
        <div class="field">
          <label for="name">Name</label>
          <input type="text" name="name" id="name"/>
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input type="text" name="email" id="email"/>
        </div>
        <div class="field">
          <label for="message">Message</label>
          <textarea name="message" id="message" rows="3"></textarea>
        </div>
        <ul class="actions">
          <li><input type="submit" value="Send Message" onclick="return confirm('Are you sure?');"/></li>
        </ul>
      </form>
      <!-- Copyright -->
      <div id="copyright" class="footer-copyright text-center">
        &copy; 2019 iamsitting
      </div>
    </footer>
  </div>
</template>

<style lang="scss">
  @import "~bootstrap/scss/bootstrap";
  .blog-app {
    background: url(~base_theme/images/bg.jpg) no-repeat center center fixed;
  }
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