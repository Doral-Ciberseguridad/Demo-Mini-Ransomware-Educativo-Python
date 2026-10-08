


print(r"""

  __  __ _       _   ____                                                         ____                           _                  _             
 |  \/  (_)_ __ (_) |  _ \ __ _ _ __  ___  ___  _ __ _____      ____ _ _ __ ___  |  _ \  ___ _ __ ___   ___  ___| |_ _ __ __ _  ___(_) ___  _ __  
 | |\/| | | '_ \| | | |_) / _` | '_ \/ __|/ _ \| '_ ` _ \ \ /\ / / _` | '__/ _ \ | | | |/ _ \ '_ ` _ \ / _ \/ __| __| '__/ _` |/ __| |/ _ \| '_ \ 
 | |  | | | | | | | |  _ < (_| | | | \__ \ (_) | | | | | \ V  V / (_| | | |  __/ | |_| |  __/ | | | | | (_) \__ \ |_| | | (_| | (__| | (_) | | | |
 |_|  |_|_|_| |_|_| |_| \_\__,_|_| |_|___/\___/|_| |_| |_|\_/\_/ \__,_|_|  \___| |____/ \___|_| |_| |_|\___/|___/\__|_|  \__,_|\___|_|\___/|_| |_|
                                                                                                                                                  

Este programa:
0.Importa la libreria Fernet para cifrado
1.Le pide al usuario un mensaje secreto en texto plano
2.Decodifica y convierte el mensaje en bytes
3.Crea una clave simetrica
4.Asigna esa clave a un objeto responsable
5.El objeto cifra el mensaje secreto del usuario
6.Pide al usuario que introduzca la clave para descifrar y recuperar sus datos
""")





# 0.Importar librerias necesarias
from cryptography.fernet import Fernet



# 1.Mensaje secreto 
print("")
mensaje_secreto = input("Guarda tu información secreta aquí --> ")



# 2.Convertir mensaje secreto en bytes
mensaje_secreto_bytes = mensaje_secreto.encode()
print("")
print("Mensaje secreto en bytes:")
print(mensaje_secreto_bytes)



# 3.Crear clave simétrica de cifrado/descifrado
clave = Fernet.generate_key()
print("")
print("Clave del cifrado simétrico:")
print(clave)



# 4.Crear objeto encriptador/desencriptador
cipher = Fernet(clave)



# 5.Cifrar mensaje
mensaje_cifrado = cipher.encrypt(mensaje_secreto_bytes)
print("")
print("Mensaje cifrado:")
print(mensaje_cifrado)



# 6.Descifrar  mensaje
print("")
introducir_clave = input("Introduce la clave para descifrar el mensaje y recuperar tus datos --> ") # Esta línea no es necesaria para el funcionamiento del código. Es solo demostrativa para entender como funciona un ransomware.
mensaje_descifrado = cipher.decrypt(mensaje_cifrado)
print("")
print("Mensaje descifrado:")
print(mensaje_descifrado)
print("")


