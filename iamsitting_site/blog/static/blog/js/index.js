// Import TinyMCE
import tinymce from 'tinymce/tinymce';

// A theme is also required
import 'tinymce/themes/modern/theme';

// Any plugins you want to use has to be imported
//"advlist autolink autosave link image lists charmap print preview hr anchor pagebreak",
import 'tinymce/plugins/advlist';
import 'tinymce/plugins/autolink';
import 'tinymce/plugins/autosave';
import 'tinymce/plugins/link';
import 'tinymce/plugins/image'
import 'tinymce/plugins/lists';
import 'tinymce/plugins/charmap';
import 'tinymce/plugins/print';
import 'tinymce/plugins/preview';
import 'tinymce/plugins/hr';
import 'tinymce/plugins/anchor';
import 'tinymce/plugins/pagebreak';

//"searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
import 'tinymce/plugins/searchreplace';
import 'tinymce/plugins/wordcount';
import 'tinymce/plugins/visualblocks';
import 'tinymce/plugins/visualchars';
import 'tinymce/plugins/code';
import 'tinymce/plugins/fullscreen';
import 'tinymce/plugins/insertdatetime';
import 'tinymce/plugins/media';
import 'tinymce/plugins/nonbreaking';

//"table contextmenu directionality emoticons template textcolor paste fullpage textcolor colorpicker textpattern"
import 'tinymce/plugins/table';
import 'tinymce/plugins/contextmenu';
import 'tinymce/plugins/directionality';
import 'tinymce/plugins/emoticons';
import 'tinymce/plugins/template';
import 'tinymce/plugins/textcolor';
import 'tinymce/plugins/paste';
import 'tinymce/plugins/fullpage';
import 'tinymce/plugins/colorpicker';
import 'tinymce/plugins/textpattern';
    

let plugin_str = "advlist autolink autosave link image lists charmap print preview hr anchor pagebreak " +
    "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking " +
    "table contextmenu directionality emoticons template textcolor paste fullpage textcolor colorpicker textpattern"

let plugin_list = plugin_str.split(" ")


tinymce.init({
  mode: "textareas",
  editor_selector: "mceEditor",
  //selector: "textarea",
  height: 500,
  plugins: plugin_list,

  toolbar1: "newdocument fullpage | bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | styleselect formatselect fontselect fontsizeselect",
  toolbar2: "cut copy paste | searchreplace | bullist numlist | outdent indent blockquote | undo redo | link unlink anchor image media code | insertdatetime preview | forecolor backcolor",
  toolbar3: "table | hr removeformat | subscript superscript | charmap emoticons | print fullscreen | ltr rtl | visualchars visualblocks nonbreaking template pagebreak restoredraft",
  content_css: [
    '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tinymce.com/css/codepen.min.css'],

  menubar: false,
  toolbar_items_size: 'small',

  style_formats: [{
    title: 'Bold text',
    inline: 'b'
  }, {
    title: 'Red text',
    inline: 'span',
    styles: {
      color: '#ff0000'
    }
  }, {
    title: 'Red header',
    block: 'h1',
    styles: {
      color: '#ff0000'
    }
  }, {
    title: 'Example 1',
    inline: 'span',
    classes: 'example1'
  }, {
    title: 'Example 2',
    inline: 'span',
    classes: 'example2'
  }, {
    title: 'Table styles'
  }, {
    title: 'Table row 1',
    selector: 'tr',
    classes: 'tablerow1'
  }],

  templates: [{
    title: 'Test template 1',
    content: 'Test 1'
  }, {
    title: 'Test template 2',
    content: 'Test 2'
  }],

  //image uploader/picker
 // enable title field in the Image dialog
  image_title: true, 
  // enable automatic uploads of images represented by blob or data URIs
  automatic_uploads: true,
  // URL of our upload handler (for more details check: https://www.tinymce.com/docs/configure/file-image-upload/#images_upload_url)
  images_upload_url: '/api/images/',
  // here we add custom filepicker only to Image dialog
  file_picker_types: 'image', 
  // and here's our custom image picker
  file_picker_callback: function(cb, value, meta) {
    var input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', 'image/*');
    
    // Note: In modern browsers input[type="file"] is functional without 
    // even adding it to the DOM, but that might not be the case in some older
    // or quirky browsers like IE, so you might want to add it to the DOM
    // just in case, and visually hide it. And do not forget do remove it
    // once you do not need it anymore.

    input.onchange = function() {
      var file = this.files[0];
      
      var reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = function () {
        // Note: Now we need to register the blob in TinyMCEs image blob
        // registry. In the next release this part hopefully won't be
        // necessary, as we are looking to handle it internally.
        var id = 'blobid' + (new Date()).getTime();
        var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
        var base64 = reader.result.split(',')[1];
        var blobInfo = blobCache.create(id, file, base64);
        blobCache.add(blobInfo);

        // call the callback and populate the Title field with the file name
        cb(blobInfo.blobUri(), { title: file.name });
      };
    };
    
    input.click();
  } 

});
