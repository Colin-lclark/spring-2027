<?php
/* Authors: Fabrizio Martinez & Colin Sheehan */
require 'db.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Result</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Update Status</h1>
    <div class="card">
        <?php
        if (isset($_POST['tree_id']) && isset($_POST['new_health'])) {
            $tree_id = $_POST['tree_id'];
            $new_health = $_POST['new_health'];
            
            $sql = "UPDATE tree SET health = ? WHERE tree_id = ?";
            $stmt = $conn->prepare($sql);
            
            // "si" means String (health), Integer (tree_id)
            $stmt->bind_param("si", $new_health, $tree_id);
            
            if ($stmt->execute()) {
                if ($stmt->affected_rows > 0) {
                    echo "<p>✅ Successfully updated Tree ID $tree_id to health status '$new_health'.</p>";
                } else {
                    echo "<p>⚠️ Tree ID $tree_id was found, but the health is already set to '$new_health' (or the ID doesn't exist).</p>";
                }
            } else {
                echo "<p>❌ Error updating record: " . $conn->error . "</p>";
            }
            $stmt->close();
        }
        $conn->close();
        ?>
    </div>
    <a href="index.html" class="back-link">← Return to Main Menu</a>
</body>
</html>