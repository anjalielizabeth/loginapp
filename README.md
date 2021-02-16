# Login App

This projects create simple login/registration application.This project make use of python,flask,mysql.

## Getting Started

1. Clone this repository.
2. From the root of the project run `pip install -r requirements.txt`
3. Copy the sql data from `db_scripts/data.sql` and paste it into MySQL Workbench and execute the queries.
4. Open app.py in an editor and edit the below settings as per your enviornment.
````
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'loginapp'
````

5. From the project root run `python app.py`
6. Load `http://localhost:5000` on your browser. You should see a login page. 




### Prerequisites
1. Python 2.7 should be installed.
2. MySQL database should be installed.

## Example Screenshots

![Alt text](screens/1.png?raw=true "Optional Title")
![Alt text](screens/2.png?raw=true "Optional Title")
![Alt text](screens/3.png?raw=true "Optional Title")
![Alt text](screens/4.png?raw=true "Optional Title")
![Alt text](screens/5.png?raw=true "Optional Title")
