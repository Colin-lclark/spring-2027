# Note 35

## Redundancy and normal forms

### Summary

* Data redundancy can cause problems.
* Relation decomposition can eliminate redundancy.

> All problems in computer science can be solved by another level of 
> indirection
> -- Butler Lampson

### Problems caused by redundancy

* *Redundant storage*: The same data is stored multiple times.
* *Update anomalies*: If one copy of the data is updated, others may not, 
  creating inconsistencies.
* *Insertion anomalies*: It may not be possible to store information unless some
  other information is provided.
* *Deletion anomalies*: It may not be possible to delete information without
  losing some other information

### Caveat

Although decomposition can eliminate redundancy, it can lead to problems and 
should be used with caution. Indeed, a join of the decomposed tables can recover 
the content of the original table (before decomposition). If queries over the 
original table, requiring a join first, are frequent, the performance penalty of 
the decomposition may become unacceptable.

### Normal forms

Normal forms can eliminate redundancies by decomposing tables (see Sections
2.10, 2.11, and 2.12 of the text).

Normal forms are organized hierarchically; each normal form further reduces 
sources of dependencies.

Normal forms can often be best described in terms of functional dependencies.

### Functional dependence

Column A depends on column B means each B value is related to at most one A
value. We write B → A (see Section 2.10 of the text).

### First normal form (1NF)

Definition: A table is in first normal form when every column contains only 
atomic values (e.g., no arrays) and the table has a primary key.

Corollaries:

* Every non-key column of a table depends on the primary key.
* A first normal form table has no duplicate rows.

### Second normal form (2NF)

Definition: A table is in second normal form when it is first normal form and
all non-key columns depend on the whole primary key.

This normal form is mainly of historical interest.

Every first normal form table is also in second normal form unless it uses a 
composite primary key.

### Third normal form (3NF)

Definition: A table is in third normal form if it is second normal form and 
whenever a non-key column A depends on column B, then B is unique.

### Boyce-Codd normal form (BCNF)

Only in rare cases does a third normal form table not meet the requirements of 
BCNF. If the primary key is non-composite then a third normal form table is also 
a BCNF table.

BCNF ensures that no redundancy can be detected using functional dependencies 
alone. It is thus the most desirable normal form.

### Activity

Consider the following table with the primary key shown in *italics*.

*ssn*       | name      | lot | rating | hourly_wage | hours_worked
-|-|-|-|-|-
123-22-3666 | Attisho   | 48  | 8      | 10          | 40
231-31-5368 | Smiley    | 22  | 8      | 10          | 30
131-24-3650 | Smethurst | 35  | 5      | 7           | 30
434-26-3751 | Guldu     | 35  | 5      | 7           | 32
612-67-4134 | Madayan   | 35  | 8      | 10          | 40

Questions:

1. Find all functional dependencies.
2. Is this table in first normal form?
3. Is this table in second normal form?
4. Is this table in third normal form?
5. Is this table in Boyce-Codd normal form?
6. For each question related to normal form: if it is not in normal form, use   
   table decomposition to achieve normalization

### References

Sections 2.10, 2.11, and 2.12 of the text.
