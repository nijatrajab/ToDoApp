# Basic ToDo app

## Description

Welcome to ToDo app

## Getting Started

### Dependencies

* [Docker](https://www.docker.com/get-started)

### Installing

* Clone the repo
```
git clone https://github.com/nijatrajab/ToDoApp.git
```
* Create `.env` file on cloned directory and define your passwords
```
SECRET_KEY='YOUR DJANGO SECRET KEY'
DEBUG=0 for False | 1 for True
DB_HOST=YOUR DB HOST
DB_NAME=YOUR DB NAME
DB_USER=YOUR DB USER
DB_PASS=YOUR DB PASSWORD
POSTGRES_DB=YOUR DB NAME
POSTGRES_USER=YOUR DB USER
POSTGRES_PASSWORD=YOUR DB PASSWORD
```
* Open `cmd` on cloned directory then follow commands:
```
docker-compose up
```

### Executing program

After creating docker images it will automaticly start containers for a service. There is also 2 options
* On Docker Desktop start your containers using GUI or open `cmd` on cloned directory then follow commands:
```
docker-compose up
```
_Make sure Docker is running as an administrator. For the first time it may take a few minutes to start because of creating containers_

