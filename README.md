# 🔐 GENERADOR DE CREDENCIALES

Una herramienta sencilla desarrollada en Python para generar un nombre de usuario/correo corporativo y una contraseña segura.

## Características

- Genera un correo corporativo.
- Agrega las 3 primeras letras del apellido.
- Agrega 2 dígitos aleatorios al usuario.
- Genera una contraseña aleatoria con una longitud personalizable.
- Utiliza el módulo `secrets` de Python para generar contraseñas de forma segura.
- Soporta mayúsculas, minúsculas, números y caracteres especiales.

## ¿Cómo funciona?
--- El usuario / correo corporativo es generado usando: 
Nombre + 3 primeras letras del apellido + 2 dígitos aleatorios + @corp.pe

--- La contraseña es generada usando
Letras + Números + Caracteres especiales

## Requiere :
Python 3.X

## Ejemplo:
Nombre: Juan
Apellido: Ramirez
Longitud de contraseña: 12

usuario: JuanRam12@corp.pe
Contraseña: xP$93!0PqT2n
