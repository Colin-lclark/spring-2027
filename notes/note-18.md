# Note 18

## Normalization

From the Wikipedia page on [Database
normalization](https://en.wikipedia.org/wiki/Database_normalization):

> [Normalization] is the process of structuring a relational database in
> accordance with a series [of] normal forms [to] reduce data redundancy and
> improve data integrity.

This process leads to data, possibly originally organized as one unit (e.g.,
think about our [City of Portland Tree
Inventory](https://gis-pdx.opendata.arcgis.com/datasets/c2b02440053f459db71e1109b9947e51_1415/explore)
dataset), being stored in distinct tables.

## Join queries

Certain queries requires data to be reorganized temporarily with duplication.
That is the role of join queries.

## Activity

Using the `registrar` example ([schema](./registrar-schema.sql) and
[data](./registrar-data.sql)), write SQL queries to find answers to the
following questions:

* Write a query that lists all the students with the names of all classes that
  they are taking.
* Extend the previous query to lists only the students taking "Physics I:
  Motion".
