import os
from dotenv import load_dotenv

load_dotenv()

SOURCE = os.getenv("SRC")
DEST = os.getenv("DES")
