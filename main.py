from device_manager import DeviceManager
from efficiency_calculator import EfficiencyCalculator

def main():
    # Path to the CSV file
    csv_path = '/smart_home_device_data.csv'
    
    device_manager = DeviceManager(csv_path)
    efficiency_calculator = EfficiencyCalculator(device_manager)

    print("Welcome to the Smart Home Device Efficiency Monitor.")
    
    devices = device_manager.get_devices()
    print(f"Found {len(devices)} devices.")
    
    for device in devices:
        print(f"Device ID: {device['serID']}, Type: {device['DeviceType']}, "
              f"Usage Hours: {device['UsageHoursPerDay']} hrs, "
              f"Energy Consumption: {device['EnergyConsumption']} kWh, "
              f"Smart Home Efficiency: {'Efficient' if device['SmartHomeEfficiency'] == 1 else 'Inefficient'}")
    
    efficiency = efficiency_calculator.calculate_efficiency(devices)
    print(f"Overall Efficiency: {efficiency}%")

if __name__ == "__main__":
    main()
