# Note 11

## SQL

From Wikipedia:

> Structured Query Language (SQL) is a *domain-specific language* used to
> manage data, especially in a relational database management system.

SQL is a declarative language (as opposed to imperative, e.g., C, Python, Java).

Declarative: *What* should be done

Imperative: *How* should it be done

### Data definition

`DROP DATABASE airbnb` deletes an entire database, usually irretrievably; fails
if the database does not exist.

`DROP DATABASE IF EXISTS airbnb` deletes an entire database, but only attempts
the action if the database exists.

`USE airbnb` switches context to the named database.

`CREATE TABLE neighborhood ( <column definition> [, <column definition>]... )`
creates a new table.

### SQL script

* Text file
* Extension: `.sql`
* Sequence of *statements* and *comments*
  * Comment starts with `--` and ends at the end of the line

### Example: `airbnb_schema.sql`

```sql
- AirBnB Database
-- Version 1.0
-- 2/13/2026
-- Author Jane Doe


DROP DATABASE IF EXISTS airbnb;

CREATE DATABASE airbnb;

USE airbnb;

CREATE TABLE neighborhood(
    id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);
```
