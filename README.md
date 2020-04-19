Brief follows a lab completed at CodeClan in Ruby, to learn Python.

Deployed on Heroku: https://jmm-python-hogwarts.herokuapp.com/students

**App outline**
- The user can add students.
- The user can view an individual student and sort them into a house (random selection)
- The user can expel (delete) a student

**Summary of original brief:**

- Create a CRUD app for adding Students to Hogwarts

- GET - '/students' - index action - index page to display all students
- GET - '/students/new' - new action - displays create student form
- GET - '/students/:id' - show action - displays one student based on ID in the url
- POST - '/students' - create action - creates one student
- GET - '/students/:id/edit' - edit action - displays edit form based on ID in the url
- POST - '/students/:id' - update action - replaces an existing student based on ID in the url
- POST - '/students/:id/delete' - destroy action - deletes one student based on ID in the url

Note: did not include authentication, so mocked a prototype of user login/logout experience.

Ruby Project: https://github.com/jenmerritt/ruby_hogwarts_lab
