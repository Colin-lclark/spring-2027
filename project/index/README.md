# Project: Index

This is a team project. Work on it with your assigned team. Only one of you
needs to turn it in — but make sure someone does!

## Objective

* Define an index to speed up the processing of one of your queries

## Details

Select a query, from those you have designed in the
[SQL Queries](../sql-queries/) assignment, that requires the full scan of one of
your largest tables (use the `EXPLAIN` command to find such a query). Measure
the time it takes to run the selected query. Then create an index and measure
the improvement in runtime, Finally, compute the achieved speedup.

## What to turn in

*When ready, show your work to the instructor.*

But also upload a text file with the query you selected, the command you used to
create the index, the original runtime, the improved runtime using the index,
and the speedup that this index has achieved (ratio of the original runtime
divided by the improved runtime, this ratio should be greater than 1.0).
