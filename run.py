from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True sam przeladowuje aplikacje po zmianie kodu
    app.run(debug=True)
