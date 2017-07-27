# Setup

## AWS Setup

* Create an AWS account.
* Launch an EC2 instance with Ubuntu AMI.
* Make sure to get a keypair for login.
* View the description of the instance
  - Go to security group and click on it
  - Make sure SSH is in the inbound rules
  - Add Custom TCP, port 8000 from anywhere to inbound rules
  - Take note of: IPv4 Public IP
  - Take note of: Public DNS (IPv4)


### Login with SSH

Open a terminal and log into the server using the public DNS (IPV4)
ssh -i "path/to/key.pem" ubuntu@ec2...computes.amazonaws.com

## Environment Setup

First run these commands:
```
sudo apt-get update
sudo apt-get upgrade
```
Make sure python3 is installed. Run:
```
python3
```
You should get a python shell. If not, run:
```
sudo apt-get install python3
```
Run: 
```
sudo apt-get install python3-pip
```
Now create a virtual environment. Run:
```
pip3 install virtualenv
mkdir ~/Envs
cd ~/Envs
virtualenv djenv
source djenv/bin/activate #run this line everytime you log into the server
```
Now install Django. Run:
```
pip install Django
```
Start a project. Run:
```
mkdir ~/workspace # create a workspace for your project
cd ~/workspace
django-admin startproject iamsitting_site #replace 'iamsitting_site' with whatever name you want
cd iamsitting_site
python manage.py runserver # test to make sure server is running
```

## Git setup
This is completely optional. This is mostly for collaboration, but I just like to backup my work in GitHub. First create a GitHub account. Then create a repo. Do **NOT** initialize with a readme, gitignore, or license files.

Now run:
```
git config --global user.name real_name #use whatever name you want
git config --global user.email github_email #use email tied to your github account
cd ~/worskpace
git init # creates empty git repo
git add . #adds all files in worskpace to commit
git commit -m "first commit"
git remote add origin https://github.com/user/project.git #use repo url
git push -u origin master #you'll need your github username and password
```

Now we'll commit more files. Let's add gitignore, readme, and requirement files. At this point, we will write files, it may be good to setup your preferred text editors (vim, emacs, etc.). In the workspace create a file ".gitignore" write. We don't want to commit these files. We can add more as we go on.
```
.DS_Store
*.log
*.egg-info
*.pot
*.py[co]
.tox/
__pycache__
migrations/
static/
```

Now let's do README.md. This just tells everyone what you're doing.
```
# iamsitting_site

## Summary

Just a simple website
* No apps yet
```

Now requirements.txt This is a list of python packages needed to run your project. This will definitely get larger as we go on.
```
Django==1.11.3 # whatever django version your using
# add more python packages
```
Now commit these files to master.
```
git status # see which files are tracked and modified
git add .
git commit -m "message"
git push -u origin master
```

## Database setup
I like PostgreSQL, so we'll use that. First install it.
```
sudo apt-get install postgresql postgresql-contrib
```
Now create the database.
```
sudo su - postgres # changes user to postgres
psql # enters psql shell
CREATE DATABASE iamsitting_site; # use project name, don't forget ';'
CREATE USER username WITH PASSWORD 'complicatedpassword'; #use quotes
GRANT ALL PRIVILEGES ON DATABASE iamsitting_site TO iamsitting;
\q
exit
```
That's it. That was easy.

## Django Setup
We haven't touched Django much. But now we'll begin setting up. First let's add the database we just created. First, let's install psycopg2. Make sure yourin your **virtualenv**.
```
pip install psycopg2
pip freeze #to find out version number
```
**Add this package to the requirements.txt**

Now add the database to Django setings. First, in the workspace create a secrets.py with the following: 
```
db_username = 'username_for_database'
db_password = 'password_for_database'
```
**Add this secrets.py to .gitignore**

Now go to settings.py file in Django
```
cd ~/workspace/iamsitting_site/iamsitting_site
vim settings.py
```
Make these changes:
```
import os
import secrets # add this line
.
.
.
ALLOWED_HOSTS = ['public_ip'] #public_ip is from IPv4 Public IP from EC2, you can add it to secrets.py
.
.
.
DATABASES = {
  #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'iamsitting_site',
    'USER': secrets.db_username,
    'PASSWORD': secrets.db_password,
    'HOST': 'localhost',
    'PORT': '',
  }
}
.
.
.
#all the way at the bottom
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```
Now run:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser #creates admin username and password
python manage.py collectstatic #places all static files in /static directory
python manage.py runserver 0.0.0.0:8000
```

Now in your browser visit your public_ip:8000. You now have a running server accessible from anywhere! Congrats.

### Notes:
Sometimes your ssh connection will time out and log you off. Just connect again. However:
* make sure to source your virtualenvironment
* you may still have server running the background. You can kill those instance with
```
ps aux | grep python # produce a list of python jobs with job_number
kill -9 job_number
```

## Server Setup
Okay. Now we get to the most difficult part. You will likely run into problems. Sorry.

### Gunicorn Setup
Install gunicorn:
```
pip install gunicorn
```
Now test it:
```
cd ~/workspace/iamsitting_site
gunicorn --bind 0.0.0.0:8000 iamsitting_site.wsgi:application
```

Exit gunicorn. Let's get it as a systemd service:

```
deactivate #to leave virtualenv
sudo vim /etc/systemd/system/gunicorn.service
```

In gunicorn.service, type the following:

```
[Unit]
Description=Gunicorn Application Server handling iamsitting_site
After=network.target

[Service]
User=user #system user name, ubuntu if on aws
Group=www-data
WorkingDirectory=/home/user/path/to/workspace/iamsitting_site
ExecStart=/home/user/path/to/djenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/user/path/to/workspace/iamsitting_site/iamsitting_site.sock iamsitting_site.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```

You can now do these:

```
sudo systemctl start gunicorn
sudo systemctl stop gunicorn
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl status gunicorn
```

### Nginx Setup

Now let's get Nginx going. First install it:
```
sudo apt-get install nginx
```

Perform the following commands to get django to run off of the nginx server:

```
sudo vim /etc/nginx/sites-available/iamsitting_site
```

In the file write:

```
server {

  listen 80;
  server_name (public_ip); #public ipv4 from ec2

  location = /favicon.ico { access_log off; log_not_found off;}
  location /static/ {
    root /home/user/path/to/workspace/iamsitting_site/static;
  }

  location / {
    include proxy_params;
    proxy_pass http://unix:/home/user/path/to/workspace/iamsitting_site/iamsitting_site.sock;
  }
}
```

Now link to sites-enabled:

```
sudo ln -s /etc/ngnix/sites-available/iamsitting_site /etc/ngnix/sites-enabled/iamsitting_site
```

Now include sited-enabled to the conf file

```
sudo vim /etc/ngnix/nginx.conf
```

Change this line:

```
# include /etc/nginx/sites-enabled/*; #commented out
include /etc/nginx/sites-enabled/iamsitting_site
```

Test nginx with:
```
sudo nginx -t
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

In you broweser type your public_ip. Now you have a django website running with gunicorn and nginx. The hardest part is over!
