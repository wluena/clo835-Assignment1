from flask import Flask
import pymysql
import os

app = Flask(__name__)

# These variables should match what you set in your Terraform/Kubernetes env
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASS", "password")
DB_NAME = os.environ.get("DB_NAME", "testdb")

@app.route('/')
def index():
    try:
        # Attempt to connect to the database
        db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        return f"<h1>Success!</h1><p>Connected to Database. Version: {data[0]}</p>"
    except Exception as e:
        return f"<h1>Error</h1><p>Could not connect to database: {str(e)}</p>"

if __name__ == "__main__":
    # Port 8080 is common for this assignment
    app.run(host='0.0.0.0', port=8080)