
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

if __name__ == "__main__":
        # Connect to the slave
        serial = serial.Serial(
                               port='com5', #'/dev/ttyUSB0',
                               baudrate=9600,
                               bytesize=8,
                               parity='N',
                               stopbits=1,
                               xonxoff=0
                              )
       # print(answer)
        master = modbus_rtu.RtuMaster(serial)
        master.set_timeout(2.0)
        master.set_verbose(True)
        
        #El primer parámetro es el número referente a la dirección del sensor que se quiere modificar,o sea,
        #si el sensor a modificar tiene como dirección 0x006, en ese primer parámetro se coloca 6.
        #En el último parámetro se coloca la dirección que quisieran que tenga el sensor.
        #Cada sensor del canal de comunicación tiene que tener una dirección diferente.
        
        '''
        The first parameter is the address of the device that will be modified, i.e if sensor has addres 0x06,
        in that parameter you write 6. The last parameter output_value you put the new address you want the sensor to have.
        each sensor in the same channel must have different address.
        '''
        master.execute(1, cst.WRITE_SINGLE_REGISTER,2,output_value=0x002)