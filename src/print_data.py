import subprocess
import sys
import os

def print_text_file(file_path):
    """
    Druckt eine Textdatei über Notepad auf einem POS-80 Drucker
    
    Args:
        file_path (str): Pfad zur zu druckenden Textdatei
        printer_name (str, optional): Name des Druckers (optional)
    """
    
    # Prüfen ob die Datei existiert
    if not os.path.exists(file_path):
        print(f"Fehler: Datei '{file_path}' nicht gefunden!")
        return False
    
    try:
        # Notepad mit der Datei öffnen und direkt drucken
        cmd = f'notepad.exe /p "{file_path}"'
        # Befehl ausführen
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Datei '{file_path}' wurde erfolgreich gedruckt.")
            return True
        else:
            print(f"Fehler beim Drucken: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        return False
    
