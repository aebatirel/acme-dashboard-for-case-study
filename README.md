# Acme Dashboard Project

## Overview

This project is a dashboard application built for Acme Firm. It consists of a backend built with Python and FastAPI, and a frontend built with Vue.js and Vuetify. The backend serves a REST API that manages restaurant data, and the frontend interacts with this API to display and edit restaurant information. The project also includes Keycloak for authentication.

## Prerequisites

- Docker
- Docker Compose

## Running the Project with Docker Compose

1. **Build and start the containers:**
   ```sh
   docker-compose up --build
   ```

2. **Access the application:**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend: [http://localhost:8000](http://localhost:8000)
   - Keycloak: [http://localhost:8080](http://localhost:8080)

3. **Keycloak Setup:**
   - Log in to the Keycloak admin console with the following credentials:
     - Username: `admin`
     - Password: `admin`
   - The `acme-realm` and `acme-client` should already be set up from the realm import.
   - Registration is enabled, so new users can sign up via the Keycloak login page.

## Backend

### Local Setup

1. **Navigate to the backend directory:**
   ```sh
   cd backend
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```sh
   uvicorn app.main:app --reload
   ```

## Frontend

### Local Setup

1. **Navigate to the frontend directory:**
   ```sh
   cd frontend
   ```

2. **Install the dependencies:**
   ```sh
   npm install
   ```

3. **Run the application:**
   ```sh
   npm run dev
   ```

## License

This project is licensed under the MIT License.
