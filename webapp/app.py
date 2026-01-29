from flask import Flask, render_template
import pymysql
import os
template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

# Database configuration from Environment Variables
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASS", "password")
DB_NAME = os.environ.get("DB_NAME", "testdb")

@app.route('/')
def index():
    # Get the background color from the Environment Variable (defaults to white)
    bg_color = os.environ.get("APP_COLOR", "white")
    
    db_version = "Unknown"
    status = "Connected"
    
    try:
        # Attempt to connect to the database
        db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        db_version = data[0]
        db.close()
    except Exception as e:
        status = f"Error: {str(e)}"

    # Pass the color and DB info to the HTML template
    return render_template('index.html', color=bg_color, version=db_version, status=status)

if __name__ == "__main__":
    # Ensure it listens on all interfaces
    app.run(host='0.0.0.0', port=8080)