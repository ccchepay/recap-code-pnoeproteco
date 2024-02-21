<?php
//FUNCIONES
function imprimir_cualidades($cualidades) {
    foreach ($cualidades as $cualidad) {
        echo $cualidad . "\n";
    }
}
if(!function_exists("readline")) {
    function readline($prompt = null){
        if($prompt){
            echo $prompt;
        }
        $fp = fopen("php://stdin","r");
        $line = rtrim(fgets($fp, 1024));
        return $line;
    }
}

function agregar_cualidades(&$cualidades) {
    $flag = true;
    while ($flag) {
        if (readline("Deseas agregar más condiciones?(Y/N)") == "Y") {
            $cualidades[] = readline("Escribe la propiedad: ");
        } else {
            $flag = false;
        }
    }
}

function cuestionar_cualidades($cualidades) {
    $score = 0;
    foreach ($cualidades as $cualidad) {
        $prompt = readline("Es $cualidad? (Y/N)");
        if ($prompt != 'N') {
            $score = $score + 1;
        }
    }
    return $score;
}

function calcular_score($score, $len) {
    if (($score / $len) == 1) {
        echo "Es perfecto\n";
    } elseif (($score / $len) >= 0.8) {
        echo "Apliquese o se lo ganan\n";
    } elseif (($score / $len) >= 0.6) {
        echo "Momeno\n";
    } elseif (($score / $len) >= 0.4) {
        echo "No te lo recomiendo\n";
    } elseif (($score / $len) <= 0.2) {
        echo "Corre y no mires atrás\n";
    }
}

//VARIABLES
$qualities = ["alto", "bronceado", "guapo", "rico", "sexy", "tierno", "rudo"];

//PROGRAMA
echo "Vamos a ver si la persona que piensas te conviene\n";
echo "Estas son las cualidades que actualmente validamos\n";
imprimir_cualidades($qualities);
agregar_cualidades($qualities);
echo "vamos a comenzar\n";

$score = cuestionar_cualidades($qualities);
calcular_score($score, count($qualities));
?>
