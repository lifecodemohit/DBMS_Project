# DBMS_Project
# Project By : Anmol Singh (2013021) and Mohit Wadhwa (2013063)

Framework : Django 1.6.6
Database : mysql

Problem Statement : 
You want to set up a database company, ArtBase, that builds a product for art galleries. The core of this product is a database with a schema that captures all the information that galleries need to maintain.
Galleries keep information about artists, their names (which are unique), birthplaces, age,and style of art. For each piece of artwork, the artist, the year it was made, its unique title, its type of art (e.g., painting, lithograph, sculpture, photograph), and its price must be stored. Pieces of artwork are also classified into groups of various kinds, for example, portraits, still lifes, works by Picasso, or works of the 19th century; a given piece may belong to more than one group
Each group is identified by a name (like those just given) that describes the group. Finally, galleries keep information about customers. For each customer, galleries keep that person’s unique name, address, total amount of dollars spent in the gallery (very important!), and the artists and groups of art that the customer tends to like.

Folders :
DBMS_PRO : Python script to create database. Change mysql username and password.
art_gallery : Django app.
DBMS_project: Django setup files.

1. Create database by running script in DBMS_PRO.
2. Go to DBMS_project directory from terminal and run "$python manange.py runserver"
3. Go to url "localhost:8000".
