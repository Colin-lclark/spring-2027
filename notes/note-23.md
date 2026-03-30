# Note 23

## Join queries

### Prefixes

Ambiguity arises when a query must refer to columns in distinct tables that have
the same name. Use prefixes to break such ambiguities. Such a prefix consists of
a table name followed by a period (`.`).

### Aliases

Queries can specify aliases with the keyword (`AS`). You can use this keyword
in the `SELECT` portion of a query to give a temporary name to a column of
output (e.g., to make the output more readable).

You can also use `AS` with the `FROM` portion of a query to assign tables
aliases (e.g., to shorten a query).

## Activity

Using the `registrar` example ([schema](./registrar-schema.sql) and
[data](./registrar-data.sql)), write SQL queries to find answers to the
following questions:

* List the course schedule of every student. The resulting table should have the
  headers "student name" and "course name", and list the rows sorted by student
  names and then by course names.
* Find the number of classes taken by each student; students should be listed
  alphabetically; and the headers should read "student name" and "number of
  classes".
