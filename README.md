# N2Task
Case Study for N2Mobiles

## Installation
The installation assumes you are using MacOS or a Linux distribution. If you are using Windows please use the correct commands for Windows.

1. Install PostgreSQL to your device.
2. Create a new PostgreSQL server with the following information.
    - The server should be on the port 5454.
    - Make sure the default database 'postgres' exists on the server.
    - Create a user for the database with the following credentials:
        - name: n2admin
        - password: 123123
3. Make sure the server is running on localhost.
4. Clone the repository to your device.
5. Create a python virtual env.
```bash
python3 -m venv ./venv
```
6. Activate the virtual environment.
```bash
source venv/bin/activate
```
7. Install required packages.
```bash
pip install -r requirements.txt
```
8. Make Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
9. Run the Django REST application.
```bash
python manage.py runserver
```
10. Open the link provided in the console in a web browser.

## Postman Collection
Postman Collection is provided for basic test cases in the n2postman.json file. You can import it from Postman