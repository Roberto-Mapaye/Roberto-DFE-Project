# Roberto-DFE-Project

This is Roberto Jr Mapaye's Project. This will focus on the knowledge I have learned throughout the QA Academy Bootcamp as I create an Esports Team tracker. This Esports team tracker will showcase the players and what team they are a part of. 

This project will showcase the CRUD functionality, The relationships between two tables (Players and Teams), the usage of a frontend and backend, CI/CD and Testing. The project also must run within a containers and have continuous intergration/deployment pipeline for automatic testing, building and deployment. 

## Planning and Introduction

For my project, I plan on creating a website that will create esports teams and allow players to be added to it. There will be two tables, The teams and the players.

![ERD](https://i.imgur.com/lpOmfct.png)

Shown above would be how I plan on creating my database and its structure. I plan on creating a many to one structure between the players and team table, using Team ID as a Foreign Key and to have the data stored into the org key. 


## Project Management and Version Control

To manage my project, I utilized the GitHub's Project Tab to create a project board to place down issues and create user stories. 

![GitHub Project Board](https://i.imgur.com/iVMBP1S.png)

As shown above, I created another column for user stories and categorized each issues depending on their importance (MUST, SHOULD, COULD, HAVE). The categories represent the MoSCoW method and the user stories help me understand the features needed for the application. The GitHub project board allows me to automate the issues, which allows me to instantly send it to the "Complete" column if its done. 

![Branches](https://i.imgur.com/rFGVman.png)

I have also used branches in git, making a dev branch for developemt and the main branch for when a feature is complete. There was a test branch used but was merged into the dev branch during developemtn. 

## Application

This application is not a monolothic design but uses two services, one of which is a backend api that connects to the database in Microsoft Azure. The other service is the frontend, which contains the HTML and forms used to interact with the user. 

### Frontend Service

### Backend Service

## CI/CD Pipeline

## Testing

By the use of pytest and Jenkins, I created test logs, test coverages and reports. The Jenkins pipelines reads these test coverage and uses a plugin (cobertura) to translate these data into easily read information. 

![Test Results](https://i.imgur.com/rFGVman.png)

![Coverage](https://i.imgur.com/rFGVman.png)

The plugin themselves allow for some information regarding code coverage and the errors caused by the application that the developer can solve. 

## Issues

Here are some of the issues during developent/final build

- Unable to delete a team that contains players. Must delete players first before deleting teams
- Unable to switch teams for players (Unknown how to make this work)
- CSS design for boxes tend to join to each other when creating teams. This only happens when the previous team has no players on them. 

## Future Improvements

### Better Looks/Design

As of this moment, it looks ugly. I planned to use CSS to make it more pretty and use flexbox to spread out the teams for easier readability. The usage of more colours and images was planned but unable to complete due to time.

### Addtional Tables

There are only two tables used on the design to simplify the structure of the database. Originally, I wanted to create three tables called Organisation which will track the teams. This will create an Organisation table which relates to teams which relates to players. The reason why this wasn't added is due to time and the problems caused by using foreign keys to find information to other tables. 


## Other links

https://drive.google.com/drive/folders/1vYIxhDnMal6_JxTU9dRinxOClK7eEMD1?usp=sharing

Contains demonstration of my CI/CD pipeline and connnection to a Microsoft Azure Database. 
