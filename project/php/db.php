<?php
/* Authors: Fabrizio Martinez & Colin Sheehan */
$host = 'localhost';
$db   = 'tree';
$user = 'root'; 
$pass = '';     

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Database Connection failed: " . $conn->connect_error);
}
?>