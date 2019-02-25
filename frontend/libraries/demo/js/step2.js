import {getPatient, getPatientDose} from 'demo/js/api'
export function begin(patientId){
  basicInfo(patientId);
}

function basicInfo(id){
  let patientData = getPatient(id);
  let patientDose = getPatientDose(id);
  $("#patient-data").append(`
    <div class="table-responsive">
      <table class='table table-hover' id="patient-table">
        <thead>
          <tr>
            <th>KEY</th>
            <th>VALUE</th>
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
    </div>
    `)
  $("#patient-dose").append(`
    <div class="table-responsive">
      <table class='table table-hover' id="dose-table">
        <thead>
          <tr>
            <th>KEY</th>
            <th>VALUE</th>
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
    </div>
    `)
  patientData.then(function (data) {
    let $tbody = $('#patient-table').find('tbody');
    $.each(data, function (k, v) {
      $tbody.append('<tr><td>'+k+'</td><td>'+v+'</td></tr>');
    });
  });

  patientDose.then(function (data) {
    let $tbody = $('#dose-table').find('tbody');
    $.each(data, function (k, v) {
      $tbody.append('<tr><td>'+k+'</td><td>'+v+'</td></tr>');
    });
  });

}
