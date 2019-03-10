<template>
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
</template>

<script>
  export default {
    name: 'BlogFooter'
  }
</script>