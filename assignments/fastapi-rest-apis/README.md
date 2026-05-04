# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create a REST API using FastAPI by defining routes, validating request data, and implementing simple CRUD operations.

## 📝 Tasks

### 🛠️ Create the FastAPI Application and Basic Endpoints

#### Description
Set up a FastAPI app and add basic endpoints to return JSON responses.

#### Requirements
Completed program should:

- Create a `FastAPI()` app instance.
- Add a root endpoint at `/` that returns a welcome message.
- Add a GET endpoint at `/items/{item_id}` that returns item details.
- Return JSON data using Python dictionaries.

### 🛠️ Add Request Validation and Query Parameters

#### Description
Define a Pydantic model for request validation and accept query parameters for a search endpoint.

#### Requirements
Completed program should:

- Create a `BaseModel` class for item data.
- Accept request body data in a POST endpoint.
- Accept an optional query parameter on a GET endpoint.
- Return the validated request data in the response.

### 🛠️ Implement In-Memory CRUD Operations

#### Description
Build simple create, read, update, and delete endpoints using an in-memory data store.

#### Requirements
Completed program should:

- Use an in-memory dictionary or list to store items.
- Implement POST, GET, PUT, and DELETE endpoints for items.
- Return `HTTPException` with status code `404` when an item is not found.
- Demonstrate correct responses for creating, updating, and deleting items.
