import 'sammy'
import {appRoutes} from 'routes'

let app = $.samme("#app", function() {
  this.use('Template');
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
  app.run('#/about/');
});
