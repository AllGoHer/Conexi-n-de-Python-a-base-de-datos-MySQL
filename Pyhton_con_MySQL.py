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