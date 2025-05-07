# Task Tracker

## Installation

To set up the Task Tracker project, follow these steps:

1. Clone the repository:

```
git clone https://github.com/KapHullloK/taskTracker.git
```

2. Navigate to the project directory:

```
cd taskTracker
```

3. Set up the environment variables:
    - Create a `.env` file in the project root directory.
    - Add the necessary environment variables, such
      as `SECRET_KEY`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `HOST`, and `POSTGRES_PORT`.


4. You must have Docker. Run the Docker commands:

```
docker compose build
docker compose up
```

The application should now be running at `http://localhost:8000`.

## Usage

The Task Tracker application provides the following functionality:

- **Task Management**: Users can create, view, update, and delete tasks.
- **Task Status**: Tasks can have different statuses, such as "created", "in_progress", and "completed".
- **Task Dependencies**: Tasks can have parent-child relationships, allowing for the management of task dependencies.
- **Task Assignments**: Tasks can be assigned to specific users as performers.
- **Access Control**: The application has different access levels (superuser, staff, and regular users) with
  corresponding permissions.

To use the application, you can interact with the provided API endpoints using a tool like Postman or by building a
frontend application.

## API

The Task Tracker application exposes the following API endpoints:

### Tasks

- `GET /tasks/`: List all tasks
- `GET /tasks/<int:pk>`: Retrieve a specific task
- `POST /tasks/create/`: Create a new task
- `PUT /tasks/update/<int:pk>`: Update a task
- `DELETE /tasks/delete/<int:pk>`: Delete a task
- `GET /tasks/important/`: List important tasks (tasks with status "created" and a parent task with status "
  in_progress")

### Users

- `POST /users/register/`: Register a new user
- `GET /users/`: List all users
- `GET /users/<int:pk>`: Retrieve a specific user
- `PUT /users/update/<int:pk>`: Update a user
- `DELETE /users/delete/<int:pk>`: Delete a user
- `GET /users/tasks/`: List all users with their task counts
- `GET /users/candidate/`: List candidate users for important tasks
