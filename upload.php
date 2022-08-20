<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload</title>
</head>
<body>
    <?php
    $filename = $_FILES['file']['name'];

    $location = "upload/".$filename;

    if( move_uploaded_file($_FILES['file']['tmp_name'], $location))(
        echo '<p>File Uploaded Successfully</p>';
    )else(
        echo '<p>error uploading file</p>';
    )
    ?>
</body>
</html>