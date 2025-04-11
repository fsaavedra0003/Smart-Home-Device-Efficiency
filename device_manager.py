class DeviceManager:
    def __init__(self):
        self.devices = [
            {"name": "Smart Light", "status": "on", "energy_usage": 10},
            {"name": "Smart Thermostat", "status": "on", "energy_usage": 50},
            {"name": "Smart Speaker", "status": "off", "energy_usage": 0},
        ]

    def get_devices(self):
        return self.devices

    def toggle_device(self, device_name):
        for device in self.devices:
            if device["name"] == device_name:
                device["status"] = "off" if device["status"] == "on" else "on"
                return f"{device_name} is now {device['status']}."
        return f"{device_name} not found."
