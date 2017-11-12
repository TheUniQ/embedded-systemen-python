import model_temp
import settings
import serial
import serial.tools.list_ports


class com_device:
    """ model class

    attributes = info"""

    def __init__(self, info = None, name_type = None): # roep aan: comlist[<positie>].info
        print(info)
        self.info = info # de ser van de com devcie
        self.name_type = name_type
        print(self.info)
        settings.com_list.append(self)
        self.checksensors(settings.com_list[0].info)

    def checksensors(self, info):
        if (len(settings.com_list) == 1):
            settings.arduinoconnected = '1'
            settings.afstandconnected = '1'
            self.is_licht_connected(info)
            self.is_temp_connected(info)
        elif (len(settings.com_list) < 1):
            settings.arduinoconnected = '0'
            settings.afstandconnected = '0'


    def get_name_type(self): 
        info = str(self.info.readline())
        info = info[2:-1]
        self.info.write(b'\xe1')
        void = self.info.read() # anders krijg je altijd een 0 als eerste waarde
        self.name_type = info


    def get_temp(self, info):
        s = info.read(4) #leest 4 bytes voor de float waarde
        man = model_temp.get_temp(s) #krijgt de stringwaarde van de floatwaarde terug
        return man


    def get_light(self, info):
        light = info.read()
        if light != (b''):
            light = int(light.hex(), 16)
            return light
        return 'nog geen waarde'

    def get_temp_licht(self, info):
        info.write(b'\xe1')
        void = info.read()  # anders krijg je altijd een 0 als eerste waarde
        test = str(info.readline())
        print(test)


    def aan(self, info):
        print(self, info)
        info.write(b'\x01')

    def is_licht_connected(self, info):
        info.write(b'\xe3')
        void = info.read()  # anders krijg je altijd een 0 als eerste waarde
        testlicht = str(info.readline())
        testlicht = testlicht[-2]
        settings.lichtconnected = testlicht
        print(testlicht)


    def get_info(self, info):
        info.write(b'\xe3')
        void = info.read()  # anders krijg je altijd een 0 als eerste waarde
        test = str(info.readline())
        print(test)

    def get_data_type(self, info):
        info.write(b'\xe2')
        void = info.read()  # anders krijg je altijd een 0 als eerste waarde
        test = str(info.readline())
        print(test)

    def change_type_write(self, info):
        data = settings.option.get()

        if (data == '0'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x00')
        if (data == '1'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x01')
        if (data == '2'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x02')
        if (data == '3'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x03')
        if (data == '4'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x04')



    def is_temp_connected(self,info):
        info.write(b'\xe3')
        void = info.read()  # anders krijg je altijd een 0 als eerste waarde
        testtemp = str(info.readline())
        testtemp = testtemp[-7]
        settings.tempconnected = testtemp
        print(testtemp)

    def get_waardes(self, info):
        info.write(b'\xe1')
        void = info.read()  # anders krijg je altijd een 0 als eerste waarde
        test = str(info.readline())
        print(test)

    def uit(self, info):
        info.write(b'\x02')

    def setting(self, info):
        info.write(b'200')
        info.write(b'200')
        info.write(b'200')



    def set_max_distance(self,info):
        maximum = int(str(settings.max_distance.get()))
        info.write(b'\xC8')
        info.write(b'\x00')
        info.write(bytes([maximum]))

    def set_min_distance(self,info):
        minimum = int(str(settings.min_distance.get()))
        info.write(b'\xC8')
        info.write(b'\x01')
        info.write(bytes([minimum]))

def init():
    device = serial.tools.list_ports.comports()
    for i in range(0, len(device)):
        com_device(serial.Serial(device[i].device, 19200, timeout=2))
    for i in settings.com_list:
        i.get_name_type()