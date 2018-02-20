from flask import Flask

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

#Config files for where files will be uploaded
UPLOAD_FOLDER = './app/static/uploads'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
