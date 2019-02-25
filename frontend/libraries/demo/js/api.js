export function getPatient(id){
  return $.ajax({
    url: 'api/patients/' + id,
  });
}