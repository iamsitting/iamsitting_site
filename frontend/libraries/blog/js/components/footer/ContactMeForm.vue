<template>
  <form method="post" action="/contact-me/">
    <div class="form-group">
      <label for="name">Name</label>
      <input class="form-control" type="text" name="name" id="name"/>
    </div>
    <div class="form-group">
      <label for="email">Email</label>
      <input class="form-control" type="text" name="email" id="email"/>
    </div>
    <div class="form-group">
      <label for="message">Message</label>
      <textarea class="form-control" name="message" id="message" rows="3"></textarea>
    </div>
    <input class="btn btn-primary" type="submit" value="Send Message" onclick="return confirm('Are you sure?');"/></li>
  </form>
</template>

<script>
  export default {
    name: 'ContactMeForm'    
  }
</script>