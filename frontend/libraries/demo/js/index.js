import 'bootstrap';
import 'demo/sass/main.scss'
import 'select2'
import 'select2/dist/css/select2.css'
import * as step2 from 'demo/js/step2'

$(document).ready(() => {
  $('.container h1').text('Welcome to your demo!');

  $(".select-patient").select2({
    width: "50%",
    ajax: {
      url: 'api/patients/',
      dataType: 'json',
      data: function (params) {
        return {
          search: params.term, // search term
        };
      },
      processResults: function (apiResults) {
        let data = [];
        $.each(apiResults, function (index, patient) {
          data.push({
            id: patient.id,
            text: patient.firstname + ' ' + patient.lastname
          });
        });
        return {
          "results": data
        };
      },
    },
    placeholder: 'Search for a patient',
    minimumInputLength: 1,
  });

  $('.select-patient').on('select2:select', function (e) {
    $('#step-1').fadeOut('slow', function(){
        $('#step-2').fadeIn('slow');
    });
    // step 2
    step2.begin(e.params.data.id);
  });

});

