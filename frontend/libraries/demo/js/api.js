export function getPatient(id){
  return $.ajax({
    url: 'api/patients/' + id,
  });
}

export function getPatientDose(id){
  return $.ajax({
    url: 'get-patient-dose/' + id,
  });
}
