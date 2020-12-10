document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#course_view').style.display = 'none';
    document.querySelector('#courses').style.display = 'block';

    Array.from(document.querySelectorAll('.view-course')).forEach(button => 
    button.onclick = view_course)
  })


  function view_course(e) {
    let course_id = e.target.dataset.course_id
    document.querySelector('#courses').style.display = 'none';
    fetch( `/coursesapi/${course_id}`, {
      method: 'GET',
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
       }
    })
    .then(response => response.json())
    .then(result => {
        console.log(result)
        document.querySelector('#course_view').style.display = 'block';
    })
}
