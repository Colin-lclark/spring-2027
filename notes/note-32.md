# Note 32

## Select query processing

In many databases, read queries (i.e., `select` statements) are more frequent
than updates. This note discusses aspects of processing `select` statements that
may affect their performance (i.e., how quickly it can generate the result).

### Table scan

Absent additional information about the data stored in tables, `select` query
processing may need to scan each row of the table sequentially to check if it
meets the conditions described in the query. This method, referred to as a *full
table scan* or *sequential scan* is usually slowest because it may read the
content of the entire table.

### Index scan

To speed up read queries, one may add one or more indices. With such structures
in place, a read query may scan the index rather than the table. This method is
referred to as an *index scan*. To find matching rows, the index is scanned
sequentially and only when a match is found does the operation read the needed
rows in the table. Since indices are typically much smaller, fewer accesses to
storage are required to generate the result.

In a way, indices maintain additional information about the data stored in a
table to speed up some read queries.

### Updates

If a table is associated with one or more indices, updates to the table will be
slower to maintain the accuracy of indices.

### Query processing

The database estimates the number of rows selected by a query. If this number
represents a high percentage of the total rows, the database is likely to
perform a table scan. Otherwise, if an appropriate index exists, the database
will rely on an index scan.
