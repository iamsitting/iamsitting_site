<template>
  <!-- Footer -->
  <footer class="page-footer">
    <hr>
    <div class="container">
      <div class="row">
        <div class="col-sm">
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
        </div>
        <div class="col-sm-1">
        </div>
        <div class="col-sm">
          <div class="more-info">
            <p>Adress: Bryan/College Station, Texas</p>
          </div>
          <div class="more-info">
            <p>Phone: (Just email me.)</p>
          </div>
          <div class="more-info">
            <p>Email: carlos@iamsitting.com</p>
          </div>
        </div>
      </div>
    </div>
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

<style lang="scss" scoped>
  .page-footer {
    hr {
      background-color: white;
    }
  }
  .more-info {
    padding: 10% 0 5% 0;
    border: 1px solid white;
  }
  .footer-copyright {
    padding: 3%;
  }
</style>