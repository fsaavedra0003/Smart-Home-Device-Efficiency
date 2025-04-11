class EfficiencyCalculator:
    def __init__(self, device_manager):
        self.device_manager = device_manager

    def calculate_efficiency(self, devices):
        total_devices = len(devices)
        efficient_devices = sum(1 for device in devices if device['SmartHomeEfficiency'] == 1)
        
        # Calculate the percentage of efficient devices
        efficiency = (efficient_devices / total_devices) * 100
        return round(efficiency, 2)
