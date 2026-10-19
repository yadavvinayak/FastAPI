# FastAPI
Technologies Used

Python: The programming language used to implement the utility functions and API.

FastAPI: A Python web framework used to create HTTP endpoints and automatically generate interactive API documentation.

psutil: A Python library for retrieving system and process information, including CPU, memory, disk, and network statistics.

Uvicorn: The ASGI server used to run the FastAPI application locally.

Project Structure

I separated the system metrics collection logic from the API implementation.

The project uses two important files:

python_programs/
├── system_utils.py
└── api.py

system_utils.py contains the reusable function that collects system information.

api.py defines the FastAPI application and its HTTP endpoints.

This separation makes the code easier to understand and allows the same utility function to be reused by other Python modules.


<img width="1572" height="823" alt="Screenshot 2026-10-19 062352" src="https://github.com/user-attachments/assets/b0de2a3d-6a4c-4791-9a23-971049ff2c3d" />
<img width="1658" height="1108" alt="Screenshot 2026-10-19 062448" src="https://github.com/user-attachments/assets/77a3d0f4-65ea-49f7-83fb-136883e245ec" />

Testing the API

After starting the server, I tested the endpoints in my browser.

1. Welcome endpoint

http://127.0.0.1:8000/hello

This endpoint returns the welcome message.

2. System metrics endpoint

http://127.0.0.1:8000/metrics

This endpoint returns the system information collected by the reusable function.

3. Interactive API documentation

http://127.0.0.1:8000/docs

FastAPI automatically generates an interactive Swagger UI page from the application's registered routes.
