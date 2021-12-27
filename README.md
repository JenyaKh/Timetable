# Timetable

This project is a Django GraphQL application that manages the training schedule.
To add a workout to the schedule, use the admin panel:
https://pure-headland-70258.herokuapp.com/admin/ (user - admin, password - admin)  

https://pure-headland-70258.herokuapp.com/graphql/ - API with an opportunity:
- getting a list of workouts for a specified time ( to indicate the beginning of the time range, the from_time parameter is specified, the end of the range - to_time. It is possible to specify the training date or the date and time. If the parameter is absent, the current date and time are taken.
- retrieving Workout Details by ID ( parameter id)
