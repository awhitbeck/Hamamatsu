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
            [12, 'HBV', 'Reference Voltage Temporary Setting']
            ]

        print(tabulate(menu, headers=["\nNo.", "\nCommand Name", "\nFunction"]))

        self.com = input("\nENTER THE DESIRED COMMAND")

    def set_values(self):

        self.deltaPrime_T1 = float(input("\n Set a Δ\'T1 value (mV/°C^2)"))
        while abs(self.deltaPrime_T1) > 1.507:
            self.deltaPrime_T1 = float(input("\nInvalid value, input another value"))
        deltaPrime_T1_dec = int(round(self.deltaPrime_T1 / (1.507 * 10 ** -3), 0))
        self.deltaPrime_T1_hex = hex(deltaPrime_T1_dec)[2:]
        if len(self.deltaPrime_T1_hex) < 4:
            diff = 4 - len(self.deltaPrime_T1_hex)
            for i in range(diff):
                self.deltaPrime_T1_hex = '0' + self.deltaPrime_T1_hex

        self.deltaPrime_T2 = float(input("\n Set a Δ\'T2 value (mV/°C^2)"))
        while abs(self.deltaPrime_T2) > 1.507:
            self.deltaPrime_T2 = float(input("\nInvalid value, input another value"))
        deltaPrime_T2_dec = int(round(self.deltaPrime_T2 / (1.507 * 10 ** -3), 0))
        self.deltaPrime_T2_hex = hex(deltaPrime_T2_dec)[2:]
        if len(self.deltaPrime_T2_hex) < 4:
            diff = 4 - len(self.deltaPrime_T2_hex)
            for i in range(diff):
                self.deltaPrime_T2_hex = '0' + self.deltaPrime_T2_hex


        self.delta_T1 = float(input("\n Set a ΔT1 value (mV/°C)"))
        while self.delta_T1 < 0 or self.delta_T1 > 3424.20375:
            self.delta_T1 = float(input("\nInvalid value, input another value"))
        delta_T1_dec = int(round(self.delta_T1 / (5.225 * 10 ** -2), 0))
        self.delta_T1_hex = hex(delta_T1_dec)[2:]
        if len(self.delta_T1_hex) < 4:
            diff = 4 - len(self.delta_T1_hex)
            for i in range(diff):
                self.delta_T1_hex = '0' + self.delta_T1_hex

        self.delta_T2 = float(input("\n Set a ΔT2 value (mV/°C)"))
        while self.delta_T2 < 0 or self.delta_T2 > 3424.20375:
            self.delta_T2 = float(input("\nInvalid value, input another value"))
        delta_T2_dec = int(round(self.delta_T2 / (5.225 * 10 ** -2), 0))
        self.delta_T2_hex = hex(delta_T2_dec)[2:]
        if len(self.delta_T2_hex) < 4:
            diff = 4 - len(self.delta_T2_hex)
            for i in range(diff):
                self.delta_T2_hex = '0' + self.delta_T2_hex


        self.Vb = float(input("\n Set a Vb value (V)"))
        while self.Vb < 0 or self.Vb > 118.74942:
            self.Vb = float(input("\nInvalid value, input another value"))
        Vb_dec = int(round(self.Vb / (1.812 * 10 ** -3), 0))
        self.Vb_hex = hex(Vb_dec)[2:]
        if len(self.Vb_hex) < 4:
            diff = 4 - len(self.Vb_hex)
            for i in range(diff):
                self.Vb_hex = '0' + self.Vb_hex

        self.Tb = float(input("\n Set a Tb value (°C)"))
        while self.Tb < -39.0459 or self.Tb > 188.1818:
            self.Tb = float(input("\nInvalid value, input another value"))
        Tb_dec = int(round((1.035 + (self.Tb * -5.5 * 10 ** -3)) / 1.907 * 10 ** -5, 0))
        self.Tb_hex = hex(Tb_dec)[2:]
        if len(self.Tb_hex) < 4:
            diff = 4 - len(self.Tb_hex)
            for i in range(diff):
                self.Tb_hex = '0' + self.Tb_hex

        print("\nThe Following Variables Have Been Set:")

        data = [
            ['Δ\'T1', str(self.deltaPrime_T1) + ' mV/°C^2'], ['Δ\'T2', str(self.deltaPrime_T2) + ' mV/°C^2'],
            ['ΔT1', str(self.delta_T1) + ' mV/°C'], ['ΔT2', str(self.delta_T2) + ' mV/°C'], ['Vb', str(self.Vb) + ' V'],
            ['Tb', str(self.Tb) + ' °C']
        ]

        print(tabulate(data, headers=["\nVariable", "\nUser Input Value"]))
        time.sleep(2)
        answer = input(
            "\nDo these values make sense to you? (If not, type \"no\" to retype your values and if yes, type "
            "\"yes\" to confirm values)")
        if answer == "yes":
            print("")
        elif answer == "no":
            self.set_values()
        else:
            print("\nInvalid Response")


    def encode(self):
        self.STX_asc = hex(2)   #ASCII CODE FOR 'STX', 'ETX', AND 'CR'
        self.ETX_asc = hex(3)
        self.CR_asc = hex(13)[0] + hex(13)[1] + hex(13)[2].upper()
        com_char1_asc = hex(ord(self.com[0]))   #ASCII CODE FOR THE 3 BYTES OF THE THREE-LETTER COMMAND
        com_char2_asc = hex(ord(self.com[1]))
        com_char3_asc = hex(ord(self.com[2]))

        encode = [
            ['ASCII Code', 'STX', self.com[0], self.com[1], self.com[2], "ETX", "CS", "CS", "CR"],
            ['Size(Byte)', self.STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, self.ETX_asc, "CS", "CS", self.CR_asc]
                 ]

        for i in range(self.x):  # APPENDS THE TABLE IN THE MIDDLE CREATING EMPTY BYTES FOR DATA
            encode[0].append("")
            encode[1].append("")
            for n in range(4):
                encode[0][9 - n + i] = encode[0][8 - n + i]
                encode[1][9 - n + i] = encode[1][8 - n + i]
            encode[0][5 + i] = ""
            encode[1][5 + i] = ""

        if self.com == "HST":

            for i in range(4): #PUTS EACH HEX CHARACTER IN THE CORRESPONDING 24 BYTE SLOTS IN THE TABLE (6 VARIABLES)
                encode[0][5 + i] = self.deltaPrime_T1_hex[i]
                encode[1][5 + i] = hex(ord(self.deltaPrime_T1_hex[i]))

                encode[0][9 + i] = self.deltaPrime_T2_hex[i]
                encode[1][9 + i] = hex(ord(self.deltaPrime_T2_hex[i]))

                encode[0][13 + i] = self.delta_T1_hex[i]
                encode[1][13 + i] = hex(ord(self.delta_T1_hex[i]))

                encode[0][17 + i] = self.delta_T2_hex[i]
                encode[1][17 + i] = hex(ord(self.delta_T2_hex[i]))

                encode[0][21 + i] = self.Vb_hex[i]
                encode[1][21 + i] = hex(ord(self.Vb_hex[i]))

                encode[0][25 + i] = self.Tb_hex[i]
                encode[1][25 + i] = hex(ord(self.Tb_hex[i]))

        if self.com == "HCM":                   #PUTS EITHER A '1' OR '0' IN A ONE BYTE SLOT IN THE TABLE
            self.temp = int(                    #(ENABLE OR DISABLE TEMPERATURE COMPENSATION FUNCTION
                input("\nDo you want to enable or disable the temperature correction function? (Type 1 to enable "
                      "or Type 0 to disable)"))
            encode[0][5] = self.temp
            encode[1][5] = hex(ord(str(self.temp)))

        if self.com == "HBV":                          #USER PICKS REFERENCE VOLTAGE AND PUTS EACH HEX CHARACTER IN
            self.Vb = float(input("\n Set a Vb value (V)"))    # ITS CORRESPONDING 4 BYTE SLOT IN THE TABLE
            while self.Vb < 0 or self.Vb > 118.74942:
                self.Vb = float(input("\nInvalid value, input another value"))
            Vb_dec = int(round(self.Vb / (1.812 * 10 ** -3), 0))
            self.Vb_hex = hex(Vb_dec)[2:]
            if len(self.Vb_hex) < 4:
                diff = 4 - len(self.Vb_hex)
                for i in range(diff):
                    self.Vb_hex = '0' + self.Vb_hex
            for i in range(4):
                encode[0][5 + i] = self.Vb_hex[i]
                encode[1][5 + i] = hex(ord(self.Vb_hex[i]))



        print("\nSEND COMMAND")
        print(tabulate(encode, headers=["\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n"]))
        time.sleep(2)

    def decode(self):
        com_char1_asc = hex(ord(self.com[0].lower())) #ASCII CODE FOR THE 3 BYTES OF THE THREE-LETTER COMMAND
        com_char2_asc = hex(ord(self.com[1].lower()))
        com_char3_asc = hex(ord(self.com[2].lower()))

        decode = [
            ['ASCII Code', 'STX', self.com[0].lower(), self.com[1].lower(), self.com[2].lower(), "ETX", "CS", "CS", "CR"],
            ['Size(Byte)', self.STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, self.ETX_asc, "CS", "CS", self.CR_asc]
        ]

        for i in range(self.y):  # APPENDS THE TABLE IN THE MIDDLE CREATING EMPTY BYTES FOR DATA
            decode[0].append("")
            decode[1].append("")
            for n in range(4):
                decode[0][9 - n + i] = decode[0][8 - n + i]
                decode[1][9 - n + i] = decode[1][8 - n + i]
            decode[0][5 + i] = ""
            decode[1][5 + i] = ""

        if self.com in ["HGS", "HGV", "HGC", "HGT"]:  #PUTS EACH HEX CHARACTER IN THE CORRESPONDING 4 BYTE SLOTS IN THE TABLE
            for i in range(4):                          #VARIABLES ARE OUTPUT VOLTAGE, OUTPUT CURRENT, MPPC TEMPERATURE, STATUS
                decode[0][5 + i] = self.data_string_1[i]
                decode[1][5 + i] = hex(ord(self.data_string_1[i]))

        #if self.com in ["HRT", "HPO"]:






        print("\nRESPONSE COMMAND")
        print(tabulate(decode, headers=["\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n"]))
        time.sleep(2)

    def status(self):
        status_dec = int(self.status_hex, 16)
        status_bin = bin(status_dec)[2:]
        print("\n" + status_bin)
        time.sleep(2)

    def voltageOut(self):
        voltage_out_dec = int(self.voltage_out_hex, 16)
        voltage_out = round(voltage_out_dec * 1.812*10**-3, 2)
        print("\nThe Output Voltage is " + str(voltage_out) + "V")
        time.sleep(2)

    def currentOut(self):
        current_out_dec = int(self.current_out_hex, 16)
        current_out = round(current_out_dec * 4.980*10**-3, 2)
        print("\nThe Output Current is " + str(current_out) + "mA")
        time.sleep(2)

    def MPPCOUT(self):
        MPPC_temp_dec = int(self.MPPC_temp_hex, 16)
        MPPC_temp = round((MPPC_temp_dec * 1.907 * 10 ** -5 - 1.035) / (-5.5 * 10 ** -3), 2)
        print("\nThe Output MPPC Temperature is " + str(MPPC_temp) + "°C")
        time.sleep(2)



    def commands(self):
        if self.com == 'HST':
            self.set_values()
            self.x = 24
            self.y = 0
            self.encode()
            self.decode()

        if self.com == 'HRT':
            data = [
                ['Δ\'T1', str(self.deltaPrime_T1) + ' mV/°C^2'], ['Δ\'T2', str(self.deltaPrime_T2) + ' mV/°C^2'],
                ['ΔT1', str(self.delta_T1) + ' mV/°C'], ['ΔT2', str(self.delta_T2) + ' mV/°C'],
                ['Vb', str(self.Vb) + ' V'],
                ['Tb', str(self.Tb) + ' °C']
            ]
            print(tabulate(data, headers=["\nVariable", "\nExisting Value"]))
            time.sleep(2)

        if self.com == 'HPO':
            data = [
                ['Status', "..."], ['Reserve', '...'],
                ['Output Voltage', '...'], ['Output Current', '...'], ['MPPC Temperature', '...']
            ]
            print(tabulate(data, headers=["\nVariable", "\nValue"]))
            time.sleep(2)

        if self.com == 'HGS':
            self.x = 0
            self.y = 4
            self.status_hex = hex(random.randint(int('0', 16), int('FFFF', 16)))[2:].upper()
            if len(self.status_hex) < 4:
                diff = 4 - len(self.status_hex)
                for i in range(diff):
                    self.status_hex = '0' + self.status_hex
            self.data_string_1 = self.status_hex
            self.encode()
            self.decode()
            self.status()


        if self.com == 'HGV':
            self.x = 0
            self.y = 4
            self.voltage_out_hex = hex(random.randint(int('0', 16), int('FFFF', 16)))[2:].upper()
            if len(self.voltage_out_hex) < 4:
                diff = 4 - len(self.voltage_out_hex)
                for i in range(diff):
                    self.voltage_out_hex = '0' + self.voltage_out_hex
            self.data_string_1 = self.voltage_out_hex
            self.encode()
            self.decode()
            self.voltageOut()


        if self.com == 'HGC':
            self.x = 0
            self.y = 4
            self.current_out_hex = hex(random.randint(int('0', 16), int('0400', 16)))[2:].upper()
            if len(self.current_out_hex) < 4:
                diff = 4 - len(self.current_out_hex)
                for i in range(diff):
                    self.current_out_hex = '0' + self.current_out_hex
            self.data_string_1 = self.current_out_hex
            self.encode()
            self.decode()
            self.currentOut()


        if self.com == 'HGT':
            self.x = 0
            self.y = 4
            self.MPPC_temp_hex = hex(random.randint(int('0', 16), int('FFFF', 16)))[2:].upper()
            if len(self.MPPC_temp_hex) < 4:
                diff = 4 - len(self.MPPC_temp_hex)
                for i in range(diff):
                    self.MPPC_temp_hex = '0' + self.MPPC_temp_hex
            self.data_string_1 = self.MPPC_temp_hex
            self.encode()
            self.decode()
            self.MPPCOUT()


        if self.com == 'HOF':
            self.x = 0
            self.y = 0
            self.encode()
            self.decode()

        if self.com == 'HON':
            self.x = 0
            self.y = 0
            self.encode()
            self.decode()

        if self.com == 'HRE':
            self.x = 0
            self.y = 0
            self.encode()
            self.decode()


        if self.com == 'HCM':
            self.x = 1
            self.y = 0
            self.encode()
            self.decode()


        if self.com == "HBV":
            self.x = 4
            self.y = 0
            self.encode()
            self.decode()

    def run(self):
        while 1 > 0:
            self.menu()
            self.commands()


test = serialInterface()

test.run()