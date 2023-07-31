# Login-con-Flask---pasantia-SODEP

Este es un proyecto basico demostrativo de como se podria implementar una arquitectura de 3 capas para un Login utilizando el framework Flask para el desarrollo de una REST API.


# Paso a paso
Antes de poder ejecutar el programa debemos tener installado lo siguiente 
https://www.python.org/ asegurate de tener instalado una version de python reciente 

1. Abrir command prompt o terminal en la carpeta raiz donde tenga guardado ambos archivos .py o dirigirse hasta ahi a traves del comando cd 
2. Procedemos a instalar virtualEnv de la siguiente manera
   
***Virtualenv***

Instalar con el comando:
```bash
pip install virtualenv
```
3. A continuacion, creamos un virtualenv con el comando:
```bash
virtualenv env
```
donde "env" sera el nombre de nuestro ambiente virtual

4. Activaremos el virtualenv con el comando:
```bash
rutadecarpetaraiz\nombredelacarpeta\env\Scripts\activate.bat
```

5. Instalamos Flask dentro de nuestro ambiente virtual
   
***flask***

Flask es un framework para desarrollo de aplicaciones webs y api's que necesitaremos para poder correr correctamente el programa.
```bash
pip install flask
```
6. Corrremos el script con el comando:
```bash
flask run
 ```

8. En un nuevo command prompt podemos ejecutar el comando Curl
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"user1\", \"password\": \"password1\"}" http://127.0.0.1:5000/login
```

Las credenciales necesarias ya estan insertadas dentro del comando, "user1" usuario y "password1" como contraseña.
