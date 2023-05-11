 --- schema.sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    name TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    category_id INTEGER,
    amount DECIMAL(10,2) NOT NULL,
    date DATETIME WITH TIME ZONE,
    description TEXT,
    type TEXT NOT NULL CHECK(type IN ('expense', 'income')),
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (category_id) REFERENCES categories (id)
);