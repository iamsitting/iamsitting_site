<template>
  <div class="more-info__section--container">
    <more-info-panel :content="addressContent"></more-info-panel>
    <more-info-panel :content="phoneContent"></more-info-panel>
    <more-info-panel :content="emailContent"></more-info-panel>
  </div>
</template>

<script>
  import MoreInfoPanel from 'blog/js/components/footer/MoreInfoPanel.vue'
  export default {
    name: 'MoreInfoSection',
    components: {
      MoreInfoPanel
    },
    data() {
      return {
        addressContent: 'Address: Bryan/College Station, Texas',
        phoneContent: 'Phone: (Just email me...)',
        emailContent: 'Email: carlos@iamsitting.com'
      }
    }
  }
</script>

<style lang="scss" scoped>
  .more-info__section--container {
    margin-top: 10%;
  }
</style>