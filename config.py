"""Local configuration"""
import os
import socket
import getpass

# MY_DEVICE_ID = socket.gethostname()
# MY_OPERATOR_ID = getpass.getuser()

MY_DEVICE_ID = "Ryzen5"
MY_OPERATOR_ID = "matth"


TIMEZONE='UTC'
if os.path.exists('/etc/timezone'):
    with open('/etc/timezone', 'r', encoding='utf-8') as f:
        TIMEZONE=f.read().strip()
