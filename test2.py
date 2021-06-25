from tabulate import tabulate
import random

from tabulate import tabulate
import random
import time

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
        for i in range(4):
             self.hexstring1 += hex(ord(deltaPrime_T1_hex[i:i + 1]))[2:]

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
        for i in range(4):
            self.hexstring2 += hex(ord(deltaPrime_T2_hex[i:i + 1]))[2:]

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
        for i in range(4):
            self.hexstring3 += hex(ord(delta_T1_hex[i:i + 1]))[2:]

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
        for i in range(4):
            self.hexstring4 += hex(ord(delta_T2_hex[i:i + 1]))[2:]


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
        for i in range(4):
            self.hexstring5 += hex(ord(Vb_hex[i:i + 1]))[2:]

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
        for i in range(4):
            self.hexstring6 += hex(ord(Tb_hex[i:i + 1]))[2:]

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
            return self.hexstring1 + self.hexstring2 + self.hexstring3 + self.hexstring4 + self.hexstring5 + self.hexstring6
        elif answer == "no":
            self.set_values()
        else:
            print("\nInvalid Response")


    def encode(self, request_com='', data=''):
        self.STX_asc = hex(2)[2:]   #ASCII CODE FOR 'STX', 'ETX', AND 'CR'
        self.ETX_asc = hex(3)[2:]
        self.CR_asc = hex(13)[2].upper()
        com_char1_asc = hex(ord(request_com[0]))[2:].upper()   #ASCII CODE FOR THE 3 BYTES OF THE THREE-LETTER COMMAND
        com_char2_asc = hex(ord(request_com[1]))[2:].upper()
        com_char3_asc = hex(ord(request_com[2]))[2:].upper()

        data_asc_sum = 0
        for i in range(0, len(data), 2):
            data_asc_sum += int(data[i:i + 2], 16)

        check_sum = hex(
            int(self.STX_asc, 16) + int(com_char1_asc, 16) + int(com_char2_asc, 16) + int(com_char3_asc, 16) +
            data_asc_sum + int(self.ETX_asc, 16))

        last_two = str(hex(int(check_sum, 16) % int('1000', 16))[2:]).upper()
        second_to_last = last_two[len(last_two) - 2]
        last = last_two[len(last_two) - 1]
        second_to_last_asc = hex(ord(second_to_last))[2:]
        last_asc = hex(ord(last))[2:]

        request_hexstring = self.STX_asc + com_char1_asc + com_char2_asc + com_char3_asc + data + self.ETX_asc +\
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
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == 'hst':
            print("\nVariables are successfully set!")
            time.sleep(2)

    def readsixVariables(self):
        request_com = self.request_com
        data = ''
        request_hexstring = self.encode(request_com, data)
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == 'hrt':
            deltaPrimeT1_val = ''
            deltaPrimeT2_val = ''
            deltaT1_val = ''
            deltaT2_val = ''
            Vb_val = ''
            Tb_val = ''
            for i in range(0, 7, 2):
                deltaPrimeT1_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))
            for i in range(8, 15, 2):
                deltaPrimeT2_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))
            for i in range(16, 23, 2):
                deltaT1_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))
            for i in range(24, 31, 2):
                deltaT2_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))
            for i in range(32, 39, 2):
                Vb_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))
            for i in range(40, 47, 2):
                Tb_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))

            deltaPrimeT1_dec = int(deltaPrimeT1_val, 16)
            deltaPrimeT1 = deltaPrimeT1_dec * 1.507*10**-3

            deltaPrimeT2_dec = int(deltaPrimeT2_val, 16)
            deltaPrimeT2 = deltaPrimeT2_dec * 1.507 * 10 ** -3

            deltaT1_dec = int(deltaT1_val, 16)
            deltaT1 = deltaT1_dec * 5.225 * 10 ** -2

            deltaT2_dec = int(deltaT2_val, 16)
            deltaT2 = deltaT2_dec * 5.225 * 10 ** -2

            Vb_dec = int(Vb_val, 16)
            Vb = Vb_dec * 1.812 * 10 ** -3

            Tb_dec = int(Tb_val, 16)
            Tb = (Tb_dec * 1.907 * 10**-5 - 1.035)/(-5.5 * 10**-3)

            readData = [
                ['Δ\'T1', str(deltaPrimeT1) + ' mV/°C^2'], ['Δ\'T2', str(deltaPrimeT2) + ' mV/°C^2'],
                ['ΔT1', str(deltaT1) + ' mV/°C'], ['ΔT2', str(deltaT2) + ' mV/°C'],
                ['Vb', str(Vb) + ' V'],
                ['Tb', str(Tb) + ' °C']
            ]
            print(tabulate(readData, headers=["\nVariable", "\nExisting Value"]))

        time.sleep(2)


    def getStatus(self):
        request_com = self.request_com
        data = ''
        request_hexstring = self.encode(request_com, data)
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == 'hgs':
            response_data_val = ''
            for i in range(0, len(response_com_and_datastring[1]), 2):
                response_data_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))
            status_dec = int(response_data_val, 16)
            status_bin = bin(status_dec)[2:]
            print("\n" + status_bin)
            time.sleep(2)

    def voltageOut(self):
        request_com = self.request_com
        data = ''
        request_hexstring = self.encode(request_com, data)
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == 'hgv':
            response_data_val = ''
            for i in range(0, len(response_com_and_datastring[1]), 2):
                response_data_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))
            voltage_out_dec = int(response_data_val, 16)
            voltage_out = round(voltage_out_dec * 1.812*10**-3, 2)
            print("\nThe Output Voltage is " + str(voltage_out) + "V")
            time.sleep(2)


    def currentOut(self):
        request_com = self.request_com
        data = ''
        request_hexstring = self.encode(request_com, data)
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == 'hgc':
            response_data_val = ''
            for i in range(0, len(response_com_and_datastring[1]), 2):
                response_data_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))
            current_out_dec = int(response_data_val, 16)
            current_out = round(current_out_dec * 4.980*10**-3, 2)
            print("\nThe Output Current is " + str(current_out) + "mA")
            time.sleep(2)

    def MPPCOUT(self):
        request_com = self.request_com
        data = ''
        request_hexstring = self.encode(request_com, data)
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == 'hgt':
            response_data_val = ''
            for i in range(0, len(response_com_and_datastring[1]), 2):
                response_data_val += chr(int(response_com_and_datastring[1][i:i + 2], 16))
            MPPC_temp_dec = int(response_data_val, 16)
            MPPC_temp = round((MPPC_temp_dec * 1.907 * 10 ** -5 - 1.035) / (-5.5 * 10 ** -3), 2)
            print("\nThe Output MPPC Temperature is " + str(MPPC_temp) + "°C")
            time.sleep(2)

    def turnvoltageOFF(self):
        request_com = self.request_com
        data = ''
        request_hexstring = self.encode(request_com, data)
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == "hof":
            print("High Voltage Output is OFF")
            time.sleep(2)

    def turnvoltageON(self):
        request_com = self.request_com
        data = ''
        request_hexstring = self.encode(request_com, data)
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == "hon":
            print("High Voltage Output is ON")
            time.sleep(2)

    def resetPower(self):
        request_com = self.request_com
        data = ''
        request_hexstring = self.encode(request_com, data)
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == "hre":
            print("The Power Will Reset Shortly...")
            time.sleep(2)

    def tempcompMode(self):
        request_com = self.request_com
        answer = input("\nDo you want to enable or disable the temperature correction function? "
                       "(Type 1 to enable ""or Type 0 to disable)")

        data = hex(ord(answer))[2:]
        request_hexstring = self.encode(request_com, data)
        response_com_and_datastring = self.decode(request_hexstring)
        if response_com_and_datastring[0] == "hcm":
            print("\nYou Successfully Switched")
            time.sleep(2)

    def commandsList(self):
        if self.request_com == 'HST':
            self.setsixVariables()

        if self.request_com == 'HRT':
            self.readsixVariables()

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