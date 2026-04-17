# Note 34

## Index implementation

Assume we have the `employee` table filled as follows:

emp_no | first_name | last_name
-|-|-
10001  | Julian     | Rhodes
10002  | Sloane     | Whitaker
10003  | Gage       | Henderson
10004  | Zara       | Blackwell
10005  | Chase      | Callahan
10006  | Eleanor    | Wang
10007  | Nash       | Montgomery
10008  | Fiona      | Ashford
10009  | Arthur     | Sterling
10010  | Zion       | Kumar
10011  | Jaxson     | Riggs
10012  | Ivy        | Beaumont
10013  | Silas      | Thorne
10014  | Helena     | Vane
10015  | DeAndre    | Simms
10016  | Beatrice   | Thorne

Let us assume that **emp_no** is the (only) primary key.

## Activity

Consider the following query:

```sql
SELECT *
  FROM employee
 WHERE last_name = 'Riggs';
```

1. How many rows will this query scan?

2. Design an auxiliary data structure to speed up the execution of this query.

3. Assuming values in the **last_name** column are unique, how many steps does
   it take to evaluate the query with the help of the auxiliary data structure
   designed in the previous step?
