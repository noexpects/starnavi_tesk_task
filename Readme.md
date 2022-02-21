## **Task Description**

### **Social Network**
Object of this task is to create a simple REST API. You can use one framework from this list
(Django Rest Framework, Flask or FastAPI) and all libraries which you are prefer to use with
this frameworks.

### **Basic models:**
- User
- Post (always made by a user)

### **Basic Features:**
- user signup

- user login

- post creation

- post like

- post unlike

- analytics about how many likes was made. Example url
/api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics
aggregated by day.

- user activity an endpoint which will show when user was login last time and when he
mades a last request to the service.


### **Requirements:**
- Implement token authentication (JWT is prefered)

## **Endpoints:**

### **Users:**
- GET api/v1/users/ - Get list of all users
- GET api/v1/users/<user_ID>/ - Get single user by ID
- GET api/v1/users/<user_ID>/activity/ - Get user activity
- POST api/v1/users/ - Create user
- PATCH api/v1/users/<user_ID>/ - Update user
- DELETE api/v1/users/<user_ID>/ - Delete user by ID

### **Posts:**
- GET api/v1/posts/ - Get list of all posts
- GET api/v1/posts/<post_ID>/ - Get single post by ID
- GET api/v1/posts/<post_ID>/upvote/ - Upvote post
- GET api/v1/posts/<post_ID>/retract_upvote/ - Retract upvote
- POST api/v1/posts/ - Create post
- PATCH api/v1/posts/<user_ID>/ - Update post
- DELETE api/v1/posts/<user_ID>/ - Delete post by ID

### **Service:**
- GET api/v1/analytics/?date_from&date_to - Get upvotes analytic for date range
- POST api/v1/token/ - Get JWT token
- POST api/v1/token/refresh/ - Refresh JWT token
## **Steps to run project with Docker:**

- Clone this repository.
- Open CMD in project's folder
- Run next commands:
    1. docker-compose build
    2. docker-compose up
    3. docker-compose exec web python manage.py migrate
    4. docker-compose exec web python manage.py createsuperuser

## **[Link to Postman collection](https://www.getpostman.com/collections/228d4fa31548e09f21d9)**

### P.S.
Use StarNavi_TestTask.env.postman_environment.json file to create an enviroment for provided Postman collection.
