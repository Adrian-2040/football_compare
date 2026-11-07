"""
run.py (uruchom)

Od tego pliku startuje program (zielona strzałka w PyCharmie).
Tworzy aplikację i uruchamia serwer pod adresem http://127.0.0.1:5000.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
