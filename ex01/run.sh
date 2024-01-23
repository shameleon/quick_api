#!/bin/sh

# poetry run ./run.sh
# or
# poetry run python app/main.py
export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-127.0.0.1}
export PORT=${PORT:-8000}

exec uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"