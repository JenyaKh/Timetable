# Timetable

This project is a Django GraphQL application that manages the training schedule.
To add a workout to the schedule, use the admin panel:
https://pure-headland-70258.herokuapp.com/admin/ (user - admin, password - admin)  

https://pure-headland-70258.herokuapp.com/graphql/ - API with an opportunity:
- getting a list of workouts for a specified time ( property timetable. Parameters fromDate, toDate. In the absence of parameters, the current date is taken)
- retrieving Workout Details by ID (property training, parameter id)
