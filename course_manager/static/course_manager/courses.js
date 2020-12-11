document.addEventListener('DOMContentLoaded', function() {
    basicDisplay()

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
        document.querySelector('#header').innerHTML =  `<b>${result.title}</b>`
        document.querySelector('#course_view').style.display = 'block';

        document.querySelector('#subject').innerHTML = `${result.subject}`;
        document.querySelector('#professor').innerHTML = `Professor: <b>${result.professor}</b>`;
        document.querySelector('#days').innerHTML = `Days: <b>${result.day}</b> from <b>${result.start_time}</b> to <b>${result.end_time}</b>`;
        document.querySelector('#description').innerHTML = `${result.description}`;
        
        document.querySelector('#go-back').addEventListener('click', () => 
        basicDisplay())
    })
}

  function basicDisplay() {
    fetch( `/coursesapi`, {
      method: 'GET',
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
       }
    })
    .then(response => response.json())
    .then(result => {
      for(var i=0; i<result.length; i++) { 
    }
    })

    document.querySelector('#course_view').style.display = 'none';
    document.querySelector('#courses').style.display = 'block';
    document.querySelector('#header').innerHTML =  `<b>Course Catalog</b>`

  }
