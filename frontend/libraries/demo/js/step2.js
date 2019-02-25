import {getPatient, getPatientDose} from 'demo/js/api'
export function begin(patientId){
  basicInfo(patientId);
}

function basicInfo(id){
  let patientData = getPatient(id);
  let patientDose = getPatientDose(id);
  $("#patient-data").append(`
    <table id="patient-table">
      <thead>
        <tr>
          <th>KEY</th>
          <th>VALUE</th>
        </tr>
      </thead>
      <tbody>
      </tbody>
    </table>
    `)
  $("#patient-dose").append(`
    <table id="dose-table">
      <thead>
        <tr>
          <th>KEY</th>
          <th>VALUE</th>
        </tr>
      </thead>
      <tbody>
      </tbody>
    </table>
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
