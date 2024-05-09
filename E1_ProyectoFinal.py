import zipfile as zf
import os
import pyminizip

carpeta = input("Ingrese la direccion de la carpeta: ")

# Iterate over files in directory
for name in os.listdir(carpeta):
	# Open file

	with open(os.path.join(carpeta, name)) as f:
		print(f"Encriptando '{name}'...")

		pre = None
		oupt = (f"{name}.zip") 
		password = "p1p0" 
		com_lvl = 5
		pyminizip.compress(os.path.join(carpeta, name), None, os.path.join(carpeta, oupt), password, com_lvl) 

	if name.endswith(".txt"):
		os.remove(os.path.join(carpeta, name))
	print()
	
print("Se ha encriptado la informacion exitosamente.")
