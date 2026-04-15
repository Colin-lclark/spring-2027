# Note 33

## Indices

An index on a table is an auxiliary structure (another level of indirection!)
designed to speed up operations.

## Activity

### Prep

On the system with your XAMPP installation perform the following steps:

1. `git clone https://github.com/datacharmer/test_db.git`
2. `cd test_db`
3. `mysql -u root < employees.sql`

### Stage 1

Run the following queries below. For each query, note the running time reported
by MySQL.

```sql
 SELECT count(*)
   FROM employees
  WHERE last_name = 'Peha';

 SELECT count(*)
   FROM employees
  WHERE last_name IN ('Peha', 'Genin');

 SELECT count(*)
   FROM employees
  WHERE birth_date = '1960-03-14';

 SELECT count(*)
   FROM employees
  WHERE last_name = 'Peha'
    AND first_name = 'Mary';
```

Notice anything remarkable?

### Stage 2

Run the following query.

```sql
EXPLAIN
 SELECT count(*)
   FROM employees
  WHERE last_name = 'Peha';
```

Search for explanation of the output with your favorite search engine.

Get explanations for the other queries you’ve run so far.  Notice any
differences?

### Stage 3

Run the following command.

```sql
CREATE INDEX index_last_name ON employees (last_name);
```

And then rerun all the queries computing the speedup (i.e., the ratio of the
original latency divided by the new latency).

### Stage 4

Let’s look at the output of the `EXPLAIN` command for some of these queries.

### References

Sections 5.3 through 5.5 of the text.
