# Conexión de Python a base de datos MySQL  ![image](https://github.com/user-attachments/assets/0ec69129-e2c9-4b13-9362-60f53799c1ee) ![image](https://github.com/user-attachments/assets/8d8cb19c-928c-4e37-a011-13dbdaa6551d)
_____________________________________________________________________________________________________________________________________________________________________________________________________________________________

1.	Descargamos nuestro gestor de MySQL, prime en el navegador escribimos XAMPP el cual contiene el gestor de bases de datos de MySQL

   ![image](https://github.com/user-attachments/assets/a13e8138-82be-405e-a41b-108a5a8416fe)

2.	Luego que descargue se abrirá la siguiente ventana en cual seleccionaremos start Apache y Start MySQL.

  ![image](https://github.com/user-attachments/assets/e0a582a7-20a7-4336-9659-f65c1f53e59f)

3.	Ahora nos vamos al navegador y escribimos lo siguiente:

   ![image](https://github.com/user-attachments/assets/0bb24c00-b299-47ec-baea-08182a2cd684)

  Luego de dar enter veremos el panel de administración de phpMyAdmin

  ![image](https://github.com/user-attachments/assets/2817e612-dedc-4553-89c7-4ca851a29089)

 Ahora hacemos click en Nueva para crear una base de datos y le asignamos un nombre (Base_Prueba) y luego hacemos click en crear.

 ![image](https://github.com/user-attachments/assets/87ce4355-9f66-4d7a-a5f9-a8e7d43988ba)

 Luego crearemos una tabla asignándole nombre usuarios y 3 columnas y, posteriormente le damos click en crear.

 ![image](https://github.com/user-attachments/assets/b77ac912-3847-4455-a59a-fe74e2a79ac2)

Posteriormente se nos abrirá una ventana donde pasaremos los datos de nuestra tabla como:

IDusuario  INT (4) ,

Nombre  TEXT(20),

Clave  VARCHAR(10)


Y le damos click en guardar para crear las columnas de la tabla.

![image](https://github.com/user-attachments/assets/0454eba6-acc4-4361-b657-8b8d3b60a8ac)

4.	Luego nos vamos a nuestro editor de código (VSCode) y creamos la carpeta para la conexión de python con la base de datos de MySQL e importamos la librería.
Previo a ello debes instalar en la terminar el siguiente comando:

código:

        pip install mysql-connector-python


Si en caso aun no tuvieras instalado la librería de mysql, a pesar de intentarlo con el anterior comando, ve a tu terminar y escribe el siguiente comando para que descargue y puedas trabajar con normalidad.

código:

        & "C:/Users/User/AppData/Local/Python/bin/python.exe" -m pip install mysql-connector-python

Donde:

•	& "C:/Users/User/AppData/Local/Python/bin/python.exe"   es tu ruta donde tienes python.

•	-m pip install mysql-connector-python    es el comando que instala el paquete de MySQL.

![image](https://github.com/user-attachments/assets/e8804eec-83bc-4c63-81c3-9ad83a8f7081)


•	Ahora escribimos el código completo para conectar con la base de datos

código:

       import mysql.connector

       try: # te conecta
           conexion=mysql.connector.connect(host='localhost',
           
                                           user='root',
                                           
                                           passwd='',
                                           
                                           database='Base_Prueba')

           cursor01 = conexion.cursor()
           
           print("¡Conexión exitosa a MySQL!")
    
           # 2. HACES EL INSERT
           
           cursor01.execute("INSERT INTO usuarios VALUES(1001, 'Axel', 'admi2')")
    
           # 3. ¡EL COMMIT! (Obligatorio en MySQL también para guardar los datos)
           
           conexion.commit()
           
           print('Datos insertados correctamente en la tabla.')

       except Exception as err:
       
           print('Ocurrió un error:', err)

       finally:
       
           # 4. Cerramos todo de forma segura
           
           # En MySQL usamos .is_connected() para saber si sigue abierta
           
           if 'conexion' in locals() and conexion.is_connected():
           
               cursor01.close()
               
               conexion.close()
               
               print("Conexión cerrada correctamente.")


   ![image](https://github.com/user-attachments/assets/0b485c94-ae55-4531-8efd-dcc6797831a4)

   •	Luego nos dirigimos a la base de datos MySQL para verificar que la conexión fue exitosa, para ello hacemos click en usuarios del phpMyAdmin.

   ![image](https://github.com/user-attachments/assets/c3e004ad-f336-4426-9998-01f543b67f6f)

   

   
![image](https://github.com/user-attachments/assets/d59ab7cc-29c0-4333-a0dd-fa9cee68e68d)






 


 
