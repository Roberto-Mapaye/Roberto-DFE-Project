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

The frontend service is connected to the Backend API, and has code that allows its to connect/commmunicate with it. This is done through routing. 

```
@app.route('/')
@app.route('/home')
def home():
    all_teams = requests.get(f"http://{backend}/read/allTeams").json()
    return render_template('index.html', all_teams=all_teams["teams"])
```
Shown above is my code trying to access another code from the backend folder by refering to it through its route (read/allTeams). If the website goes to a route '/' or '/home', it will send a message to the backend, which is then used to render the template into the HTML. 

![HomePage](https://i.imgur.com/hNlBNLX.png)

The application has two links which allows it to add a team and player for that team. 

#### By clicking add team, a new team will be made. 

![Add Team Page](https://i.imgur.com/Gz10HN4.png)

![New Team Page](https://i.imgur.com/65IR10t.png)

#### By clicking add player, a new player will be made

![Add Player Page](https://i.imgur.com/TFKTU7U.png)

![New Player Page](https://i.imgur.com/2l2LSCu.png)

#### There is also an edit feature which is used to edit each detail. 

![Edit Team Page](https://i.imgur.com/zhc7mnO.png)

![Updated Player Page](https://i.imgur.com/QY69gq9.png)


### Backend Service

Once a request has been made from the frontend, it'll send a message to the backend. Once this happens, the backend will send a return json script to be loaded into the HTML

```
@app.route('/read/allTeams', methods=['GET'])
def read_all_teams():
    all_teams = Teams.query.all()
    teams_dict = {"teams": []}
    for teams in all_teams:
        players = []
        for player in teams.org:
            players.append(
                {
                    "player_id": player.player_id,
                    "first_name": player.first_name,
                    "last_name": player.last_name
                }
            )
        teams_dict["teams"].append(
            {
                "team_id": teams.team_id,
                "team_name": teams.team_name,
                "game": teams.game,
                "org": players
            }
        )
    return jsonify(teams_dict)

```
Shown above is an example of this, where the backend sends a GET Method. This get method gets the data from the database and adds it into dictionary so that it can be loaded into a json script for HTML. This script uses two for loops that gets each team, and gets the player within each team. The frontend will then load this data into the HTML.

This is also similar to the other commands such as Add, Edit and Delete.

#### Add Team

```
@app.route('/create/teams', methods=['POST'])
def create_teams():
    package = request.json
    new_teams = Teams(team_name=package["team_name"], game=package["game"])
    db.session.add(new_teams)
    db.session.commit()
    return f"Planet '{new_teams.team_name}' added to database"
```

#### Edit Team

```
@app.route('/update/team/<int:id>', methods=['PUT'])
def update_team(id):
    package = request.json
    team = Teams.query.get(id)
    team.team_name = package["team_name"]
    team.game = package["game"]
    db.session.commit()
    return Response(f"Updated task (ID: {id}) with description: {team.team_name}", mimetype='text/plain')
```


#### Delete Team
```
@app.route('/delete/team/<int:id>', methods=['DELETE'])
def delete_teams(id):
    teams = Teams.query.get(id)
    db.session.delete(teams)
    db.session.commit()
    return Response(f"Deleted task with ID: {id}", mimetype='text/plain')
```

## CI/CD Pipeline



## Testing

By the use of pytest and Jenkins, I created test logs, test coverages and reports. The Jenkins pipelines reads these test coverage and uses a plugin (cobertura) to translate these data into easily read information. 

![Test Results](https://i.imgur.com/jqlJzvZ.png)

Out of 22 tests, about 6 failed. While i do wish that we succeed and obtain 100% success rate, the problems tend to relate with using relational databases. It does succeed and work regardless. 

![Backend](https://i.imgur.com/PC7Pj3F.png)

![Frontend](https://i.imgur.com/kyKVUg0.png)

The coverage is over 80% for both backend and frontend. Overall, my coverage is around 92%, which means that i tested most of the code in my project. 

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
