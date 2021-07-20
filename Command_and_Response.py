from tabulate import tabulate
import random
import time
import serial

ser = serial.Serial('COM4', baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN,
                    stopbits=serial.STOPBITS_ONE, timeout=3)  # open serial port

class serialInterface():
    def menu(self):
        menu = [
            [1, 'HST', 'Temperature Correction Factor Setting'], [2, 'HRT', 'Temperature Correction Factor Read'],
            [3, 'HPO', 'Get The Monitor Information and Status'], [4, 'HGS', 'Get Status'],
            [5, 'HGV', 'Get Output Voltage'], [6, 'HGC', 'Get Output Current'], [7, 'HGT', 'Get MPPC Temperature'],
            [8, 'HOF', 'High Voltage Output OFF'], [9, 'HON', 'High Voltage Output ON'],
            [10, 'HRE', 'Power Supply Reset'],
            [11, 'HCM', 'Switching The Temperature Compensation Mode'],
            [12, 'HBV', 'Reference Voltage Setting']
            ]

        print(tabulate(menu, headers=["\nNo.", "\nCommand Name", "\nFunction"]))

        self.request_com = input("\nENTER THE DESIRED COMMAND")

    def set_values(self):

        deltaPrime_T1 = float(input("\n Set a Δ\'T1 value (mV/°C^2)"))
        while abs(deltaPrime_T1) > 1.507:
            deltaPrime_T1 = float(input("\nInvalid value, input another value"))
        deltaPrime_T1_dec = int(round(deltaPrime_T1 / (1.507 * 10 ** -3), 0))
        deltaPrime_T1_hex = hex(deltaPrime_T1_dec)[2:]
        if len(deltaPrime_T1_hex) < 4:
            diff = 4 - len(deltaPrime_T1_hex)
            for i in range(diff):
                deltaPrime_T1_hex = '0' + deltaPrime_T1_hex
        self.hexstring1 = ''
        self.hexsum1 = '0'
        for i in range(4):
             self.hexstring1 += '\\x' + hex(ord(deltaPrime_T1_hex[i:i + 1]))[2:]
             self.hexsum1 = hex(int(self.hexsum1, 16) + int(self.hexstring1[(len(self.hexstring1)-2):], 16))

        deltaPrime_T2 = float(input("\n Set a Δ\'T2 value (mV/°C^2)"))
        while abs(deltaPrime_T2) > 1.507:
            deltaPrime_T2 = float(input("\nInvalid value, input another value"))
        deltaPrime_T2_dec = int(round(deltaPrime_T2 / (1.507 * 10 ** -3), 0))
        deltaPrime_T2_hex = hex(deltaPrime_T2_dec)[2:]
        if len(deltaPrime_T2_hex) < 4:
            diff = 4 - len(deltaPrime_T2_hex)
            for i in range(diff):
                deltaPrime_T2_hex = '0' + deltaPrime_T2_hex
        self.hexstring2 = ''
        self.hexsum2 = '0'
        for i in range(4):
            self.hexstring2 += '\\x' + hex(ord(deltaPrime_T2_hex[i:i + 1]))[2:]
            self.hexsum2 = hex(int(self.hexsum2, 16) + int(self.hexstring2[(len(self.hexstring2) - 2):], 16))

        delta_T1 = float(input("\n Set a ΔT1 value (mV/°C)"))
        while delta_T1 < 0 or delta_T1 > 3424.20375:
            delta_T1 = float(input("\nInvalid value, input another value"))
        delta_T1_dec = int(round(delta_T1 / (5.225 * 10 ** -2), 0))
        delta_T1_hex = hex(delta_T1_dec)[2:]
        if len(delta_T1_hex) < 4:
            diff = 4 - len(delta_T1_hex)
            for i in range(diff):
                delta_T1_hex = '0' + delta_T1_hex
        self.hexstring3 = ''
        self.hexsum3 = '0'
        for i in range(4):
            self.hexstring3 += '\\x' + hex(ord(delta_T1_hex[i:i + 1]))[2:]
            self.hexsum3 = hex(int(self.hexsum3, 16) + int(self.hexstring3[(len(self.hexstring3) - 2):], 16))

        delta_T2 = float(input("\n Set a ΔT2 value (mV/°C)"))
        while delta_T2 < 0 or delta_T2 > 3424.20375:
            delta_T2 = float(input("\nInvalid value, input another value"))
        delta_T2_dec = int(round(delta_T2 / (5.225 * 10 ** -2), 0))
        delta_T2_hex = hex(delta_T2_dec)[2:]
        if len(delta_T2_hex) < 4:
            diff = 4 - len(delta_T2_hex)
            for i in range(diff):
                delta_T2_hex = '0' + delta_T2_hex
        self.hexstring4 = ''
        self.hexsum4 = '0'
        for i in range(4):
            self.hexstring4 += '\\x' + hex(ord(delta_T2_hex[i:i + 1]))[2:]
            self.hexsum4 = hex(int(self.hexsum4, 16) + int(self.hexstring4[(len(self.hexstring4) - 2):], 16))


        Vb = float(input("\n Set a Vb value (V)"))
        while Vb < 0 or Vb > 118.74942:
            Vb = float(input("\nInvalid value, input another value"))
        Vb_dec = int(round(Vb / (1.812 * 10 ** -3), 0))
        Vb_hex = hex(Vb_dec)[2:]
        if len(Vb_hex) < 4:
            diff = 4 - len(Vb_hex)
            for i in range(diff):
                Vb_hex = '0' + Vb_hex
        self.hexstring5 = ''
        self.hexsum5 = '0'
        for i in range(4):
            self.hexstring5 += '\\x' + hex(ord(Vb_hex[i:i + 1]))[2:]
            self.hexsum5 = hex(int(self.hexsum5, 16) + int(self.hexstring5[(len(self.hexstring5) - 2):], 16))

        Tb = float(input("\n Set a Tb value (°C)"))
        while Tb < -39.0459 or Tb > 188.1818:
            Tb = float(input("\nInvalid value, input another value"))
        Tb_dec = int(round((1.035 + (Tb * -5.5 * 10 ** -3)) / (1.907 * 10 ** -5), 0))
        Tb_hex = hex(Tb_dec)[2:]
        if len(Tb_hex) < 4:
            diff = 4 - len(Tb_hex)
            for i in range(diff):
                Tb_hex = '0' + Tb_hex
        self.hexstring6 = ''
        self.hexsum6 = '0'
        for i in range(4):
            self.hexstring6 += '\\x' + hex(ord(Tb_hex[i:i + 1]))[2:]
            self.hexsum6 = hex(int(self.hexsum6, 16) + int(self.hexstring6[(len(self.hexstring6) - 2):], 16))

        self.hexstring = self.hexstring1 + self.hexstring2 + self.hexstring3 + self.hexstring4 + self.hexstring5 + self.hexstring6
        self.hexsum = hex(int(self.hexsum1, 16) + int(self.hexsum2, 16) + int(self.hexsum3, 16) + int(self.hexsum4, 16)\
                      + int(self.hexsum5, 16) + int(self.hexsum6, 16))

        print("\nThe Following Variables Have Been Set:")

        data = [
            ['Δ\'T1', str(deltaPrime_T1) + ' mV/°C^2'], ['Δ\'T2', str(deltaPrime_T2) + ' mV/°C^2'],
            ['ΔT1', str(delta_T1) + ' mV/°C'], ['ΔT2', str(delta_T2) + ' mV/°C'], ['Vb', str(Vb) + ' V'],
            ['Tb', str(Tb) + ' °C']
        ]

        print(tabulate(data, headers=["\nVariable", "\nUser Input Value"]))
        time.sleep(2)
        answer = input(
            "\nDo these values make sense to you? (If not, type \"no\" to retype your values and if yes, type "
            "\"yes\" to confirm values)")
        if answer == "yes":
            return self.hexstring, self.hexsum

        elif answer == "no":
            self.set_values()
        else:
            print("\nInvalid Response")


    def encode(self, request_com='', data=[]):
        self.STX_asc = '\\x' + hex(2)[2:]   #ASCII CODE FOR 'STX', 'ETX', AND 'CR'
        self.ETX_asc = '\\x' + hex(3)[2:]
        self.CR_asc = '\\x' + hex(13)[2].upper()
        com_char1_asc = '\\x' + hex(ord(request_com[0]))[2:].upper()   #ASCII CODE FOR THE 3 BYTES OF THE THREE-LETTER COMMAND
        com_char2_asc = '\\x' + hex(ord(request_com[1]))[2:].upper()
        com_char3_asc = '\\x' + hex(ord(request_com[2]))[2:].upper()

        data_asc_sum = data[1]

        check_sum = hex(
            int(self.STX_asc[2:], 16) + int(com_char1_asc[2:], 16) + int(com_char2_asc[2:], 16) + int(com_char3_asc[2:], 16) +
            int(data_asc_sum, 16) + int(self.ETX_asc[2:], 16))

        last_two = str(hex(int(check_sum, 16) % int('1000', 16))[2:]).upper()
        second_to_last = last_two[len(last_two) - 2]
        last = last_two[len(last_two) - 1]
        second_to_last_asc = '\\x' + hex(ord(second_to_last))[2:]
        last_asc = '\\x' + hex(ord(last))[2:]

        request_hexstring = self.STX_asc + com_char1_asc + com_char2_asc + com_char3_asc + data[0] + self.ETX_asc +\
                            second_to_last_asc + last_asc + self.CR_asc

        #print(request_hexstring)
        return request_hexstring



    def decode(self, request_hexstring=''):
        l = list(request_hexstring)
        del (l[0])
        del (l[-6:])
        useful_hexstring = "".join(l)
        response_com = ''
        response_data_hexstring = ''

        for i in range(0, len(useful_hexstring[0:6]), 2):
            response_com += chr(int(useful_hexstring[i:i + 2], 16)).lower()


        if response_com in ["hgs", "hgv", "hgt"]:
            for i in range(4):
                x = [random.randint(30, 39), random.randint(41, 46)]    #EXAMPLE response_data_hexstring = 30454139
                response_data_hexstring += str(random.choice(x))

        if response_com == "hgc":
            for i in range(2):
                x = [random.randint(30, 39), random.randint(41, 46)]
                response_data_hexstring += str(random.choice(x))
            response_data_hexstring = str(random.randint(30, 34)) + response_data_hexstring
            if response_data_hexstring[0:2] == '34':
                l = list(response_data_hexstring)
                l[2] = '3'
                l[3] = '0'
                l[4] = '3'
                l[5] = '0'
                response_data_hexstring = "".join(l)
            response_data_hexstring = '30' + response_data_hexstring

        if response_com == "hrt":
            response_data_hexstring = self.hexstring1 + self.hexstring2 + self.hexstring3 + self.hexstring4 + \
                                      self.hexstring5 + self.hexstring6


        return response_com, response_data_hexstring



    def setsixVariables(self):
        request_com = self.request_com
        data = self.set_values()
        request_hexstring = self.encode(request_com, data)
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(8)
        print(response_ascii_string)
        time.sleep(2)

    def readsixVariables(self):
        request_com = self.request_com
        request_hexstring = '\x02\x48\x52\x54\x03\x46\x33\x0D'
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = str(ser.read(32))
        deltaPrimeT1_val = response_ascii_string[9:13]
        deltaPrimeT2_val = response_ascii_string[13:17]
        deltaT1_val = response_ascii_string[17:21]
        deltaT2_val = response_ascii_string[21:25]
        Vb_val = response_ascii_string[25:29]
        Tb_val = response_ascii_string[29:33]

        deltaPrimeT1_dec = int(deltaPrimeT1_val, 16)
        deltaPrimeT1 = round(deltaPrimeT1_dec * 1.507 * 10 ** -3, 2)

        deltaPrimeT2_dec = int(deltaPrimeT2_val, 16)
        deltaPrimeT2 = round(deltaPrimeT2_dec * 1.507 * 10 ** -3, 2)

        deltaT1_dec = int(deltaT1_val, 16)
        deltaT1 = round(deltaT1_dec * 5.225 * 10 ** -2, 2)

        deltaT2_dec = int(deltaT2_val, 16)
        deltaT2 = round(deltaT2_dec * 5.225 * 10 ** -2, 2)

        Vb_dec = int(Vb_val, 16)
        Vb = round(Vb_dec * 1.812 * 10 ** -3, 2)

        Tb_dec = int(Tb_val, 16)
        Tb = round((Tb_dec * 1.907 * 10 ** -5 - 1.035) / (-5.5 * 10 ** -3), 2)

        readData = [
            ['Δ\'T1', str(deltaPrimeT1) + ' mV/°C^2'], ['Δ\'T2', str(deltaPrimeT2) + ' mV/°C^2'],
            ['ΔT1', str(deltaT1) + ' mV/°C'], ['ΔT2', str(deltaT2) + ' mV/°C'],
            ['Vb', str(Vb) + ' V'],
            ['Tb', str(Tb) + ' °C']
        ]
        print(tabulate(readData, headers=["\nVariable", "\nExisting Value"]))

        time.sleep(2)

    def getmonitorinfoStatus(self):
        request_com = self.request_com
        request_hexstring = '\x02\x48\x50\x4F\x03\x45\x43\x0D'
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = str(ser.read(32))
        status_val = response_ascii_string[9:13]
        output_voltage_val = response_ascii_string[17:21]
        output_current_val = response_ascii_string[21:25]
        MPPC_temp_val = response_ascii_string[25:29]

        status_bin = bin(int(status_val, 16))[2:]

        output_voltage_dec = int(output_voltage_val, 16)
        output_voltage = round(output_voltage_dec * 1.812 * 10 ** -3, 2)

        output_current_dec = int(output_current_val, 16)
        output_current = round(output_current_dec * 4.980 * 10 ** -3, 2)

        MPPC_temp_dec = int(MPPC_temp_val, 16)
        MPPC_temp = round((MPPC_temp_dec * 1.907 * 10 ** -5 - 1.035) / (-5.5 * 10 ** -3), 2)

        readData = [
            ['Status', str(status_bin)], ['Output Voltage', str(output_voltage) + 'V'],
            ['Output Current', str(output_current) + 'mA'], ['MPPC Temperature', str(MPPC_temp) + '°C'],
                   ]

        print(tabulate(readData, headers=["\nVariable", "\nExisting Value"]))

        time.sleep(2)


    def getStatus(self):
        request_com = self.request_com
        request_hexstring = '\x02\x48\x47\x53\x03\x45\x37\x0D'
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = str(ser.read(12))
        output_status_hex = response_ascii_string[9:13]
        status_bin = bin(int(output_status_hex, 16))[2:]
        print("\n" + status_bin)

        if status_bin[6] == '1':
            status_bin_val_6 = 1
            status_bin_des_6 = 'ON'
        else:
            status_bin_val_6 = 0
            status_bin_des_6 = 'OFF'

        if status_bin[5] == '1':
            status_bin_val_5 = 1
            status_bin_des_5 = 'Working Protection'
        else:
            status_bin_val_5 = 0
            status_bin_des_5 = 'Not Working'

        if status_bin[4] == '1':
            status_bin_val_4 = 1
            status_bin_des_4 = 'Outside Specification'
        else:
            status_bin_val_4 = 0
            status_bin_des_4 = 'Within Specification'

        if status_bin[3] == '1':
            status_bin_val_3 = 1
            status_bin_des_3 = 'Connect'
        else:
            status_bin_val_3 = 0
            status_bin_des_3 = 'Disconnect'

        if status_bin[2] == '1':
            status_bin_val_2 = 1
            status_bin_des_2 = 'Outside Specification'
        else:
            status_bin_val_2 = 0
            status_bin_des_2 = 'Within Specification'

        if status_bin[0] == '1':
            status_bin_val_0 = 1
            status_bin_des_0 = 'Effectiveness'
        else:
            status_bin_val_0 = 0
            status_bin_des_0 = 'Invalid'

        status_table = [
                [0, 'High Voltage Output', status_bin_val_6, status_bin_des_6],
                [1, 'Overcurrent Protection', status_bin_val_5, status_bin_des_5],
                [2, 'Output Current Value', status_bin_val_4, status_bin_des_4],
                [3, 'Temperature Sensor Connect', status_bin_val_3, status_bin_des_3],
                [4, 'Operation Temperature Limit', status_bin_val_2, status_bin_des_2],
                [5, 'Reserve 5', "_______", "_____________________"],
                [6, 'Temperature Correction', status_bin_val_0, status_bin_des_0],
                [7, 'Reserve 7', "_______", "_____________________"],
                [8, 'Reserve 8', "_______", "_____________________"],
                [9, 'Reserve 9', "_______", "_____________________"],
                [10, 'Reserve 10', "_______", "_____________________"],
                [11, 'Reserve 11', "_______", "_____________________"],
                [12, 'Reserve 12', "_______", "_____________________"],
                [13, 'Reserve 13', "_______", "_____________________"],
                [14, 'Reserve 14', "_______", "_____________________"],
                [15, 'Reserve 15', "_______", "_____________________"],

                      ]

        print(tabulate(status_table, headers=["\nBit.", "\nStatus", "\nValue", "\nDescription"]))
        time.sleep(2)

    def voltageOut(self):
        request_hexstring = '\x02\x48\x47\x56\x03\x45\x41\x0D'  #h02 h48 h47 h56 h03 h45 h41 h0D
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(12)
        output_voltage_hex = str(response_ascii_string)[9:13]
        output_voltage = round(int(output_voltage_hex, 16) * 1.812 * 10 ** -3, 2)
        print(str(output_voltage) + "V")
        time.sleep(2)


    def currentOut(self):
        request_hexstring = '\x02\x48\x47\x43\x03\x44\x37\x0D'  # h02 h48 h47 h43 h03 h44 h37 h0D
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(12)
        output_current_hex = str(response_ascii_string)[9:13]
        output_current = round(int(output_current_hex, 16) * 4.980 * 10 ** -3, 2)
        print(str(output_current) + "mA")
        time.sleep(2)

    def MPPCOUT(self):
        request_hexstring = '\x02\x48\x47\x54\x03\x45\x38\x0D'  # h02 h48 h47 h54 h03 h45 h38 h0D
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(12)
        output_MPPCtemp_hex = str(response_ascii_string)[9:13]
        output_MPPCtemp = round((int(output_MPPCtemp_hex, 16) * 1.907 * 10 ** -5 - 1.035) / (-5.5 * 10 ** -3), 2)
        print(str(output_MPPCtemp) + "°C")
        time.sleep(2)

    def turnvoltageOFF(self):
        request_hexstring = '\x02\x48\x4F\x46\x03\x45\x32\x0D'  # h02 h48 h4F h46 h03 h45 h32 h0D
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(12)
        print(response_ascii_string)
        print("High Voltage Output is OFF")

    def turnvoltageON(self):
        request_hexstring = '\x02\x48\x4F\x4E\x03\x45\x41\x0D'  # h02 h48 h4F h4E h03 h45 h41 h0D
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(12)
        print(response_ascii_string)
        print("High Voltage Output is ON")

    def resetPower(self):
        request_hexstring = '\x02\x48\x52\x45\x03\x45\x34\x0D'  # h02 h48 h52 h45 h03 h45 h34 h0D
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(12)
        print(response_ascii_string)
        print("The Power Will Reset")

    def tempcompMode(self):
        request_com = self.request_com
        answer = input("\nDo you want to enable or disable the temperature correction function? "
                       "(Type 1 to enable ""or Type 0 to disable)")

        if answer == '0':
            request_hexstring = '\x02\x48\x43\x4D\x30\x03\x30\x44\x0D'  # h02 h48 h43 h4D h30 h03 h30 h44 h0D
            ser.write(request_hexstring.encode('utf-8'))
        if answer == '1':
            request_hexstring = '\x02\x48\x43\x4D\x31\x03\x30\x45\x0D'  # h02 h48 h43 h4D h31 h03 h30 h45 h0D
            ser.write(request_hexstring.encode('utf-8'))

        response_ascii_string = str(ser.read(12))
        print(response_ascii_string)
        time.sleep(2)

    def referencevoltageSetting(self):
        request_com = self.request_com
        Vb = float(input("\n Set a Vb value (V)"))
        while Vb < 0 or Vb > 118.74942:
            Vb = float(input("\nInvalid value, input another value"))
        Vb_dec = int(round(Vb / (1.812 * 10 ** -3), 0))
        Vb_hex = hex(Vb_dec)[2:]
        if len(Vb_hex) < 4:
            diff = 4 - len(Vb_hex)
            for i in range(diff):
                Vb_hex = '0' + Vb_hex
        self.hexstring5 = ''
        self.hexsum5 = '0'
        for i in range(4):
            self.hexstring5 += '\\x' + hex(ord(Vb_hex[i:i + 1]))[2:]
            self.hexsum5 = hex(int(self.hexsum5, 16) + int(self.hexstring5[(len(self.hexstring5) - 2):], 16))

        data = [self.hexstring5, self.hexsum5]
        request_hexstring = self.encode(request_com, data)
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(8)
        print(response_ascii_string)
        time.sleep(2)

    def commandsList(self):
        if self.request_com == 'HST':
            self.setsixVariables()

        if self.request_com == 'HRT':
            self.readsixVariables()

        if self.request_com == 'HPO':
            self.getmonitorinfoStatus()

        if self.request_com == 'HGS':
            self.getStatus()

        if self.request_com == 'HGV':
            self.voltageOut()

        if self.request_com == 'HGC':
            self.currentOut()

        if self.request_com == 'HGT':
            self.MPPCOUT()

        if self.request_com == 'HOF':
            self.turnvoltageOFF()

        if self.request_com == 'HON':
            self.turnvoltageON()

        if self.request_com == 'HRE':
            self.resetPower()

        if self.request_com == 'HCM':
            self.tempcompMode()

    def run(self):
        while 1 > 0:
            self.menu()
            self.commandsList()


test = serialInterface()

test.run()
