<?php

function db_connect() {
  define('DB_USER', 'registrar');
  define('DB_PASSWORD', 'reg');
  define('DB_HOST', 'localhost');
  define('DB_NAME', 'registrar');

  ($dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME))
    || die('Could not connect to MariaDB: ' . mysqli_connect_error());
  return $dbc;
}

function db_get_id_and_classes($dbc) {
  $query = 'SELECT id, name FROM course';
  $response = mysqli_query($dbc, $query);
  if ($response) {
    $arr = [];
    while ($row = mysqli_fetch_array($response)) {
      array_push($arr, $row);
    }
    return $arr;
  }
  else {
    die('Couldn\'t issue database query: ' . mysqli_error($dbc));
  }
}

?>
