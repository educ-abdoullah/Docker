from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    connexion = mysql.connector.connect(
        host="mysql-db",
        user="root",
        password="root",
        database="tpdb"
    )

    cursor = connexion.cursor()
    cursor.execute("SELECT 'Connexion MySQL réussie'")
    resultat = cursor.fetchone()

    cursor.close()
    connexion.close()

    return resultat[0]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)