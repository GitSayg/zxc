CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
url text NOT NULL
);

CREATE TABLE IF NOT EXISTS posts (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
text text NOT NULL,
url text NOT NULL,
time integer NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
email text NOT NULL,
psw text NOT NULL,
avatar BLOB DEFAULT NULL,
time integer NOT NULL,
num text NOT NULL
);

CREATE TABLE IF NOT EXISTS users_cards(
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
email text NOT NULL,
avatar BLOB DEFAULT NULL,
qr BLOB DEFAULT NULL,
num text NOT NULL
);