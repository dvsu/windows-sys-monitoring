import json
from sysinfo import SysInfo


sys_info = SysInfo()

print(json.dumps(sys_info.all_info(), indent=2))
