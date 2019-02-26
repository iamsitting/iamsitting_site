import * as $ from 'jquery';

//import editor js files
import 'froala-editor/js/froala_editor.pkgd.min.js';

//import editor css files
import 'froala-editor/css/froala_style.min.css';
import 'froala-editor/css/froala_editor.pkgd.min.css';

//import font awesome
import 'font-awesome/css/font-awesome.css';

$(document).ready(() => {
  $('textarea.mceEditor').froalaEditor();
});
