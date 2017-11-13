import model_temp
import Controller
import settings
import serial
import serial.tools.list_ports


class com_device:
    """ model class

    attributes = info"""

    def __init__(self, info = None): # roep aan: comlist[<positie>].info
        self.info = info # de ser van de com devcie
        settings.com_list.append(self)
        self.checksensors(self.info)

    def checksensors(self, info):
        if (len(settings.com_list) == 1):
            settings.arduinoconnected = '1'
            settings.afstandconnected = '1'
            self.is_licht_connected(info)
            #self.is_temp_connected(info)
        elif (len(settings.com_list) < 1):
            settings.arduinoconnected = '0'
            settings.afstandconnected = '0'


    # def get_name_type(self):
    #     info = str(self.info.readline())
    #     info = info[2:-1]
    #     self.info.write(b'\xe1')
    #     void = self.info.read() # anders krijg je altijd een 0 als eerste waarde
    #     self.name_type = info


    # def get_temp(self, info):
    #     s = info.read(4) #leest 4 bytes voor de float waarde
    #     man = model_temp.get_temp(s) #krijgt de stringwaarde van de floatwaarde terug
    #     return man


    # def get_light(self, info):
    #     light = info.read()
    #     if light != (b''):
    #         light = int(light.hex(), 16)
    #         return light
    #     return 'nog geen waarde'

    def get_temp_licht(self, info):
        info.write(b'\xe1')
        test = info.read(3)# anders krijg je altijd een 0 als eerste waarde
        return test.hex()

    def aan(self, info):
        info.write(b'\x01')

    # def get_info(self, info):
    #     info.write(b'\xe3')
    #     test = info.read() # anders krijg je altijd een 0 als eerste waarde
    #     print(test.hex())

    def get_data_type(self, info):
        info.write(b'\xe2')
        test = info.read(5)  # anders krijg je altijd een 0 als eerste waarde
        print(test.hex())

    def change_type_write(self, info):
        data = settings.option.get()

        if (data == '1'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x00')
        if (data == '2'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x01')
        if (data == '3'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x02')
        if (data == '4'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x03')
        if (data == '5'):
            info.write(b'\xC8')
            info.write(b'\x04')
            info.write(b'\x04')

    # def is_temp_connected(self,info):
    #     info.write(b'\xe3')
    #     #void = info.read()  # anders krijg je altijd een 0 als eerste waarde
    #     testtemp = str(info.read(2))
    #     print(testtemp)
    #     testtemp = testtemp[0]
    #     lighttemp = testtemp[1]
    #     settings.tempconnected = testtemp
    #     settings.lightconnected = lighttemp
    #     print(testtemp)

    def is_licht_connected(self, info):
        info.read(2);
        info.write(bytes([227]))
        #void = info.read()  # anders krijg je altijd een 0 als eerste waarde
        data = info.read(2)
        data = str(data.hex())
        testtemp = data[1]
        testlicht = data[3]
        print(testlicht)
        settings.tempconnected = testtemp
        settings.lichtconnected = testlicht

    # def get_waardes(self, info):
    #     info.write(b'\xe1')
    #     #void = info.read()  # anders krijg je altijd een 0 als eerste waarde
    #     test = str(info.readline())
    #     print(test)

    def fabrieksinstellingen(self, info):
        info.write(b'\xe4')

    def uit(self, info):
        info.write(b'\x02')

    # def setting(self, info):
    #     info.write(b'200')
    #     info.write(b'200')
    #     info.write(b'200')

    def set_max_distance(self,info):
        maximum = str(settings.max_distance.get())
        if len(maximum) > 0 and maximum.isnumeric():
            maximum = int(maximum)
            if maximum >= 5 and maximum <= 255:
                info.write(b'\xC8')
                info.write(b'\x00')
                info.write(bytes([maximum]))
                print("max: ",bytes([maximum]))
                print("max distance set succes!")
            else:
                Controller.popupmsg("Value out of range 5-255!")

                return False
        else:
            Controller.popupmsg("Please use numbers only!")
            return False

    def set_min_distance(self,info):
        minimum = str(settings.min_distance.get())
        maximum = str(settings.max_distance.get())
        if len(maximum) > 0:
            if len(minimum) > 0 and minimum.isnumeric():
                minimum = int(minimum)
                maximum = int(maximum)
                if minimum < maximum:
                    if minimum >= 5 and minimum <= 255:
                        info.write(b'\xC8')
                        info.write(b'\x01')
                        info.write(bytes([minimum]))
                        print("min: ", bytes([minimum]))
                        print("min distance set succes!")
                    else:
                        Controller.popupmsg("Value out of range 5-255!")
                        return False
                else:
                    Controller.popupmsg("Min must be smaller than Max")
            else:
                Controller.popupmsg("Please use numbers only!")
                return False
        else:
            Controller.popupmsg("Please fill in max first.")

    # toggle light. waardes moeten int zijn tussen 1 en 102
    def set_toggle_light(self,info):
        toggle = str(settings.toggle_light.get())
        if len(toggle) > 0 and toggle.isnumeric():
            toggle = int(toggle)
            if toggle >= 1 and toggle <= 102:
                info.write(b'\xC8')
                info.write(b'\x03')
                info.write(bytes([toggle]))
                print("toggle light: ", bytes([toggle]))
                print("Toggle light set succes!")
            else:
                Controller.popupmsg("Value out of range 1 <-> 102!")
                return False
        else:
            Controller.popupmsg("Please use numbers only!")
            return False
    #toggle temp met waardes tussen de -115 tot en met 141
    def set_toggle_temp(self,info):
        toggle = str(settings.toggle_temp.get())
        if len(toggle) > 0 and toggle.isnumeric():
            toggle = int(toggle)
            if toggle >= -115 and toggle <= 141:
                info.write(b'\xC8')
                info.write(b'\x02')
                info.write(bytes([toggle]))
                print("toggle temp: ", bytes([toggle]))
                print("Toggle light set succes!")
            else:
                Controller.popupmsg("Value out of range -115 <-> 141!")
                return False
        else:
            Controller.popupmsg("Please use numbers only!")
            return False

def init():
    device = serial.tools.list_ports.comports()
    for i in range(0, len(device)):
        com_device(serial.Serial(device[i].device, 19200, timeout=2))