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
    - FRONTEND_BASE_URL: the domain for the frontend application it is need to allow CORS on that domain
    - DATABASES_DEFAULT_ENGINE: production database engine
    - DATABASES_DEFAULT_NAME: production database name
    - DATABASES_DEFAULT_HOST: production database host
    - DATABASES_DEFAULT_USER: production database user
    - DATABASES_DEFAULT_PASSWORD: production database password



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

- `POST /api/v1/token/` - Returns access and refresh token
- `POST /api/v1/token/blacklist/` - Blacklists refresh token
- `POST /api/v1/token/refresh/` - Return new access token
- `GET /api/v1/token/user/` - Returns the currently authenticated user details
