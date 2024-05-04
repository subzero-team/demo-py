from flask import Flask, render_template
import os

app = Flask(__name__)
app.config.update(
    STATIC_FOLDER='static',
)
enviroment = os.getenv('env',"Prod")
version = os.getenv('version',"1.0.0")
color = os.getenv('color',"blue")

# Definisci la rotta per la pagina principale
@app.route('/')
def index():
    # Passa i parametri al template
    context = {
        'enviroment': enviroment,
        'version': version,
        'color': color
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    # Assicurati che l'immagine sia nella stessa cartella del file Python o in una cartella statica configurata
    app.run(debug=True)
