# Project: Schema

This is a team project. Work on it with your assigned team. Only one of you
needs to turn it in — but make sure someone does!

## Objective

* Define the tables you will need in your Tree database.

## Details

Create a text file with all the SQL statements necessary to create all the
tables required for your Tree database design. Call this file `tree-schema.sql`.
Use your ER diagram and glossary to name all tables, their columns, their types,
and their attributes. Apply what you have learned in Chapter 3 (e.g., types,
null values, primary keys, foreign keys, referential integrity, and constraints)
and Chapter 2 (e.g., implementing entities, implementing relationships,
implementing attributes, normalization).

Your sequence of SQL statements should start with the following line:

```sql
DROP DATABASE IF EXISTS tree;
```

That way this file can be used without generating errors even if the database
`tree` already exists (obviously you’d lose the content of the entire database
previously loaded, so use with care!).

The beginning of your file might look something like:

```sql
-- Tree database
-- Version 1.0
-- Date 2/13/2026
-- Author Jane Doe

DROP DATABASE IF EXISTS tree;
CREATE DATABASE tree;
USE tree;

CREATE TABLE species (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);
```

Test that your file works by uploading it in MySQL/MariaDB.
