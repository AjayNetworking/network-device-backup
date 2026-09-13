from netmiko import ConnectHandler


device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "YOUR_PASSWORD",
}


print("Connecting to device...")

connection = ConnectHandler(**device)

print("Connected successfully!")

output = connection.send_command("show running-config")

print(output)

connection.disconnect()

print("Disconnected.")
