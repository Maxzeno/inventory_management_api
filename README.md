## Setup

#### Setup for Online Store Inventory and Supplier Management API

1. **Install Required packages**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Set environment variables (can be added to .env file)**:
    ```bash
    SECRET_KEY=
    DEBUG=
    TRY_LOCAL_DB=
    ALLOWED_HOST=
    FRONTEND_BASE_URL=
    DATABASES_DEFAULT_ENGINE=
    DATABASES_DEFAULT_NAME=
    DATABASES_DEFAULT_HOST=
    DATABASES_DEFAULT_PORT=
    DATABASES_DEFAULT_USER=
    DATABASES_DEFAULT_PASSWORD=
    ```

    ### Find examples in env_examples.txt file at the root of the project 

    - SECRET_KEY: text - used as django secret key and is required
    - DEBUG: options (true, false) - used to set django debug mode by default is false
    - TRY_LOCAL_DB: options (true, false) - if true the local sqlite database will be used else the production database will be used but the environments variables for it has to be set
    - ALLOWED_HOST: django allowed host options useful in production, it is a list separated by space eg. domain1.com domain2.com
    - FRONTEND_BASE_URL: the domain for the frontend application if any it is needed to allow CORS on that domain
    - DATABASES_DEFAULT_ENGINE: production database engine (required in production - when DEBUG is true)
    - DATABASES_DEFAULT_NAME: production database name (required in production - when DEBUG is true)
    - DATABASES_DEFAULT_HOST: production database host (required in production - when DEBUG is true)
    - DATABASES_DEFAULT_USER: production database user (required in production - when DEBUG is true)
    - DATABASES_DEFAULT_PASSWORD: production database password (required in production - when DEBUG is true)

3. **Migrate the database**:
    ```bash
    python manage.py migrate
    ```

4. **Collect static (required if debug with be set to false)**:
    ```bash
    python manage.py collectstatic
    ```

5. **Create Superuser so you can login to the dashboard**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server**:
    ```bash
    python manage.py runserver
    ```


## API usage

### Swagger documentation for the API /api/v1/docs/

### Endpoints

Sure! Here is the documentation for each endpoint based on your structure:

### Items

- `GET /api/v1/items/`
  - **Description**: Retrieves a list of items (has filters like supplier).
  - **Response**: List of items.
  
- `POST /api/v1/items/`
  - **Description**: Creates a new item.
  - **Request Body**: Item details (e.g., name, description, price).
  - **Response**: Created item details.
  
- `GET /api/v1/items/{id}/`
  - **Description**: Retrieves details of a specific item by ID.
  - **Path Parameter**: `id` - ID of the item.
  - **Response**: Item details.
  
- `PUT /api/v1/items/{id}/`
  - **Description**: Updates a specific item by ID.
  - **Path Parameter**: `id` - ID of the item.
  - **Request Body**: Updated item details.
  - **Response**: Updated item details.
  
- `PATCH /api/v1/items/{id}/`
  - **Description**: Partially updates a specific item by ID.
  - **Path Parameter**: `id` - ID of the item.
  - **Request Body**: Partial item details to be updated.
  - **Response**: Updated item details.
  
- `DELETE /api/v1/items/{id}/`
  - **Description**: Deletes a specific item by ID.
  - **Path Parameter**: `id` - ID of the item.
  - **Response**: Confirmation of deletion.

### Suppliers

- `GET /api/v1/suppliers/`
  - **Description**: Retrieves a list of suppliers.
  - **Response**: List of suppliers.
  
- `POST /api/v1/suppliers/`
  - **Description**: Creates a new supplier.
  - **Request Body**: Supplier details (e.g., name, contact information).
  - **Response**: Created supplier details.
  
- `GET /api/v1/suppliers/{id}/`
  - **Description**: Retrieves details of a specific supplier by ID.
  - **Path Parameter**: `id` - ID of the supplier.
  - **Response**: Supplier details.
  
- `PUT /api/v1/suppliers/{id}/`
  - **Description**: Updates a specific supplier by ID.
  - **Path Parameter**: `id` - ID of the supplier.
  - **Request Body**: Updated supplier details.
  - **Response**: Updated supplier details.
  
- `PATCH /api/v1/suppliers/{id}/`
  - **Description**: Partially updates a specific supplier by ID.
  - **Path Parameter**: `id` - ID of the supplier.
  - **Request Body**: Partial supplier details to be updated.
  - **Response**: Updated supplier details.

### Auth

- `POST /api/v1/token/`
  - **Description**: Returns access and refresh token.
  - **Request Body**: User credentials (e.g., email, password).
  - **Response**: Access and refresh tokens.
  
- `POST /api/v1/token/blacklist/`
  - **Description**: Blacklists a refresh token, effectively logging out the user.
  - **Request Body**: Refresh token.
  - **Response**: Confirmation of token blacklisting.
  
- `POST /api/v1/token/refresh/`
  - **Description**: Returns a new access token using a refresh token.
  - **Request Body**: Refresh token.
  - **Response**: New access token.

### User

- `GET /api/v1/token/user/`
  - **Description**: Retrieves details of the authenticated user.
  - **Response**: User details.
  
- `PATCH /api/v1/token/user/`
  - **Description**: Partially updates details of the authenticated user.
  - **Request Body**: Partial user details to be updated.
  - **Response**: Updated user details.
