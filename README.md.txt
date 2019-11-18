#  GET STARTED WITH DJANGO   

##  INTRO 

Django is a Web framework written in Python. A Web framework is a software that supports
the development of dynamic Web sites, applications, and services.

Django is one of the most popular Web frameworks written in Python. It provides a set
of tools and functionalities that solves many common problems associated with Web
development, such as security features, database access, sessions, template processing,
URL routing, internationalization, localization, and much more.

## INSTALLATION

### Python

```python
python --version
```

### Virtualenv

Each project you develop will have its isolated environment

#### PIP

 [How to install PIP](https://www.liquidweb.com/kb/install-pip-windows/) 


#### Virtualenv

```python
sudo pip3.6 install virtualenv
```


 
### Django

From now on, everything we install, including Django itself, will be installed inside a Virtual Environment.

#### Create project folder

```bas
mkdir shell_testProject
cd shell_testProject
```




#### Create and activate virtual environment

```python
virtualenv venv -p python3.6
source venv/bin/activate
```


#### Install Django

```python
pip install django
```



##  STARTING A NEW PROJECT

```pyth
django-admin startproject testProject
python manage.py runserver
```
	

## CLONING AFRO_ED REPO

```pyth
git clone https://github.com/meite-root/afro_ed.git
sudo apt install libpq-dev
pip install -r requirements.txt
# Install whatever module is required
python manage.py migrate
python manage.py runserver
```



# PYTHON/DJANGO/ LOCAL CODES 

```python
atom new newfile.txt        # Create new file (with atom editor)
nano new newfile.txt        # Create new file (with nano editor)

pip freeze                       # check the currently installed Python libraries

python manage.py runserver       # Launch server
python manage.py createsuperuser # Create super user


```
                                        
### Python Shell

```pyt
Open Shell                                 # python manage.py shell
Import a class (Boards in this case)       # from boards.models import Board
Create an object without saving	           # board = Board()
Save an object (create or update)	       # board.save()
Create and save an object in the database  # Board.objects.create(name='...', description='...')
List all objects                           # Board.objects.all()
Get a single object, identified by a field # Board.objects.get(id=1) 
Close Shell                                # exit()

```



#  USE GIT 

### Great summary

[Git-guide](https://rogerdudler.github.io/git-guide/)


### Git official documentation

[Documentation](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
  
        

### Quick commands

```python
git init                                # Initialize repository (once in folder)

git config --global user.name "myname"  # set main user name
git config --global user.email "myemail"# set main user email

git remote add origin (https://github.com/exp/exp) # Connect to a remote repo (origin could be any name)
git push origin master                  # Push latest (commit) to defined remote repo
git push                                # Push latest (commit) to remote repo
git pull                                # Pull latest (commit) to remote repo

git clone (https://github.com/exp/exp)  # clone online repository
git status                              # checks if there's sanything to commit
git add .                               # Add any changes made to the folder
git add (new-file)                      # Add file indicated
git commit -m (name_of_the_new_commit)  # save a new commit/ version
git log            (+ Q to exit)        # See commit history ( Head is the latest commit)

git checkout (commitID)                 # back to commit pointed (which is ejected from the master branch for that purpose)
git reset --hard (commitID)             # back to commit pointed ( any commit after that is deleted)
git checkout -- .                       # revert all unstaged (uncommitted) changes and get back to last commit

git branch                              # checkout which branches are here and which one you are in
git checkout -b (New-branch-name)       # Create new branch 
git checkout (branch-name)              # swich to other branch
git merge (New-branch-name)             # merges to master branch
git branch -D (branch-name)             # Deletes branch


```



### How to make a clean pull request (Contribute to someone's repository)

https://gist.github.com/MarcDiethelm/7303312
https://kbroman.org/github_tutorial/pages/fork.html

Both are complementary