# Todo Web App

This is a simple Todo web application built using Flask. The application allows users to add, update, and delete tasks. The app is hosted on Render.

# Check it out here!
https://todo-app-flask-g8uk.onrender.com

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Display tasks with their creation time
## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `.env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create the database:
    ```sh
    flask create-db
    ```
## Running the App

1. Start the Flask development server:
    ```sh
    python backend/app.py
    ```

2. Open your web browser and go to `http://localhost:5000`.

## Deployment

The app is hosted on Render. To deploy the app, follow these steps:

1. Create a `Procfile` in the `backend` directory with the following content:
    ```
    web: gunicorn app:app
    ```

2. Push your code to a Git repository.

3. Create a new web service on Render and connect it to your Git repository.

4. Set the build and start commands:
    - Build Command: `pip install -r requirements.txt`
    - Start Command: `gunicorn app:app`

5. Deploy the app.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.    
