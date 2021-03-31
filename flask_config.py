import os 
from dotenv import load_dotenv

load_dotenv()

DEBUG=os.environ['DEBUG']
PORT=os.environ['PORT']