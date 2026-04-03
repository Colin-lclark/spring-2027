<?php

/*

Exercise 3: Get a search string and generate a result.

1. Install `search.html` and `search-results.php`. Load `search.html` in a
   web browser and follow the stated directions. Study the HTML and PHP code
   used to implement this functionality.

2. Add a function in `src/functions.php` that returns all classes
   whose names contain a given search string.

3. Modify `search-results.php` to use the function of step 2 to
   produce a list of classes.

 */

echo 'You searched for "' . $_GET['search_string'] . '".';

?>
