## Installation

### Requirements
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Heroku](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

### Procedure
- Create an account on heroku (follow this [link](https://signup.heroku.com/login))
- Login on heroku and create a new app

### Setup
- Create a new git repository in the folder containing the project
-  Add heroku remote using `heroku git:remote -a worldcup-flask`
-  Copy the files `requirements.txt` and `Procfile` from this repo
-  Commit your code running the following commands (or using the git GUI)
```
    git add .
    git commit -am "first commit"
    git push heroku master
```