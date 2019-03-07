import 'bootstrap'
import "bootstrap/scss/bootstrap.scss"
import * as sammy from 'sammy'
import 'sammy/lib/plugins/sammy.handlebars'
import {appRoutes} from './routes'

let app = sammy("#app", function() {
  this.use('Handlebars', 'hb');
  // this.around(function(callback) {
  //     let context = this;
  //     this.load('API_URL')
  //       .then(function(items) {
  //         context.items = items;
  //     }).then(callback);
  //   });
  // this.before('.*', function() {

  //     let hash = document.location.hash;
  //     $(“nav”).find('a').removeClass("current");
  //     $(“nav”).find("a[href='"+hash+"']").addClass("current");
  //   });
  this.mapRoutes(appRoutes);
});

$(document).ready(() => {
  app.run('blog/');
});
