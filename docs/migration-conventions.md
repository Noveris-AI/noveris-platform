# Alembic Migration Conventions

## Naming

Format: `{yyyy_mm_dd}_{HHMMSS}_{description}.py`

Example: `2024_05_20_143000_create_users_table.py`

## Rules

1. **One module per migration file**. Do not mix schema changes from multiple modules in a single revision (exceptions allowed for tightly coupled tables).
2. **Explicit dependencies**. When two migrations are generated close together, the later one must declare `depends_on` pointing to the earlier revision.
3. **No data seeding in migrations**. Use `scripts/setup/seed_data.py` for default data insertion.
4. **Always review autogenerate output**. Check constraints, indexes, and `nullable` settings before committing.
5. **Downgrade must be implemented**. Every upgrade must have a corresponding, tested downgrade.

## Workflow

```bash
cd backend/api
alembic revision --autogenerate -m "create users table"
alembic upgrade head
alembic downgrade -1
alembic upgrade head
```
