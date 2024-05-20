# Acme Dashboard Project

## Overview

This project is a dashboard application built for Acme Firm. It consists of a backend built with Python and Flask, and a frontend built with Vue.js and Vuetify. The backend serves a REST API that manages restaurant data, and the frontend interacts with this API to display and edit restaurant information.

## Backend

### Setup

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

### Setup

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

