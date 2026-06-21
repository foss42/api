[![Discord Server Invite](https://img.shields.io/badge/DISCORD-JOIN%20SERVER-5663F7?style=for-the-badge&logo=discord&logoColor=white)](https://bit.ly/heyfoss)

<!--This project is participating in GSSoC 2024.

![gssoc-logo-1](https://github.com/foss42/awesome-generative-ai-apis/assets/1382619/670b651a-15d7-4869-a4d1-6613df09fa37)-->

Contributors should go through the [Contributing Guide](https://github.com/foss42/api/blob/main/CONTRIBUTING.md) to learn how to setup development environment, raise an issue and send across a PR.

# Open Source APIs for all!

### Please support this initiative by giving this project a Star ⭐️

Currently, we have open source public APIs for the following use cases that you can directly add to your projects:

### 1. Country

Access to a wide range of country data (geographic & demographic) and services.

### 2. Text Conversion

Convert one type (or format) of data into another format or structure.

### 3. Humanization

Convert data into human readable format for social media applications.

### 4. Case Conversion

Easily convert text between different letter cases.

### 5. User Authentication

Endpoints for user login and logout operations, managing user sessions and access tokens.

### 6. User Data

Retrieve user information, including profiles, lists of users, and specific user details by ID.

### 7. Input/Output (I/O)

Endpoints for testing I/O behavior

### 8. Server-Sent Events (SSE)

Endpoints for testing Server-Sent Events (SSE).

### 9. WebSockets

A self-hosted WebSocket echo endpoint for testing WebSocket clients without relying on public endpoints.

## Understanding the Project Structure

foss42 APIs project has 3 parts:

- [Swagger API Docs](https://api.apidash.dev/docs): The documentation for all the APIs automatically generated via FastAPI.
- [foss42/api](https://github.com/foss42/api): The FastAPI app which serves the APIs.
- [foss42/foss42-core](https://github.com/foss42/foss42-core): The open source core python library which has the algorithms, the data and does all the heavy-lifting.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/foss42/api.git
   cd api
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server:**
   ```bash
   cd src
   python3 -m uvicorn main:app --reload
   ```
   Alternatively, you can run the provided startup script:
   ```bash
   bash startup.sh
   ```

5. **View API Docs:**
   Open your browser and navigate to `http://localhost:8000/docs` to see the interactive Swagger UI.

## How to Run Tests

To execute the test suite locally, use the following commands:

```bash
pip install -r requirements-dev.txt
python3 -m pytest tests/
```

## Doubts?

Also, please feel free to drop by our [Discord server](https://bit.ly/heyfoss) and we can have a chat.
