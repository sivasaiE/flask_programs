import os
from dotenv import load_dotenv

load_dotenv()
DATABASE=os.environ['DATABASE']
USER=os.environ['USER']
PASSWORD=os.environ['PASSWORD']
HOST=os.environ['HOST']
PORT=os.environ['PORT']

DEBUG=os.environ['DEBUG']
FLASK_PORT=os.getenv('FLASK_PORT',5000)
print(DATABASE)
print(USER)
print(PASSWORD)
print(PORT)
print(HOST)