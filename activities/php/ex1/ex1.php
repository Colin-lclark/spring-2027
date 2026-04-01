<?php

/*

Exercise 1: Test this code and alphabetize the list.

1. Install this file in `htdocs` and load the page in a web browser.

2. Modify `db_get_id_and_classes` so that the list of classes appears in sorted
   order.

 */

include('src/functions.php');

$dbc = db_connect();
$id_and_classes = db_get_id_and_classes($dbc);

?>

<!DOCTYPE html>
<html>
  <head>
    <title>EX1</title>
  </head>
  <body>

  <?php

  echo '<table>';
  echo '<tr><td><b>Name</b></td></tr>';

  foreach ($id_and_classes as $row) {
    echo '<tr>';
    echo '<td>' . $row['name'] . '</td>';
    echo '</tr>';
  }

  echo '</table>';

  mysqli_close($dbc);
  ?>

  </body>
</html>
