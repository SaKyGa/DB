CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    created_at TEXT
    )
"""
SELECT_TASKS = """
    SELECT id, title, created_at FROM tasks
"""
INSERT_TASK = """
    INSERT INTO tasks (title, created_at) VALUES (?, ?)
"""
UBDATE_TASK = """ UPDATE tasks SET title = ? WHERE id = ? """
DELETE_TASK = """ DELETE FROM tasks WHERE id = ? """