import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import DatatableFactory from 'vuejs-datatable'

Vue.use(DatatableFactory)
Vue.config.productionTip = false

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#blog-app')
