# Note 30

## Persistence

One important property of databases is *persistence*. That is, we expect any
piece of information in the database to stay available, no matter the
circumstances, until we explicitly discard it. To achieve persistence we must
store our data on a persistent medium. Two popular solutions exist today: (1)
hard drives and (2) flash memories (a.k.a., memory sticks or flash drives).
Hard drives rely on a magnetized medium, flash memories rely on some
semiconductor properties, to store information.

Access time of persistent storage is typically much too slow for a database
application. Hence the role of the memory hierarchy (see below) to allow subsets
of data to be temporarily copied in a different type of memory for more
convenient access.

## Memory hierarchy

> [The] memory hierarchy separates computer storage into a hierarchy based on
> response time. Since response time, complexity, and capacity are related, the
> levels may also be distinguished by their performance and controlling
> technologies.
>
> [Wikipedia](https://en.wikipedia.org/wiki/Memory_hierarchy)

![Computer memory hierarchy](../images/ComputerMemoryHierarchy.svg)

Memory hierarchy figure courtesy of Danlash at en.wikipedia.org, Public domain,
via Wikimedia Commons.

## Hard drives

Hard drives are a form of magnetic storage. A hard drive is rotational storage
medium consisting of one or more platters. Each platter has a given number of
tracks. And each track is broken into sectors.

## Activity

Assume a hard drive with 4 platters, each platter has 2,048 tracks, there is an
average of 4,096 sectors per track, and each sector is 512 bytes. What is the
capacity in bytes of the disk?

### Solution

Capacity =	4 × 2,048 × 4,096 × 512  
            4 × 2 × 1,024 × 4 × 1,024 × 0.5 × 1,024  
            4 × 2 × 4 × 0.5 × 1,024^3  
            16 × 1,024^3 byte or approx. 16 GB
