# Weather Forecast API

This Django-based REST API provides weather forecasts for cities. It uses the OpenWeather API for weather data and the Reservamos API for city information.

## Prerequisites

- Python 3.11
- Poetry (Python package manager)
- Docker and Docker Compose (optional, for running with Docker)

## Installation and Running (Local)

1. Clone the repository:
   ```
   git clone https://github.com/ferjflores/reservamos_challenge.git
   cd reservamos_challenge
   ```

2. Make sure you're using Python 3.11. You can check your Python version with:
   ```
   python --version
   ```

3. Install dependencies using Poetry:
   ```
   poetry install
   ```

4. Set up environment variables (see Environment Variables section below).

5. Apply database migrations:
   ```
   poetry run migrate
   ```

6. Start the development server:
   ```
   poetry run start
   ```

The API will be available at `http://localhost:8000/api/forecast/`.

## Running with Docker (Optional)

If you prefer to use Docker, follow these steps:

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone the repository (if you haven't already):
   ```
   git clone https://github.com/ferjflores/reservamos_challenge.git
   cd reservamos_challenge
   ```

3. Set up environment variables (see Environment Variables section below).

4. Build and start the service:
   ```
   docker-compose up --build
   ```

   This command will build the Docker image (using Python 3.11), install dependencies, and start the development server. The API will be available at `http://localhost:8000/api/forecast/`.

5. To stop the service:
   ```
   docker-compose down
   ```

## Environment Variables

This project uses environment variables for configuration. Create a `.env` file in the project root with the following contents:

```
OPENWEATHER_API_KEY=your_api_key_here
OPENWEATHER_API_URL=https://api.openweathermap.org/data/3.0/onecall
RESERVAMOS_API_URL=https://search.reservamos.mx/api/v2/places
```

Make sure to replace `your_api_key_here` with your actual OpenWeather API key.

These environment variables are used to configure the API endpoints and keys used by the application. If you need to change the URLs for the OpenWeather or Reservamos APIs, you can do so by modifying these environment variables without changing the code.

## Usage

To get a weather forecast, make a GET request to the `/api/forecast/` endpoint with a `city` parameter:

```
http://localhost:8000/api/forecast/?city=Monterrey
```

This will return a list of matching cities with their 7-day weather forecasts.

## Available Commands

All commands are run using Poetry. Here are the available commands:

- `poetry run start`: Start the development server
- `poetry run test`: Run all tests
- `poetry run test_unit`: Run unit tests
- `poetry run test_integration`: Run integration tests
- `poetry run makemigrations`: Create new database migrations
- `poetry run migrate`: Apply database migrations
- `poetry run showmigrations`: Show the status of database migrations

## Testing

This project includes both unit tests and integration tests. The tests are located in the `tests` directory, with separate subdirectories for unit and integration tests.

To run all tests:
```
poetry run test
```

To run only unit tests:
```
poetry run test_unit
```

To run only integration tests:
```
poetry run test_integration
```

## Logging

This project uses Python's built-in logging module to log information, warnings, and errors. Logs are written to both the console and rotating log files:

- Console: All logs of level DEBUG and above are printed to the console.
- File: All logs of level INFO and above are written to rotating log files in the `logs` directory.

Log files:
- Main log file: `logs/weather_api.log`
- The logger uses a RotatingFileHandler, which will create new log files when the main log file reaches 5 MB in size.
- A maximum of 5 backup log files are kept.

To view the logs:

1. Check the console output when running the server.
2. Inspect the log files in the `logs` directory in the project root.