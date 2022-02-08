import inspect
import os


current_file = inspect.getframeinfo(inspect.currentframe()).filename

HOST = "127.0.0.1"
PORT = 8080
PATH_TO_ROOT = os.path.dirname(os.path.abspath(current_file))
