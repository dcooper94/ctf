
<html>
<head><title>Echo Panel</title></head>
<body>
<h1>Echo Interface</h1>
<form method="POST">
<input type="text" name="command" placeholder="Enter command">
<input type="submit" value="Execute">
<input type="hidden" name="override" value="coops{panel_override_9F4}">
</form>
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!empty($_POST['override'])) {
        echo "<p>Override accepted.</p>";
    }
}
?>
</body>
</html>
