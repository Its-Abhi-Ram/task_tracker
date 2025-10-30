# Design Notes

## Database Schema

- Tasks table includes:
  - `id`: Primary key
  - `title`: Required string
  - `description`: Optional text
  - `priority`: Enum-like string (Low, Medium, High)
  - `due_date`: Date field
  - `status`: Enum-like string (Open, InProgress, Done)

- Indexing:
  - Indexed on `due_date`, `priority`, and `status` for efficient filtering.

## Insights Logic

- Uses Python's `collections.Counter` and date comparisons.
- Computes:
  - Total open tasks
  - Priority distribution
  - Tasks due in next 3 days
  - Busiest day (most tasks due)

## Improvements

- Add user authentication for multi-user support.
- Add pagination and search to task list.
- Use Alembic for DB migrations.
- Add unit tests for API endpoints.
- Enhance UI with charts (e.g., pie chart for priority breakdown).
