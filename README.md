# Timetable

This project is a Django GraphQL application that manages the training schedule.
To add a workout to the schedule, use the admin panel:
https://pure-headland-70258.herokuapp.com/admin/ (user - admin, password - admin)  

https://pure-headland-70258.herokuapp.com/graphql/ - API with an opportunity:
- getting a list of workouts for a specified time ( property timetable. Parameters fromDate, toDate. In the absence of parameters, the current date is taken)  
- for example:
 ```
 query gettimetable{
  timetable(fromDate: "27/12/2021"){
   training{
    name
  }
    date
  }

}
```  

- retrieving Workout Details by ID (property training, parameter id)
for example: 
```
query getTraining {
  training(id:2){
    name
    description
  }
}
```
