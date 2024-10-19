# School Management System (Offline-First, Cross-Platform)

This is a comprehensive **School Management System** backend developed with **FastAPI** and **SQLAlchemy**, utilizing **PostgreSQL** as the primary database. The system supports multi-tenant architecture, role-based access control (RBAC), and offline-first capabilities with local storage. It is designed to scale and handle the management of multiple schools with specific user roles, including Super Admins, School Admins, Teachers, Parents, and Students.

## Key Features
- **Offline-First**: Local storage with bi-directional synchronization.
- **Role-Based Access Control (RBAC)**: Fine-grained permission control for different user roles.
- **Multi-Tenant Architecture**: Isolated data for each school (tenant) with tenant-specific roles and permissions.
- **User Authentication & Authorization**: Secure JWT-based authentication with optional Multi-Factor Authentication (MFA).
- **Audit Logs**: Tracks key actions for security and compliance.
- **Payments**: Integration with payment gateways (e.g., Flutterwave, Paystack) for subscription and other school payments.
- **Real-Time Notifications**: Push notifications and announcements using WebSockets or Server-Sent Events (SSE).

## Table of Contents
1. [Installation](#installation)
2. [Environment Variables](#environment-variables)
3. [Running the Application](#running-the-application)
4. [API Routes](#api-routes)
5. [Data Models](#data-models)
6. [Offline Functionality](#offline-functionality)
7. [Testing](#testing)
8. [Contributing](#contributing)
9. [License](#license)

---

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL (as the primary database)
- SQLite (for offline functionality)
- Git

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/splenwilz/schoolnify.git
    cd schoolnify
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create the PostgreSQL database**:
    ```sql
    CREATE DATABASE schoolnify;
    ```

5. **Run the application** (see next section for details).

## Environment Variables

You need to configure environment variables for database connections, API keys, and other configurations. Create a `.env` file in the project root with the following:

```env
DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=localhost
DB_NAME=schoolnify
SQLITE_DB_PATH=./local_offline_storage.db  # Path for local SQLite database
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
FLUTTERWAVE_API_KEY=your_flutterwave_key
PAYSTACK_API_KEY=your_paystack_key
```

- **DB_USER**: PostgreSQL database username.
- **DB_PASS**: PostgreSQL database password.
- **SQLITE_DB_PATH**: Path to the local SQLite database for offline storage.
- **SECRET_KEY**: Secret key for JWT token signing.
- **ACCESS_TOKEN_EXPIRE_MINUTES**: JWT token expiration time (in minutes).
- **FLUTTERWAVE_API_KEY**: API key for Flutterwave payment gateway.
- **PAYSTACK_API_KEY**: API key for Paystack payment gateway.

## Running the Application

To start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application will start at `http://127.0.0.1:8000`. You can access the interactive API documentation at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Routes

### Authentication and Authorization
- **POST** `/api/auth/register`: Register a new school (self-registration).
- **POST** `/api/auth/login`: Authenticate a user and issue JWT.
- **POST** `/api/auth/logout`: Invalidate the JWT token.
- **POST** `/api/auth/mfa/setup`: Setup Multi-Factor Authentication (MFA).
- **POST** `/api/auth/mfa/verify`: Verify MFA during login.

### Super Admin Routes
- **GET** `/api/superadmin/users`: Retrieve all users across tenants.
- **POST** `/api/superadmin/users`: Create a new user with any role.
- **GET** `/api/superadmin/roles`: List all global roles.
- **POST** `/api/superadmin/roles`: Create a new global role.

### School Admin Routes
- **GET** `/api/schools/:schoolId/users`: List all users in the school.
- **POST** `/api/schools/:schoolId/users`: Invite a new user.
- **GET** `/api/schools/:schoolId/roles`: List roles within the school.
- **POST** `/api/schools/:schoolId/roles`: Create a new role for the school.

### Classes and Assignments
- **GET** `/api/classes`: List all classes.
- **POST** `/api/classes`: Create a new class.
- **GET** `/api/assignments`: List all assignments.
- **POST** `/api/assignments`: Create a new assignment.
- **POST** `/api/assignments/:assignmentId/submissions`: Submit an assignment.


## Offline Functionality

The system supports **offline-first** capabilities through local storage using SQLite. This allows users (e.g., Teachers) to continue working without internet connectivity. Synchronization occurs once the connection is restored.

- **Local Storage**: SQLite is used for offline access to user data, assignments, attendance records, etc.
- **Data Synchronization**: Upon re-connection, data is synchronized between the local SQLite database and the central PostgreSQL database using a last-write-wins strategy or manual conflict resolution.

## Testing

To run tests:

```bash
pytest
```

Ensure that the environment variables for the test database are set up correctly.

## Contributing

Contributions are welcome! Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.