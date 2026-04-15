.PHONY: up down api worker web admin lint test

up:
	docker compose -f docker/docker-compose.yaml up -d

down:
	docker compose -f docker/docker-compose.yaml down

api:
	cd backend/api && uvicorn app.main:app --reload --port 8000

worker:
	cd backend/worker && celery -A app.main worker --loglevel=info

sandbox:
	cd backend/sandbox && uvicorn app.main:app --reload --port 8001

web:
	cd frontend/web && npm run dev

admin:
	cd frontend/admin && npm run dev

lint-backend:
	cd backend/api && ruff check .
	cd backend/worker && ruff check .
	cd backend/sandbox && ruff check .

test-backend:
	cd backend/api && pytest
	cd backend/worker && pytest
	cd backend/sandbox && pytest

test-frontend:
	cd frontend/web && npm run test
	cd frontend/admin && npm run test
