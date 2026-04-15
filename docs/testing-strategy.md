# Testing Strategy

## Backend

- **Unit tests**: `pytest backend/api/tests` and `pytest backend/worker/tests`
- **Integration tests**: Use `pytest-asyncio` + `httpx.AsyncClient` against FastAPI apps
- **Coverage target**: 80% for MVP, enforced in CI

## Frontend

- **Unit tests**: `vitest` + `@testing-library/react`
- **E2E tests**: Playwright (future, not required for Module 1)
- **Coverage target**: 70% for MVP

## Docker

- Every Dockerfile in `deploy/build/` is validated with `docker build` in CI.
- No image is pushed from CI in Module 1; push step is added later.

## Local Development

1. Start infrastructure: `docker compose -f docker/docker-compose.yaml up -d`
2. Run backend tests: `cd backend/api && pytest`
3. Run frontend tests: `cd frontend/web && npm run test`
