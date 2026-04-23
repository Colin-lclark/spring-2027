<?php
/* Authors: Fabrizio Martinez & Colin Sheehan */
require 'db.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Health Results</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Health Status Search Results</h1>
    
    <?php
    if (isset($_GET['health'])) {
        $health = $_GET['health'];
        
        $sql = "SELECT tree_id, diameter, date_inventoried FROM tree WHERE health = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("s", $health);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            echo "<table><tr><th>Tree ID</th><th>Diameter</th><th>Date Inventoried</th></tr>";
            while($row = $result->fetch_assoc()) {
                echo "<tr><td>" . $row["tree_id"] . "</td><td>" . $row["diameter"] . "</td><td>" . $row["date_inventoried"] . "</td></tr>";
            }
            echo "</table>";
        } else {
            echo "<p>No trees found with status: " . htmlspecialchars($health) . ".</p>";
        }
        $stmt->close();
    }
    $conn->close();
    ?>
    <a href="index.html" class="back-link">← Return to Main Menu</a>
</body>
</html>