# PersonalCard REST API

## Setup steps:
1. Clone the repository
2. Install packages from requirements.txt(pip install -r requirements.txt)
3. From the project root directory run:
    ```python3 manage.py migrate```. It will create an SQLite database in 
   project root directory.

## How to run
To run the server, execute the following command from the project root

```python3 manage.py runserver```

To test it, open the following URL in your browser:
```http://127.0.0.1:8000/api/personal_card```


## Description
It supports 2 methods: GET for retrieving all cards(paginated by 
10 card per page) and POST for creating new cards.
If the given information from the POST request is already in the DB,
that instance of personal card is returned with its corresponding ID.
Personal Cards do have their unique IDs, but in POST request they are 
identified by all their fields together.
This can be easily changed so that the card is identified by, for example 
combining its name, surname, middle name and age and gender but that rises a 
question what to do in POST request if the DB says the person is vaccinated, 
but the POST says it is not. 


## Testing
To test the app, there is an exported Postman collection.
Import it into Postman, set the base_url variable in collection variables if 
you host the server in any way different from its default way and run the 
requests.


