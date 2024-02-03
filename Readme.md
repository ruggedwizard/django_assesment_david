# Running the code locally
Clone the repository 
``` 
git clone repository_url
```

>[!NOTE]
>This steps are for windows OS
Create a python virtual environment, activate the python virtual environment and install the project dependencies in requiremnts file

``` 
python -m venv venv 
```

activate the virtual environment 
```
\venv\scripts\activate
```

install the requirments package using pip
```
pip install -r requirements.txt
```
run migrations
```
python manage.py migrate
```

run local server
```
python manage.py runserver
```


# Authentication 
Creating an Account:
A POST Request to 
```
{{BASE_URL}}/register/
```
it takes an input with 2 fields username and password an, exmaple imput below, and output shown below
```
input:
{
    "username":"example_username",
    "password":"example_password"
}

output:
{
    "username":"example_username"
}

example error output:
{
    "username": [
        "A user with that username already exists."
    ]
}

```
Acquiring Access Tokens and Refresh Tokens
```
{{BASE_URL}}/api/token/
```
it takes an input with 2 fields username and password, an example input and output are shown below
```
example input:
{
    "username":"example_username",
    "password":"example_password"
}

example output:
{
    "refresh": "example_refresh_token",
    "access": "example_access_token"
}

```
>[!NOTE]
>LIFESPAN OF TOKENS, ACCESS_TOKEN = 60 minutes, REFRESH_TOKEN = 1 Day
>the token can be blacklisted and refreshed

# API USEAGE 
## EXPENSE ENDPOINT
To Create an Expense Record, 
```
MAKE A POST REQUEST TO:
{{BASE_URL}}/expenses/
```
with the following input example
```
{
    "amount":example_float,
    "description":"example_string",
    "category":"FOOD"
}
Options for category are:
[FOOD, DATA, TRANSPORT and MISCELLANEOUS]
```
To view all expenses
MAKE A GET REQUEST TO:
```
{{BASE_URL}}/expenses/
```

### TO VIEW A SINGLE EXPENSE, UPDATE AND DELETE EXPENSE
>[!NOTE]
>ONLY THE USER THAT CREATED THE EXPENSE CAN VIEW, UPDATE AND DELETE THE EXPENSE RECORD 
GET A SINGLE EXPENSE 
```
SEND A GET REQUEST TO:
{{BASE_URL}}/expenses/expenses_id/
```

UPDATE A SINGLE EXPENSE RECORD
```
SEND A PUT REQUEST TO:
{{BASE_URL}}/expenses/expenses_id/
```

DELETE AN EXPENSE RECORD
```
SEND A DELETE REQUEST TO :
{{BASE_URL}}/expenses/expenses_id/
```

## BUDGET ENDPOINT
To Create an Budget Record, 
```
MAKE A POST REQUEST TO:
{{BASE_URL}}/budget/
```
with the following input example
```
{
    "amount":example_float,
    "description":"example_string",
    "category":"FOOD"
}
Options for category are:
[FOOD, DATA,SAVINGS, TRANSPORT and MISCELLANEOUS]
```
To view all budgets
MAKE A GET REQUEST TO:
```
{{BASE_URL}}/budget/
```

### TO VIEW A SINGLE BUDGET, UPDATE AND DELETE BUDGET
>[!NOTE]
>ONLY THE USER THAT CREATED THE BUDGET CAN VIEW, UPDATE AND DELETE THE BUDGET RECORD 
GET A SINGLE BUDGET 
```
SEND A GET REQUEST TO:
{{BASE_URL}}/budget/budget_id/
```

UPDATE A SINGLE BUDGET RECORD
```
SEND A PUT REQUEST TO:
{{BASE_URL}}/budget/budget_id/
```

DELETE AN BUDGET RECORD
```
SEND A DELETE REQUEST TO :
{{BASE_URL}}/budget/budget_id/
```
### JWT AUTHENTICATION PROCESS
The JWT AUTHENTICATION Takes the Username, and User ID and saves it as a payload data, to generate an Access token and a refresh token
```
ACCESS TOKEN
A POST REQUEST TO THIS ENDPOINT:
{{BASE_URL}}/api/token/
```
WITH

```
example input:
{
    "username":"example_username",
    "password":"example_password"
}
```

GIVES
```
example output:
{
    "refresh": "example_refresh_token",
    "access": "example_access_token"
}
```
the access tokens spans for 60 minutues to allow user navigate through the API Routes, after 60 minuetes its becomes void and we use the refresh token 
to get another access token, which will span for another 60 minutes. 

### REFRESH THE TOKEN 
we make a POST request to :
```
{{BASE_URL}}/api/token/refresh/
```
WITH 
```
example input
{
    "refresh":"example_refesh_token_that_is_valid"
}
```

WHICH GIVES:
{
    "access":"example_access_token_for_the_next_60_minutes"
}

>[!NOTE]
>THE REFRESH TOKEN WILL SPAN FOR ONLY 24 Hours, For Security Reasons