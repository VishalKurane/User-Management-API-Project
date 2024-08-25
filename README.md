# User Management API

This project is a REST API built with Flask that provides CRUD operations for managing user data in a Microsoft SQL Server database. The API supports the following operations:

- **GET** `/user` - Retrieve a list of all users or a specific user by `userid` using query parameters.
- **POST** `/user` - Create a new user.
- **PUT** `/user` - Update an existing user by `userid` using query parameters.
- **DELETE** `/user` - Delete a user by `userid` using query parameters.

## Getting Started

### Prerequisites

- Python 3.x
- Microsoft SQL Server
- `pyodbc` library for Python
- `Flask` library for Python

### API Endpoints

- **GET** `/user`
  - **Query Parameters**: `userid` (optional)
  - **Response**: Returns a list of all users or a single user if `userid` is provided.

- **POST** `/user`
  - **Body**: JSON object with the user details:
    ```json
    {
      "username": "Thor",
      "email": "Thor@gmail.com",
      "password_hash": "HammerofThor"
    }
    ```
  - **Response**: Returns the created user object.

- **PUT** `/user`
  - **Query Parameters**: `userid` (required)
  - **Body**: JSON object with the updated user details:
    ```json
    {
      "username": "Thor",
      "email": "Thor@gmail.com",
      "password_hash": "HammerofThor"
    }
    ```
  - **Response**: Returns the updated user object.

- **DELETE** `/user`
  - **Query Parameters**: `userid` (required)
  - **Response**: Returns a success message if the user was deleted.

### Error Handling

- **404 Not Found**: Returned if a user is not found for a given `userid`.
- **400 Bad Request**: Returned if `userid` is missing for PUT or DELETE operations.


