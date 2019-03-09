<template>
  <div class="hello">
    <p>The data below is added/removed from the SQLite Database using Django's ORM and Rest Framework.</p>
    <br/>
    <p>Title</p>
    <input type="text" placeholder="Hello" v-model="title">
    <p>Body</p>
    <input type="text" placeholder="From the other side" v-model="body">
    <p>subtitle</p>
    <input type="text" placeholder="From the other side" v-model="subtitle">
    <br><br>
    <input 
      type="submit" 
      value="Add" 
      @click="addBlogPost({ title: title, body: body, subtitle: subtitle })" 
      :disabled="!title || !body">

    <hr/>
    <h3>Messages on Database</h3>
    <p v-if="blogPosts.length === 0">No Messages</p>
    <!-- <div class="msg" v-for="(msg, index) in messages" :key="index">
        <p class="msg-index">[{{index}}]</p>
        <p class="msg-subject" v-html="msg.subject"></p>
        <p class="msg-body" v-html="msg.body"></p>
        <input type="submit" @click="deleteMessage(msg.pk)" value="Delete" />
    </div> -->
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'

  export default {
    name: "BlogPosts",
    data() {
      return {
        title: "",
        subtitle: "",
        body: "",
      };
    },
    computed: mapState({
      blogPosts: state => state.blogPosts.blogPosts
    }),
    methods: mapActions('blogPosts', [
      'addBlogPost',
      'deleteBlogPost'
    ]),
    created() {
      this.$store.dispatch('blogPosts/getBlogPosts')
    }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
  max-width: 65%;
}
.msg {
  margin: 0 auto;
  max-width: 30%;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}
.msg-index {
  color: #ccc;
  font-size: 0.8rem;
  /* margin-bottom: 0; */
}
img {
  width: 250px;
  padding-top: 50px;
  padding-bottom: 50px;
}
</style>
