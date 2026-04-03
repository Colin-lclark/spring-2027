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

?>
