<?php
    
    // $client = new MongoDB\Client(
    //     'mongodb+srv://kailehmiku:bv48PD2ixipwSUhI@<cluster-address>/test?w=majority'
    //  );

    // $db = $client->test ;
    
    $login = isset($_POST['patient']) ? $_POST['patient'] :"";

    echo "Patient dashboard here <Br>";
    echo $login;
?>