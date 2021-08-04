# ClimbTracker
Climb Tracker is a login based system that keeps track of an individual climber's completed climbs at different gyms. It's purpose is for users to be able to see the records of their climbs at indoor gyms. As an example, after registering and logging in, the user may select from a number of gyms and see the actual number of different level of climbs that the climber has finished at that specific gym.

Ex)
* Boulder
  - v3 - 15
  - v4 - 10
  - v5 - 8

* Top Rope/Lead
  - 5.10c - 6
  - 5.10d - 7
  - 5.11a - 2

The user will also have the option to add to the existing number of completed climbs.

## Dependencies
ClimbTracker is an application built using PyQt. You can install on Python >= 3.6 using the command `pip install pyqt5`. SQLite is used to handle the database and PyQt's SQL support connects the application to the database.

## References
This project was built by adding on top of a [contact book tutorial](https://realpython.com/python-contact-book/).