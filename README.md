* Python 3.10.5 [Download and install](https://www.python.org/downloads/), ensure python is in the PATH for windows
* Nodejs v16.13.0 [Download and install](https://nodejs.org/ru/blog/release/v16.13.0/)
* Sqlite 3.39.5 [Download and install](https://www.sqlite.org/download.html), ensure sqlite is in the PATH for windows

For Windows open the cmd and go to the project folder

Create a virtual environment with 
```
python3 -m venv c:\path\to\your\project\env_name
```

Activate the environment
```
env_name\Scripts\activate.bat
```

With the command line enter inside the test folder 
```
cd test
```

Install the packages in the requirements.txt file with the command:
```
pip install -r requirements.txt
```

To run the django server use the command, this command should create a db.sqlite3 file
```
python manage.py runserver
```

Open another cmd and go to the project folder where the package.json is located and run
```
npm i
```

To compile the assets use
```
npm run dev
```

To compile while working use
```
npm run watch
```

Run the command to create the migrations
```

```

Run the command to apply the migrations
```

```

When the database has been created run the command seed_db to populate with initial data
```
python manage.py seed_db
```
