import subprocess
import time
from pathlib import Path

CARTELLA = Path(__file__).parent
FILE_TESTO = CARTELLA / "testo.txt"

while True:
    try:
      
        with FILE_TESTO.open("a", encoding="utf-8") as f:
            f.write("fix\n")

 
        subprocess.run(
            ["git", "add", "testo.txt"],
            cwd=CARTELLA,
            check=True
        )

  
        subprocess.run(
            ["git", "commit", "-m", "change"],
            cwd=CARTELLA,
            check=True
        )

   
        subprocess.run(
            ["git", "push"],
            cwd=CARTELLA,
            check=True
        )

        print("Commit e push completati. Attendo 5 secondi...")
        time.sleep(5)

    except KeyboardInterrupt:
        print("\nScript interrotto.")
        break
    except subprocess.CalledProcessError as e:
        print(f"Comando Git fallito: {e}")
        print("Controlla il repository e la connessione, poi riprova.")
        time.sleep(5)