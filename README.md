## Running Fridge MVP
Running Fridge MVP is a simple yet effective tool designed to help users track their refrigerator inventory effortlessly. Here's what it offers:
User Registration and Authentication: Users can sign up and log in to the Running Fridge platform, ensuring secure access to their inventory.
Inventory Management: Users can add, update, find, and delete items within five essential categories: beverages, dairy, grains, produce, and proteins.
With these core features, Running Fridge MVP provides a straightforward solution for managing refrigerator inventory, catering to the essential needs of users without unnecessary complexity.
## Team
-   Bradley Mendel
-   Deane Logan
-   Trevor Venditti
-   Brittany Robarge
## Design
The Running Fridge backend uses MongoDB/FastAPI and is comprised of four main components: models, queries, routes, and authorization.
Backend:
Models: Define the categories for incoming and outgoing data.
Queries: Implement functions to process data for the frontend.
Routes: Configure routes for frontend interaction with the query functions.
Authorization: Handles user sign-up, login, and token tracking to secure the website through JWTDown library, granting users access only to the data they input.
Frontend: Using React/Redux we created a display for the users browser to navigate through our UI. Connecting our pages folder to our main jsx to create a SPA. Our app folder contains all of our slices, and store which control the state, and manipulation of I/O data for accounts, and item categories. For styling animation we used Tailwindcss, DaisyUI, LucideReact, and framer-motion.
## Integration - How we put the "team" in "team"
At Running Fridge, we prioritize seamless collaboration and integration across our categories to ensure efficient inventory management. While each category—beverages, dairy, grains, produce, and proteins—functions independently to track inventory within its domain, our accounts and authorization systems play a crucial role in facilitating communication and coordination among these categories.
Stand-Alone Categories: Our beverages, dairy, grains, produce, and proteins categories operate autonomously, focusing on tracking inventory within their respective domains. This streamlined approach allows for specialized management tailored to each category's unique requirements.
Accounts and Authorization: The accounts and authorization systems serve as the central hub connecting our users with the various categories. Users must be signed up and logged in to input or manipulate data within the system. This integration ensures that only authenticated users have access to the inventory management functionalities across all categories.
By maintaining a cohesive approach to integration, we ensure that the Running Fridge platform operates seamlessly, empowering users to efficiently manage their refrigerator inventory while upholding security and user privacy standards.
## Getting Started
## Install Extensions
-   Prettier: <https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode>
-   Black Formatter: <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>
**Make sure you have Docker, Git, and Node.js 18.2 or above**
1. Fork this repository
2. Clone the forked repository onto your local computer:
   git clone <<https://gitlab.com/12tier/running-fridge.git>>
3. Git checkout to working repository "name"
4. Generate a hexidecimal key and assign it as the value for SIGNING_KEY in the .env file
5. Build and run the project using Docker with these commands:
```
docker volume create mongo-data
docker volume create mongo-express
docker volume create running-fridge
docker-compose build
docker-compose up
```
-   After running these commands, make sure all of your Docker containers are running
## Accessing Endpoints to Send and View Data: Access Through Swagger and view data through Swagger or Mongo-Express
To streamline data management and facilitate interaction with the Running Fridge database, we provide convenient access points through Swagger and Mongo-Express.
Swagger
All endpoints for sending and retrieving data can be accessed via Swagger at http://localhost:8000/docs#/. Through this intuitive interface, users can seamlessly input data into the database and view existing entries.
Mongo-Express
For comprehensive insights into the database, including viewing all inputs and additional information, navigate to http://localhost:8081/ using your preferred web browser. Upon accessing Mongo-Express, log in with the following credentials:
Username: admin
Password: pass
To access the front end, input http://localhost:5173/ into your browser
## Accessing Endpoints to Send and View Data:
Access through Swagger & Your Browser (I/O will be structured the same throughout all Item categories).
## CRUD for Item Categories
# Beverages
| Action | Method | URL
| ----------- | ----------- | ----------- |
| List all items in beverages | GET | http://localhost:8000/api/beverages/beverages/mine
| Create an item for beverages | POST | http://localhost:8000/api/beverages/beverages
| Get details of beverage | GET | http://localhost:8000/api/beverages/beverages/{item_id}
| Update a specific beverage | PUT | http://localhost:8000/api/beverages/beverages/{item_id}
| Delete a specific beverage | DELETE | http://localhost:8000/api/beverages/beverages/{item_id}
# Dairies
| Action | Method | URL
| ----------- | ----------- | ----------- |
| List all items in dairies| GET | http://localhost:8000/api/dairies/dairies/mine
| Create an item for dairy | POST | http://localhost:8000/api/dairies/dairies
| Get details of dairy | GET | http://localhost:8000/api/dairies/dairies/{item_id}
| Update a specific dairy | PUT | http://localhost:8000/api/dairies/dairies/{item_id}
| Delete a specific dairy | DELETE | http://localhost:8000/api/dairies/dairies/{item_id}
# Grains
| Action | Method | URL
| ----------- | ----------- | ----------- |
| List all items in grains| GET | http://localhost:8000/api/grains/grains/mine
| Create an item for grain | POST | http://localhost:8000/api/grains/grains
| Get details of grain | GET | http://localhost:8000/api/grains/grains/{item_id}
| Update a specific grain | PUT | http://localhost:8000/api/grains/grains/{item_id}
| Delete a specific grain | DELETE | http://localhost:8000/api/grains/grains/{item_id}
# Produce
| Action | Method | URL
| ----------- | ----------- | ----------- |
| List all items in produce| GET | http://localhost:8000/api/produce/produce/mine
| Create an item for produce | POST | http://localhost:8000/api/produce/produce
| Get details of produce | GET | http://localhost:8000/api/produce/produce/{item_id}
| Update a specific produce | PUT | http://localhost:8000/api/produce/produce/{item_id}
| Delete a specific produce | DELETE | http://localhost:8000/api/produce/produce/{item_id}
# Proteins
| Action | Method | URL
| ----------- | ----------- | ----------- |
| List all items in proteins| GET | http://localhost:8000/api/proteins/proteins/mine
| Create an item for protein | POST | http://localhost:8000/api/proteins/proteins
| Get details of protein | GET | http://localhost:8000/api/proteins/proteins/{item_id}
| Update a specific protein | PUT | http://localhost:8000/api/proteins/proteins/{item_id}
| Delete a specific protein | DELETE | http://localhost:8000/api/proteins/proteins/{item_id}
## Input JSON Body for any Items category example
{
"name": "Sunny-D",
"cost": "4.00",
"expiration_date": "2024-03-21",
"measurement": "1 Gallon",
"store_name": "Walmart"
}
## Output JSON Body for any Items category example
{
"id": "65fc64ac2909181b65116887",
"account_id": "65fc64a62909181b65116883",
"name": "Sunny-D",
"cost": "4.00",
"expiration_date": "2024-03-21",
"measurement": "1 Gallon",
"store_name": "Walmart"
}
ID is unique to every product inputted and is used to manipulate data when the user wants. Account_id is unique to every user and is what restricts every user to their own data. Name is used to name the item being added to inventory. Cost is used to add the cost of the item being added to inventory. Expiration date is used to input the date the item is set to expire helping the customer keep track of items expiration. Measurement is used to input the quantity of item in inventory. Store name is used to keep track of where customer bought the item.
//////////////
# CRUD for Sign Up
| Action | Method | URL
| ----------- | ----------- | ----------- |
| Create an account | POST | http://localhost:8000/api/auth/accounts
## SignUp inputs JSON Body example
{
"username": "string",
"password": "string",
("password": "string")---optional on backend, required on front end
}
## SignUp outputs JSON Body example
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxM2I5YjZmMC03ZTYzLTRjODktYWNlMS0wZTAyNTY3YzQ3NjgiLCJleHAiOjE3MTExNDM4OTEsInN1YiI6InN0cmluZyIsImFjY291bnQiOnsiaWQiOiI2NWZkZWQ3YWNiNzBjYWEwYjQ1MTNhY2YiLCJ1c2VybmFtZSI6InN0cmluZyJ9fQ.7P9uOO_PHxg-hh59QsKbwK2rJrBr3FFfbXhdBAlVYB0",
  "token_type": "Bearer",
  "account": {
    "id": "65fdedc3cb70caa0b4513ad3",
    "username": "string"
  }
}
# CRUD for Login
| Action | Method | URL
| ----------- | ----------- | ----------- |
| Log into account | POST | http://localhost:8000/token
## Login inputs JSON Body example
{
"username": "string",
"password": "string",
}
## Login outputs JSON Body example
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0MDU2ZmEyOC01NDM0LTQzODctOTBlMy04YjQ1MTJkMDc3OTAiLCJleHAiOjE3MTExNDU1OTMsInN1YiI6InQiLCJhY2NvdW50Ijp7ImlkIjoiNjVmZGU5MDJjYjcwY2FhMGI0NTEzYWMyIiwidXNlcm5hbWUiOiJ0In19.sryNPSkptrNXXTnA85cVpVHBIzqEY58sppTa6o2KYTs",
  "token_type": "Bearer"
}
