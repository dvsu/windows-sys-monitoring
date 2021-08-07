import wmi

# w = wmi.WMI(namespace="root\OpenHardwareMonitor")

# hw = w.Hardware()

# for h in hw:
#     print(h)

# temperature_infos = w.Sensor()

# data = {}

# units = {
#     "Clock": "MHz",
#     "Control": "%",
#     "Data": "GB",
#     "Fan": "RPM",
#     "Load": "%",
#     "Power": "W",
#     "Temperature": "C",
#     "Voltage": "V"
# }

# for sensor in temperature_infos:

#     device_type, device, measurement, *_ = sensor.Identifier.split('/')[1:]

#     if device_type not in data.keys():
#         data[device_type] = {}

#     if device not in data[device_type].keys():
#         data[device_type][device] = {}

#     if measurement not in data[device_type][device].keys():
#         data[device_type][device][measurement] = []

#     data[device_type][device][measurement].append({
#         "name": sensor.Name.lower().replace(' ', '_').replace('#', ''),
#         "value": {
#             "current": float(sensor.Value),
#             "min": float(sensor.Min),
#             "max": float(sensor.Max)
#         },
#         "type": sensor.SensorType,
#         "unit": units[sensor.SensorType]
#     })


# print(json.dumps(data, indent=2))
