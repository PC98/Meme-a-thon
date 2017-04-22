<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file);
exec("python MAIN.py uploads/".$_FILES["fileToUpload"]["name"]);
echo '<h3>Original Image</h3>';
echo '<img style="width:540px; height: auto;" src="uploads/'.$_FILES["fileToUpload"]["name"].'">';
echo '<h3>Edited Image</h3>';
echo '<img style="width:540px; height: auto;" src="uploads/EDITED'.$_FILES["fileToUpload"]["name"].'">';
?>