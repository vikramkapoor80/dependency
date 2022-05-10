# NPM Packages Dependency Collisions

NPM Packages Dependency Collisions 

TNPM Packages Dependency Collisions  helps in Dependency management since Dependency management can cause huge headaches for teams as they troubleshoot and resolve conflicting in first-order (1-layer deep) transient dependencies.

## Features

- Flask Based Fullstack solution
- Bootstrap Based User interface


## Primary Goals

 - To help in troubleshooting and resolving conflicting in first-order (1-layer deep) transient dependencies 



## Table of Contents

1. [Getting Started](#getting-started)
1. [Screenshots](#screenshots)
1. [Dependancies](#dependancies)
1. [Project Structure](#project-structure)




## Getting Started

clone the project

```bash
$ git clone npmdependanciescollisions.git
$ cd npmdependanciescollisions
```

create virtual environment using python3 and activate it (keep it outside our project directory)

```bash
$ python3 -m venv /path/to/your/virtual/environment
$ source <path/to/venv>/bin/activate
```

install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

setup `flask` command for our app

```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

5) start test server at `localhost:5000`

```bash
$ flask run
```


## Screenshots

![Home](/screenshots/home.png)
![Dependancies](/screenshots/dependancy.png)
![Error](/screenshots/error.png)



## Dependancies

- asgiref==3.5.1
- certifi==2021.10.8
- charset-normalizer==2.0.12
- click==8.1.3
- colorama==0.4.4
- Flask==2.0.2
- idna==3.3
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.1
- requests==2.27.1
- urllib3==1.26.9
- Werkzeug==2.1.2



## Project Structure

npmdependanciescollisions
├── static
│   ├── bootstrap.bundle.min.js
│   ├── bootstrap.min.css
│   └── jquery.slim.min.js
├── templates
│   │   ├── base.html
│   │   ├── msg.html
│   │   ├── header.html
│   │   ├── index.html
│   │   ├── dependancy.html
│   │   ├── _form.html
├── app.py
├── README.md
├── .gitignore
├── requirements.txt
├── screenshots
│   ├── home.png
│   ├── error.png
│   └── dependancy.png

