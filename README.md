# Gaido
A Japanese tourism site where writers can write about travel-related topics, and provide real experiences to enhance people's travels. The production version is altered.

## Installing packages
Python packages that are used in this project are listed as below:
+ Django
+ Markdown
+ Pillow
+ and more upcoming...

To install the packages, run ``pip install -r requirements.txt`` to install the packages (Not yet implemented.)
Make sure to run the project in a *VirtualEnv* if you are only testing it out on your own.

## Starting the Local Server
The boot the local server, run ``python manage.py runserver`` in the main repository.

The website runs on a local server in the port ``http://127.0.0.1:8000`` on your computer. To access the page, enter the url and the page should appear.

## Migration when Testing
When you are testing out features or modifying the code, you may want to make changes to the model. When this occurs, *migrations* within *Django* have to be made to the database.

    python manage.oy makemigrations <app>
    > files are added to the migration, you can specify the main app 'Gaido' when doing migrations, or leave it blank
    python manage.py migrate
    > migration is made
    
    python manage.py runserver
    > boots server with changes
