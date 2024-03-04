# Client-Server-Development
CS-340 Client/Server Development at SNHU

Reflection:
How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

This project allowed me to realize that by keeping code simple and readable, you can reuse code preventing extra work for the future. For example, I will consider renaming the AnimalShelter CRUD that I created, to simple be CRUD, and make any other change to reflect that change, so that I can use the same CRUD file in the future. I also have plans to create a database and dashboard for truck driver destination delivery maps, and can resuse many elements from this project, such as the CRUD file, the upate-dashboard file to filter my results, and the update-map function to show each selected location visual geolocation.

I had quite a few issues with this project at the start. The area that I struggled with the most was my function to update my dashboard. Though I could get the datatable to display the orginal (reset) data, I had issues displaying the updated data in the datatable. To solve the solution, I ended up commenting out a great deal of the code, to narrow down the problem, and did a great deal of print statements until I found the issue. I eventually realized that at the beginning of the code we had removed the _id column, and when updating the dashboard it was necessary to do it again before return the data. Once I sovle this issue, everything else came soon after.

Computer scientist help to develop programs, and software for many computers and systems that we use on an everyday basis. By desinging software we are helping companies like Grzioso Salvare that are out there making a difference. In fact, it is very feasible to say that by creating software we are helping people, saving lives, and even changing the world!
