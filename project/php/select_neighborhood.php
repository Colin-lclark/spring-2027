<?php
/* Authors: Fabrizio Martinez & Colin Sheehan */
require('./db.php'); /*Changed the require statement*/
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Neighborhood Results</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Neighborhood Search Results</h1>
    
    <?php
    if (isset($_GET['neighborhood'])) {
        $neighborhood = $_GET['neighborhood'];
        
        // Using a prepared statement for security
        $sql = "SELECT tree.tree_id, tree.diameter, tree.health 
                FROM tree 
                JOIN location ON tree.location_id = location.location_id 
                WHERE location.neighborhood = ?";
                
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("s", $neighborhood);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            echo "<table><tr><th>Tree ID</th><th>Diameter</th><th>Health</th></tr>";
            while($row = $result->fetch_assoc()) {
                echo "<tr><td>" . $row["tree_id"] . "</td><td>" . $row["diameter"] . "</td><td>" . $row["health"] . "</td></tr>";
            }
            echo "</table>";
        } else {
            echo "<p>No trees found in " . htmlspecialchars($neighborhood) . ".</p>";
        }
        $stmt->close();
    }
    $conn->close();
    ?>
    <a href="index.html" class="back-link">← Return to Main Menu</a>
</body>
</html>