<p text-align="center">

## ToDoApp
[![Docker Image CI](https://github.com/nijatrajab/todoapp/actions/workflows/docker-auto.yml/badge.svg)](https://github.com/nijatrajab/todoapp/actions/workflows/docker-auto.yml)
[![Project stage: Production Ready][project-stage-badge: Production Ready]][project-stage-page]

[project-stage-badge: Production Ready]: https://img.shields.io/badge/Project%20Stage-Production%20Ready-brightgreen.svg
[project-stage-page]: https://blog.pother.ca/project-stages/

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://todoapp-pvlnj4az7q-lm.a.run.app/)
[![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/nijatrajab/todoapp/actions)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/get-started)

</p>

### App is live on _Google Cloud_
## [ToDoApp](https://todoapp-pvlnj4az7q-lm.a.run.app/)
_Also app supports continuous deployment with `Cloud Run (Buildpacks)`._

## Local Development

### Dependencies

* [Docker](https://www.docker.com/get-started)

### Installing

* Clone the repo
```
git clone https://github.com/nijatrajab/todoapp.git
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

After creating docker images it will automatically start containers for a service. There is also 2 options
* On Docker Desktop start your containers using GUI or open `cmd` on cloned directory then follow commands:
```
docker-compose up
```
_Make sure Docker is running as an administrator. For the first time it may take a few minutes to start because of creating containers_