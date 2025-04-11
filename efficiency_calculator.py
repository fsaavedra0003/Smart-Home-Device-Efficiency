class EfficiencyCalculator:
    def __init__(self, device_manager):
        self.device_manager = device_manager

    def calculate_efficiency(self, devices):
        total_usage = sum(device['energy_usage'] for device in devices)
        num_devices = len(devices)
        
        # In this case, assume 100W is the ideal energy usage per device for efficiency
        ideal_usage = num_devices * 100
        
        efficiency = (total_usage / ideal_usage) * 100
        return round(efficiency, 2)
