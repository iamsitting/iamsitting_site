<template>
  <div id="app">
    <h1>Blog App</h1>
    <div id="nav">
      <router-link :to="{ name: 'home'}">Vue</router-link>
      <router-link :to="{ name: 'blog-posts'}">Django Rest</router-link>
    </div>
  </div>
</template>

<style>
  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>