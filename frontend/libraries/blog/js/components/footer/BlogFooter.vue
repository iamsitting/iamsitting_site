<template>
  <!-- Footer -->
  <footer class="page-footer">
    <hr>
    <div class="container">
      <div class="row">
        <div class="col-sm">
          <contact-me-form></contact-me-form>
        </div>
        <div class="col-sm-1">
        </div>
        <div class="col-sm">
          <more-info-section></more-info-section> 
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
  import ContactMeForm from 'blog/js/components/footer/ContactMeForm.vue'
  import MoreInfoSection from 'blog/js/components/footer/MoreInfoSection.vue'
  export default {
    name: 'BlogFooter',
    components: {
      ContactMeForm,
      MoreInfoSection
    }
  }
</script>

<style lang="scss" scoped>
  .page-footer {
    hr {
      background-color: white;
    }
  }
  .footer-copyright {
    padding: 3%;
  }
</style>