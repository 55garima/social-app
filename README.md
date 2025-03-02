# Social Media App

A Flask-based social media application with PostgreSQL database.

## Database Migrations

This project uses Flask-Migrate for database migrations. Here's how to work with migrations:

### Initial Setup

The migration system is already initialized. The migrations directory contains all the migration scripts.

### Creating a New Migration

When you make changes to your models, create a new migration:

```bash
flask db migrate -m "Description of the changes"
```

This will generate a new migration script in the `migrations/versions` directory.

### Applying Migrations

To apply all pending migrations:

```bash
flask db upgrade
```

### Reverting Migrations

To revert the most recent migration:

```bash
flask db downgrade
```

### Migration Commands Reference

- `flask db init`: Initialize migration repository (already done)
- `flask db migrate -m "message"`: Generate a new migration
- `flask db upgrade`: Apply all migrations
- `flask db downgrade`: Revert last migration
- `flask db current`: Show current migration
- `flask db history`: Show migration history
- `flask db show <revision>`: Show a specific migration

## Development Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables in `.env` file
6. Run migrations: `flask db upgrade`
7. Start the development server: `python run.py`

## Environment Variables

Create a `.env` file with the following variables:

```
FLASK_ENV=development
FLASK_APP=run.py
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
SECRET_KEY=your_secret_key
```

## Project Structure

- `app/`: Application code
  - `models/`: Database models
  - `routes/`: API routes
  - `__init__.py`: Application factory
- `config/`: Configuration files
- `migrations/`: Database migrations
- `tests/`: Test files
- `run.py`: Application entry point 