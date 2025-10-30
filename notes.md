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

