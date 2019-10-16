import subprocess
import time

return_code = 6

while return_code != 52:
    try:
        result = subprocess.check_output(['curl', 'db:33060'])
    except subprocess.CalledProcessError as e:
        print(e.returncode)
        return_code = e.returncode
    time.sleep(5)