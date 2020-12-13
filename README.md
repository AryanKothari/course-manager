# course-manager

As an incoming freshman at Duke University, I made this project because I wanted a way of being able to organise/schedule my courses. This web app will help an individual keep track of the classes they're enrolled in and navigate through multiple course offerings (both ones that are manually input or sources using the Duke Course Catalog API).

In this project,  I created a User and Course model, that keeps track of every courses title, professor, description, timings, and more. This course model is then updated using a form PUT request (on the create Http page). Then, to view more information about each course, I created a REST API that is then accessed through the REST API as a GET request on the front end (By JS) and then displayed on the screen for the user to see. 
