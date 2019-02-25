import {getPatient} from 'demo/js/api'
export function begin(patientId){
  basicInfo(patientId);
}

function basicInfo(id){
  let patientData = getPatient(id);
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
  patientData.then(function (data) {
    console.log(data);
    let $tbody = $('#patient-table').find('tbody');
    $.each(data, function (k, v) {
      $tbody.append('<tr><td>'+k+'</td><td>'+v+'</td></tr>');
    });
  });
}
