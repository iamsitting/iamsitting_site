import 'sammy'
import 'bootstrap';
import 'blog/sass/main.scss'
import {blogApp} from 'blog/js/app'


//import editor js files
import 'froala-editor/js/froala_editor.pkgd.min.js';

//import editor css files
import 'froala-editor/css/froala_style.min.css';
import 'froala-editor/css/froala_editor.pkgd.min.css';

//import font awesome
import 'font-awesome/css/font-awesome.css';

(function($) {
      
        $.sammy(function() {
      
        });
      
      })(jQuery);

$(document).ready(function() {
  //console.log(Sammy())
  //blogApp.run('#/about/');

  // $('textarea.mceEditor').froalaEditor({
  //    height: 300
  // });
});
