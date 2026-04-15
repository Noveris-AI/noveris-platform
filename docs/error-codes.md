# Navima Error Codes

All API error responses follow this shape:

```json
{
  "code": "MODULE_ACTION_RESULT",
  "message": "Human readable description",
  "detail": {}
}
```

## Format

`{MODULE}_{ACTION}_{RESULT}`

## Common Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `COMMON_INTERNAL_ERROR` | 500 | Unexpected server error |
| `COMMON_VALIDATION_ERROR` | 422 | Request validation failed |
| `COMMON_NOT_FOUND` | 404 | Resource not found |
| `COMMON_FORBIDDEN` | 403 | Permission denied |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests |

## Auth Module

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `AUTH_INVALID_CREDENTIALS` | 401 | Email or password is incorrect |
| `AUTH_ACCOUNT_LOCKED` | 403 | Account is temporarily locked |
| `AUTH_SESSION_EXPIRED` | 401 | Session has expired |
| `AUTH_CSRF_INVALID` | 403 | CSRF token is missing or invalid |
| `AUTH_PASSWORD_TOO_WEAK` | 422 | Password does not meet policy |
| `AUTH_PASSWORD_MISMATCH` | 422 | Password confirmation does not match |

## License Module

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `LICENSE_INVALID_KEY` | 400 | License key is invalid |
| `LICENSE_EXPIRED` | 403 | License has expired |
| `LICENSE_VERIFICATION_FAILED` | 403 | License verification failed |
| `LICENSE_NODE_LIMIT_EXCEEDED` | 403 | Maximum allowed nodes exceeded |

## Workspace Module

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `WS_NAME_TAKEN` | 409 | Workspace name already exists |
| `WS_HAS_RUNNING_RESOURCES` | 409 | Cannot delete workspace with running resources |
| `WS_MEMBER_NOT_FOUND` | 404 | Member not found in workspace |

## Deployment Module

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `DEPLOY_NODE_OFFLINE` | 400 | Target node is offline |
| `DEPLOY_ENGINE_NOT_SUPPORTED` | 400 | Inference engine not supported |
| `DEPLOY_FAILED_TO_START` | 502 | Engine process failed to start |
