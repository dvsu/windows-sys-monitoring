# Windows System Info + Monitoring

System monitoring tool for Windows, created on top of `wmi` module.

## Currently Supported Features

1. System info

   - Hardware
     - Disk
     - Memory
     - Motherboard
     - Processor
     - Video (GPU)
   - Software
     - Operating system (OS)

2. Sensors and operation data (requires `Open Hardware Monitor`)

## Available Methods

- `all_hardware_info()`
- `all_software_info()`
- `all_info()`

## How to Use

```python
import json
from sysinfo import SysInfo


sys_info = SysInfo()

# get all hardware and software info, then pretty print it using json.dumps()
print(json.dumps(sys_info.all_info(), indent=2))
```

The output is extremely long which makes it quite difficult to inspect. I recommend copying the print output to [JSON Editor Online](https://jsoneditoronline.org/) and select `tree` view.
