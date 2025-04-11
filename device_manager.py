import pandas as pd

class DeviceManager:
    def __init__(self, csv_path):
        # Load device data from CSV file
        self.devices = pd.read_csv(csv_path)

    def get_devices(self):
        # Convert the dataframe to a list of dictionaries for compatibility
        devices_list = self.devices.to_dict(orient='records')
        return devices_list

    def toggle_device(self, device_id):
        # Toggle the device status in the CSV data
        device_row = self.devices[self.devices['serID'] == device_id]
        if not device_row.empty:
            current_status = device_row['SmartHomeEfficiency'].values[0]
            new_status = 0 if current_status == 1 else 1
            self.devices.loc[self.devices['serID'] == device_id, 'SmartHomeEfficiency'] = new_status
            self.devices.to_csv('updated_devices.csv', index=False)  # Save to CSV after toggle
            return f"Device with ID {device_id} is now {'efficient' if new_status == 1 else 'inefficient'}."
        return f"Device with ID {device_id} not found."
