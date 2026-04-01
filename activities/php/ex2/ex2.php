<?php

/*

Exercise 2: Get a user input and generate a result.

1. Install `classes.html` and `classes-results.php`. Load `classes.html` in a
   web browser and follow the stated directions. Study the HTML and PHP code
   used to implement this functionality.

2. Implement the previous functionality by adding the necessary code in this
   file so that the HTML code for the <form> tag is generated dynamically based
   on the output of `db_get_id_and_classes`.

3. Modify `classes-results.php` so that it lists the students taking the
   selected class.

 */

include('src/functions.php');

$dbc = db_connect();
$id_and_classes = db_get_id_and_classes($dbc);

?>

<!DOCTYPE html>
<html>
  <head>
    <title>EX2</title>
  </head>
  <body>

  <?php

  /* Add your code here */

  mysqli_close($dbc);
  ?>

</body>
</html>
