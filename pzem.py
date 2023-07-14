from pymodbus.client import ModbusSerialClient as ModbusClient

# configure the serial port
client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600)

#if windows
#client = ModbusClient(method='rtu', port='com3', baudrate=9600)

#device default address is 0x01. However you can change the address by modifying the register that sets the address
device_address = 0x01

# connect to the PZEM-004T
client.connect()


# read the voltage value
result = client.read_input_registers(0x0000, 1, device_address)
voltage = float(result.registers[0] / 10.0)

# read the current value
result = client.read_input_registers(0x0001, 2, device_address)
current = float(result.registers[0] / 1000.0)

# read the power value
result = client.read_input_registers(0x0003, 2, device_address)
power = float(result.registers[0])

# read energy value
result = client.read_input_registers(0x0005, 2, device_address)
energy = float(result.registers[0])

# read the frequency value
result = client.read_input_registers(0x0007, 1, device_address)
frequency = float(result.registers[0] / 10.0)

#read the power factor value
result = client.read_input_registers(0x0008, 1, device_address)
power_factor = float(result.registers[0] / 100.0)


# print the values
print(f"Voltage: {voltage} V")
print(f"Current: {current} A")
print(f"Power: {power} W")
print(f"Energy: {energy} Wh")
print(f"Frequency: {frequency} Hz")
print(f"Power Factor: {power_factor} ")


# disconnect from the PZEM-004T
client.close()