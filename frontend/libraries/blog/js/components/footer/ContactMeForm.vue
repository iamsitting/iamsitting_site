<template>
  <form id="contactMeForm" @submit.prevent="processForm">
    <div class="form-group">
      <label for="name">Name</label>
      <input v-model="name" class="form-control" type="text" name="name" id="name"/>
    </div>
    <div class="form-group">
      <label for="email">Email</label>
      <input v-model="email" class="form-control" type="text" name="email" id="email"/>
    </div>
    <div class="form-group">
      <label for="message">Message</label>
      <textarea v-model="message" class="form-control" name="message" id="message" rows="3"></textarea>
    </div>
    <input class="btn btn-primary" type="submit" value="Send Message" onclick="return confirm('Are you sure?');"/></li>
  </form>
</template>

<script>
  import Cookies from 'js-cookie'
  import axios from 'axios'
  import qs from 'qs'
  export default {
    name: 'ContactMeForm',
    data() {
      return {
        name: "",
        email: "",
        message: ""
      }
    },
    methods: {
      processForm: function() {
        axios({
          method: 'post',
          url: '/contact-me/',
          data: qs.stringify({
            name: this.name,
            email: this.email,
            message: this.message
          }),
          headers: {
            'X-CSRFToken': Cookies.get('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded',
          }
        }).then(response => {
          if (response.status === '200'){
            $('#contactMeForm').trigger('reset');
          }
        });
      }
    }
  }
</script>