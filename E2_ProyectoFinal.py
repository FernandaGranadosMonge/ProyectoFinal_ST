import zipfile
import os

def archiveNames(path:str):
    if os.path.isdir(path):
        archives = os.listdir(path)
        return archives

def dencrypt(name:str, password:str, path:str):
    full_path = path + "/" + name
    try:
        with zipfile.ZipFile(full_path) as zip:
            zip.extractall(path, pwd=password.encode())
            zip.close()
            os.remove(full_path)
            print(f"File '{name}' extracted successfully.")

    except zipfile.BadZipFile:
        print(f"Error: '{full_path}' is not a valid zip file.")
    except Exception as e:
        print(f"Error: An error occurred with '{full_path}': {e}")


if __name__ == '__main__':
    path = "Archivos"
    password = "p1p0"

    archives = archiveNames(path)
    print("Files in folder:", archives)

    for name in archives:
        dencrypt(name, password, path)