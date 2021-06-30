from tabulate import tabulate
import time
import random


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

        T_dec = random.randint(0, 65535)
        T_hex = hex(T_dec)
        self.T = (T_dec * 1.907 * 10 - 5 - 1.035) / (-5.5 * 10 - 3)

        self.deltaPrime_T1 = float(input("\n Set a Δ\'T1 value (mV/°C^2)"))
        while abs(self.deltaPrime_T1) > 1.507:
            self.deltaPrime_T1 = float(input("\nInvalid value, input another value"))
        deltaPrime_T1_dec = int(round(self.deltaPrime_T1 / (1.507 * 10 ** -3), 0))
        deltaPrime_T1_hex = hex(deltaPrime_T1_dec)

        self.deltaPrime_T2 = float(input("\n Set a Δ\'T2 value (mV/°C^2)"))
        while abs(self.deltaPrime_T2) > 1.507:
            self.deltaPrime_T2 = float(input("\nInvalid value, input another value"))
        deltaPrime_T2_dec = int(round(self.deltaPrime_T2 / (1.507 * 10 ** -3), 0))
        deltaPrime_T2_hex = hex(deltaPrime_T2_dec)

        self.delta_T1 = float(input("\n Set a ΔT1 value (mV/°C)"))
        while self.delta_T1 < 0 or self.delta_T1 > 3424.20375:
            self.delta_T1 = float(input("\nInvalid value, input another value"))
        delta_T1_dec = int(round(self.delta_T1 / (5.225 * 10 ** -2), 0))
        delta_T1_hex = hex(delta_T1_dec)

        self.delta_T2 = float(input("\n Set a ΔT2 value (mV/°C)"))
        while self.delta_T2 < 0 or self.delta_T2 > 3424.20375:
            self.delta_T2 = float(input("\nInvalid value, input another value"))
        delta_T2_dec = int(round(self.delta_T2 / (5.225 * 10 ** -2), 0))
        delta_T2_hex = hex(delta_T2_dec)

        self.Vb = float(input("\n Set a Vb value (V)"))
        while self.Vb < 0 or self.Vb > 118.74942:
            self.Vb = float(input("\nInvalid value, input another value"))
        Vb_dec = int(round(self.Vb / (1.812 * 10 ** -3), 0))
        Vb_hex = hex(Vb_dec)

        self.Tb = float(input("\n Set a Tb value (°C)"))
        while self.Tb < -39.0459 or self.Tb > 188.1818:
            self.Tb = float(input("\nInvalid value, input another value"))
        Tb_dec = int(round((1.035 + (self.Tb * -5.5 * 10 ** -3)) / 1.907 * 10 ** -5, 0))
        Tb_hex = hex(Tb_dec)

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
            print("\nCool!")
        elif answer == "no":
            self.set_values()
        else:
            print("\nInvalid Response")

    def loop_10(self):
        answer = input("Are you sure you want to reset the power?")

        if answer == "yes":
            print("The power will reset shortly")
        elif answer == "no":
            print("Going back to the menu...")
        else:
            print("Invalid answer")
            self.loop_10()

    def output_0_1(self):
        # Send Command
        STX_asc = hex(2)
        com_char1_asc = hex(ord(self.com[0]))
        com_char2_asc = hex(ord(self.com[1]))
        com_char3_asc = hex(ord(self.com[2]))
        ETX_asc = hex(3)
        check_sum = hex(
            int(STX_asc, 16) + int(com_char1_asc, 16) + int(com_char2_asc, 16) + int(com_char3_asc, 16) + int(ETX_asc,
                                                                                                              16))
        CR_asc = hex(13)[0] + hex(13)[1] + hex(13)[2].upper()

        last_two = str(hex(int(check_sum, 16) % int('1000', 16))[2:]).upper()
        second_to_last = last_two[len(last_two) - 2]
        last = last_two[len(last_two) - 1]
        second_to_last_asc = hex(ord(second_to_last))
        last_asc = hex(ord(last))

        menu = [
            ['ASCII Code', 'STX', self.com[0], self.com[1], self.com[2], "ETX", second_to_last, last, "CR"],
            ['Size(Byte)', STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, ETX_asc, second_to_last_asc, last_asc,
             CR_asc]
        ]

        print(tabulate(menu, headers=["\nSEND COMMAND", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n"]))
        time.sleep(2)

        # -----------------------------------------------

        # Response Command
        data_string = hex(random.randint(int('0', 16), int('FFFF', 16)))[2:].upper()  # RETRIEVE THIS NUMBER FROM DEVICE
        data_string_first = data_string[0]
        data_string_second = data_string[1]
        data_string_third = data_string[2]
        com_char1_asc = hex(ord(self.com[0].lower()))
        com_char2_asc = hex(ord(self.com[1].lower()))
        com_char3_asc = hex(ord(self.com[2].lower()))
        data_string_first_asc = hex(ord(data_string_first))
        data_string_second_asc = hex(ord(data_string_second))
        data_string_third_asc = hex(ord(data_string_third))
        if len(data_string) == 4:
            data_string_fourth = data_string[3]
            data_string_fourth_asc = hex(ord(data_string_fourth))
            check_sum = hex(
                int(STX_asc, 16) + int(com_char1_asc, 16) + int(com_char2_asc, 16) + int(com_char3_asc, 16) + int(
                    data_string_first_asc, 16)
                + int(data_string_second_asc, 16) + int(data_string_third_asc, 16) + int(data_string_fourth_asc, 16)
                + int(ETX_asc, 16))
        else:
            check_sum = hex(
                int(STX_asc, 16) + int(com_char1_asc, 16) + int(com_char2_asc, 16) + int(com_char3_asc, 16) + int(
                    data_string_first_asc, 16)
                + int(data_string_second_asc, 16) + int(data_string_third_asc, 16) + int(ETX_asc, 16))

        last_two = str(hex(int(check_sum, 16) % int('1000', 16))[2:]).upper()
        second_to_last = last_two[len(last_two) - 2]
        last = last_two[len(last_two) - 1]
        second_to_last_asc = hex(ord(second_to_last))
        last_asc = hex(ord(last))

        if len(data_string) == 4:
            menu = [
                ['ASCII Code', 'STX', self.com[0].lower(), self.com[1].lower(), self.com[2].lower(), data_string_first,
                 data_string_second, data_string_third,
                 data_string_fourth, "ETX", second_to_last, last, "CR"],
                ['Size(Byte)', STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, data_string_first_asc,
                 data_string_second_asc,
                 data_string_third_asc, data_string_fourth_asc, ETX_asc, second_to_last_asc, last_asc, CR_asc]
            ]

            print(
                tabulate(menu,
                         headers=["\nRESPONSE COMMAND", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n",
                                  "\n",
                                  "\n"]))
        else:
            menu = [
                ['ASCII Code', 'STX', self.com[0].lower(), self.com[1].lower(), self.com[2].lower(), data_string_first,
                 data_string_second, data_string_third
                    , "ETX", second_to_last, last, "CR"],
                ['Size(Byte)', STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, data_string_first_asc,
                 data_string_second_asc,
                 data_string_third_asc, ETX_asc, second_to_last_asc, last_asc, CR_asc]
            ]

            print(tabulate(menu,
                           headers=["\nRESPONSE COMMAND", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n",
                                    "\n"]))
        time.sleep(2)

        # Translate Data
        data_hex = data_string
        data_dec = int(data_hex, 16)
        if self.com == "HGS":  # OUTPUT STATUS
            data = bin(data_dec)[2:]
            if len(data) < 16:
                diff = 16 - len(data)
                for i in range(diff):
                    data = '0' + data
            print("\nThe binary value is " + data)
            time.sleep(2)

            if data[15] == '1':
                data_val_15 = 1
                data_des_15 = 'ON'
            else:
                data_val_15 = 0
                data_des_15 = 'OFF'

            if data[14] == '1':
                data_val_14 = 1
                data_des_14 = 'Working Protection'
            else:
                data_val_14 = 0
                data_des_14 = 'Not Working'

            if data[13] == '1':
                data_val_13 = 1
                data_des_13 = 'Outside Specification'
            else:
                data_val_13 = 0
                data_des_13 = 'Within Specification'

            if data[12] == '1':
                data_val_12 = 1
                data_des_12 = 'Connect'
            else:
                data_val_12 = 0
                data_des_12 = 'Disconnect'

            if data[11] == '1':
                data_val_11 = 1
                data_des_11 = 'Outside Specification'
            else:
                data_val_11 = 0
                data_des_11 = 'Within Specification'

            if data[9] == '1':
                data_val_9 = 1
                data_des_9 = 'Effectiveness'
            else:
                data_val_9 = 0
                data_des_9 = 'Invalid'

            status_table = [
                [0, 'High Voltage Output', data_val_15, data_des_15],
                [1, 'Overcurrent Protection', data_val_14, data_des_14],
                [2, 'Output Current Value', data_val_13, data_des_13],
                [3, 'Temperature Sensor Connect', data_val_12, data_des_12],
                [4, 'Operation Temperature Limit', data_val_11, data_des_11],
                [5, 'Reserve 5', "_______", "_____________________"],
                [6, 'Temperature Correction', data_val_9, data_des_9],
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


        if self.com == "HGV":  # OUTPUT VOLTAGE
            data = round(data_dec * 1.812 * 10 ** -3, 2)
            print("\nThe Output Voltage is " + str(data) + "V")

        if self.com == "HGC":  # OUTPUT CURRENT
            data = round(data_dec * 4.980 * 10 ** -3, 2)
            print("\nThe Output Current is " + str(data) + "mA")

        if self.com == "HGT":  # OUTPUT MPPC TEMPERATURE:
            data = round((data_dec * 1.907 * 10 ** -5 - 1.035) / (-5.5 * 10 ** -3), 2)
            print("\nThe Output MPPC Temperature is " + str(data) + "°C")

        time.sleep(2)

    def output_0_0(self):
        # Send Command

        STX_asc = hex(2)
        com_char1_asc = hex(ord(self.com[0]))
        com_char2_asc = hex(ord(self.com[1]))
        com_char2_asc = com_char2_asc[0:3] + com_char2_asc[3].upper()
        com_char3_asc = hex(ord(self.com[2]))
        com_char3_asc = com_char3_asc[0:3] + com_char3_asc[3].upper()
        ETX_asc = hex(3)
        check_sum = hex(
            int(STX_asc, 16) + int(com_char1_asc, 16) + int(com_char2_asc, 16) + int(com_char3_asc, 16) + int(ETX_asc,
                                                                                                              16))
        CR_asc = hex(13)[0] + hex(13)[1] + hex(13)[2].upper()

        last_two = str(hex(int(check_sum, 16) % int('1000', 16))[2:]).upper()
        second_to_last = last_two[len(last_two) - 2]
        last = last_two[len(last_two) - 1]
        second_to_last_asc = hex(ord(second_to_last))
        last_asc = hex(ord(last))

        menu = [
            ['ASCII Code', 'STX', self.com[0], self.com[1], self.com[2], "ETX", second_to_last, last, "CR"],
            ['Size(Byte)', STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, ETX_asc, second_to_last_asc, last_asc,
             CR_asc]
        ]

        print(tabulate(menu, headers=["\nSEND COMMAND", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n"]))
        time.sleep(2)

        # -----------------------------------------------

        # Response Command
        com_char1_asc = hex(ord(self.com[0].lower()))
        com_char2_asc = hex(ord(self.com[1].lower()))
        com_char2_asc = com_char2_asc[0:3] + com_char2_asc[3].upper()
        com_char3_asc = hex(ord(self.com[2].lower()))
        com_char3_asc = com_char3_asc[0:3] + com_char3_asc[3].upper()


        check_sum = hex(
            int(STX_asc, 16) + int(com_char1_asc, 16) + int(com_char2_asc, 16) + int(com_char3_asc, 16) + int(ETX_asc,
                                                                                                              16))
        last_two = str(hex(int(check_sum, 16) % int('1000', 16))[2:]).upper()
        second_to_last = last_two[len(last_two) - 2]
        last = last_two[len(last_two) - 1]
        second_to_last_asc = hex(ord(second_to_last))
        last_asc = hex(ord(last))

        menu = [
            ['ASCII Code', 'STX', self.com[0].lower(), self.com[1].lower(), self.com[2].lower(), "ETX", second_to_last,
             last, "CR"],
            ['Size(Byte)', STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, ETX_asc, second_to_last_asc, last_asc,
             CR_asc]
        ]

        print(tabulate(menu, headers=["\nRESPONSE COMMAND", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n"]))
        time.sleep(2)

        if self.com == "HOF":
            print("\nThe High Voltage Output is OFF")
        if self.com == "HON":
            print("\nThe High Voltage Output is ON")
        if self.com == "HRE":
            print("\nThe Power Will Reset Shortly...")
        time.sleep(2)

    def output_1_0(self):
        STX_asc = hex(2)
        ETX_asc = hex(3)
        CR_asc = hex(13)[0] + hex(13)[1] + hex(13)[2].upper()
        if self.com == "HCM":
            data = int(input("\nDo you want to enable or disable the temperature correction function? (Type 1 to enable "
                             "or Type 0 to disable)"))

            com_char1_asc = hex(ord(self.com[0]))
            com_char2_asc = hex(ord(self.com[1]))
            com_char3_asc = hex(ord(self.com[2]))
            com_char3_asc = com_char3_asc[0:3] + com_char3_asc[3].upper()
            data_asc = hex(ord(str(data)))
            check_sum = hex(
                int(STX_asc, 16) + int(com_char1_asc, 16) + int(com_char2_asc, 16) + int(com_char3_asc, 16) +
                int(data_asc, 16) + int(ETX_asc, 16))


            last_two = str(hex(int(check_sum, 16) % int('1000', 16))[2:]).upper()
            second_to_last = last_two[len(last_two) - 2]
            last = last_two[len(last_two) - 1]
            second_to_last_asc = hex(ord(second_to_last))
            last_asc = hex(ord(last))

            menu = [
                      ['ASCII Code', 'STX', self.com[0], self.com[1], self.com[2], data, "ETX", second_to_last, last, "CR"],
                      ['Size(Byte)', STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, data_asc, ETX_asc,
                        second_to_last_asc, last_asc, CR_asc]
                   ]

            print(tabulate(menu,
                           headers=["\nSEND COMMAND", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n",
                                    "\n"]))
            time.sleep(2)


        if self.com == "HBV":
            self.Vb = float(input("\n Set a Reference Voltage value (V)"))
            while self.Vb < 0 or self.Vb > 118.74942:
                self.Vb = float(input("\nInvalid value, input another value"))
            Vb_dec = int(round(self.Vb / (1.812 * 10 ** -3), 0))
            Vb_hex = hex(Vb_dec).upper()

            data_string = str(Vb_hex[2:])
            data_string_first = data_string[0]
            data_string_second = data_string[1]
            data_string_third = data_string[2]
            data_string_fourth = data_string[3]
            data_string_first_asc = hex(ord(data_string_first))
            data_string_second_asc = hex(ord(data_string_second))
            data_string_third_asc = hex(ord(data_string_third))
            data_string_fourth_asc = hex(ord(data_string_fourth))
            com_char1_asc = hex(ord(self.com[0]))
            com_char2_asc = hex(ord(self.com[1]))
            com_char3_asc = hex(ord(self.com[2]))
            check_sum = hex(
                int(STX_asc, 16) + int(com_char1_asc, 16) + int(com_char2_asc, 16) + int(com_char3_asc, 16) +
                int(data_string_first_asc, 16) + int(data_string_second_asc, 16) + int(data_string_third_asc, 16) +
                int(data_string_fourth_asc, 16) + int(ETX_asc, 16))

            last_two = str(hex(int(check_sum, 16) % int('1000', 16))[2:]).upper()
            second_to_last = last_two[len(last_two) - 2]
            last = last_two[len(last_two) - 1]
            second_to_last_asc = hex(ord(second_to_last))
            last_asc = hex(ord(last))

            menu = [
                ['ASCII Code', 'STX', self.com[0], self.com[1], self.com[2], data_string_first, data_string_second,
                 data_string_third, data_string_fourth, "ETX", second_to_last, last, "CR"],
                ['Size(Byte)', STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, data_string_first_asc,
                 data_string_second_asc, data_string_third_asc, data_string_fourth_asc, ETX_asc, second_to_last_asc,
                 last_asc, CR_asc]
                   ]

            print(tabulate(menu,
                           headers=["\nSEND COMMAND", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n",
                                    "\n", "\n"]))
            time.sleep(2)

        # --------------------------------------------------------
        # RESPONSE

        com_char1_asc = hex(ord(self.com[0].lower()))
        com_char2_asc = hex(ord(self.com[1].lower()))
        com_char3_asc = hex(ord(self.com[2].lower()))
        com_char3_asc = com_char3_asc[0:3] + com_char3_asc[3].upper()

        check_sum = hex(int(STX_asc, 16) + int(com_char1_asc, 16) + int(com_char2_asc, 16) + int(com_char3_asc, 16)
                            + int(ETX_asc, 16))

        last_two = str(hex(int(check_sum, 16) % int('1000', 16))[2:]).upper()
        second_to_last = last_two[len(last_two) - 2]
        last = last_two[len(last_two) - 1]
        second_to_last_asc = hex(ord(second_to_last))
        last_asc = hex(ord(last))

        menu = [
            ['ASCII Code', 'STX', self.com[0].lower(), self.com[1].lower(), self.com[2].lower(), "ETX",
             second_to_last, last, "CR"],
            ['Size(Byte)', STX_asc, com_char1_asc, com_char2_asc, com_char3_asc, ETX_asc, second_to_last_asc,
            last_asc, CR_asc]
               ]

        print(tabulate(menu,headers=["\nRESPONSE COMMAND", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n",
                "\n", "\n"]))
        time.sleep(2)

    def commands(self):
        if self.com == 'HST':
            self.set_values()
            time.sleep(2)

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
            self.output_0_1()

        if self.com == 'HGV':
            self.output_0_1()

        if self.com == 'HGC':
            self.output_0_1()

        if self.com == 'HGT':
            self.output_0_1()

        if self.com == 'HOF':
            self.output_0_0()

        if self.com == 'HON':
            self.output_0_0()

        if self.com == 'HRE':
            self.output_0_0()

        if self.com == 'HCM':
            self.output_1_0()

        if self.com == "HBV":
            self.output_1_0()

    def run(self):
        while 1 > 0:
            self.menu()
            self.commands()


test = serialInterface()

test.run()


