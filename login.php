<?php
$usuario_correto = "admin";
$senha_correta = "123456";

$usuario = $_POST['username'] ??'';
$senha = $_POST['password'] ??'';

if($usuario === $usuario_correto && $senha === $senha_correta) {
    header("Location: index.html");
    exit;
}else{
    header("Location: login.html?error=1");
    exit;
}
?>