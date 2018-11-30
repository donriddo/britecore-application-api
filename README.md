#BRITECORE ENGINEERING APPLICATION

Running on [Python3.6.0]

Server instance launched on AWS Lambda with Zappa
(https://hsttpx65oi.execute-api.us-west-2.amazonaws.com/dev/)

Vue Frontend running at (https://britecore-insurance.surge.sh)

1. Clone repository and `cd` into the project

2. Install requirements
`pip install -r requirements.txt`

3. Run migrations
`python manage.py migrate`

4. Launch server
`python manage.py runserver`

#Approach to solving the problem

1. Have a table RiskField that stores
  - field name
  - field type
  - field default value
  - field choices if type == enum

2. Have another table RiskType that stores
  - risk name
  - risk type: e.g property
  - risk fields: ManyToMany field of RiskField objects

3. Have another table Risk that stores submitted generated data from the form
  - json_body: text field storing the JSON stringified object