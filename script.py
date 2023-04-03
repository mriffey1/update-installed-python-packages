import subprocess
import json

cmd = 'pip list --outdated --format=json'

result = subprocess.run(cmd, stdout=subprocess.PIPE)
new = result.stdout.decode('utf-8')

json_object = json.loads(new)

json_formatted_str = json.dumps(json_object, indent=2)
list_to_update = []
count = 0
for item in json_object:
    command = ("pip install " + json_object[count]['name'] + " --upgrade")
    ret = subprocess.run(command, capture_output=True, shell=True)
    print(ret.stdout.decode())
    count += 1
