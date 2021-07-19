import serial
import time

ser = serial.Serial('COM4', baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN,
                    stopbits=serial.STOPBITS_ONE, timeout=3)  # open serial port

if ser.is_open == True:    # make sure port is open
    print("Port is open")

while True:
    request_com = input("\nType a command")

    if request_com == 'HST': #h02 h48 h53 h54 h30 h30 h30 h30 h30 h30 h30 h30 h30 h34 h33 h30 h30 h34 h33 h30 h38 h31 h35 h39 h42 h37 h44 h37 h03 h43 h44 h0D
        request_hexstring = b'\x02\x48\x53\x54\x30\x30\x30\x30\x30\x30\x30\x30\x30\x34\x33\x30\x30\x34\x33\x30\x38\x31\x35\x39\x42\x37\x44\x37\x03\x43\x44\x0D'
        ser.write(request_hexstring)
        response_ascii_string = ser.read(8)
        print(response_ascii_string)




    if request_com == 'HRT':
        request_hexstring = b'\x02\x48\x52\x54\x03\x46\x33\x0D' #h02 h48 h52 h54 h03 h46 h33 h0D
        ser.write(request_hexstring)
        response_ascii_string = ser.read(32)
        print(response_ascii_string)

    if request_com == 'HPO':
        request_hexstring = '\x02\x48\x50\x4F\x03\x45\x43\x0D' #h02 h48 h52 h54 h03 h46 h33 h0D
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(32)
        print(response_ascii_string)



    if request_com == 'HGS':
        request_hexstring = b'\x02\x48\x47\x53\x03\x45\x37\x0D' #h02 h48 h47 h53 h03 h45 h37 h0D
        ser.write(request_hexstring)
        response_ascii_string = ser.read(12)
        output_status_hex = str(response_ascii_string)[9:13]
        output_status = bin(int(output_status_hex, 16))[2:]
        print(response_ascii_string)
        print(str(output_status))
        time.sleep(1)

    if request_com == 'HGV':
        request_hexstring = b'\x02\x48\x47\x56\x03\x45\x41\x0D' #h02 h48 h47 h56 h03 h45 h41 h0DHR
        ser.write(request_hexstring)
        response_ascii_string = ser.read(12)
        output_voltage_hex = str(response_ascii_string)[9:13]
        output_voltage = round(int(output_voltage_hex, 16) * 1.812*10**-3, 2)
        print(response_ascii_string)
        print(str(output_voltage) + "V")
        time.sleep(1)

    if request_com == 'HGC':
        request_hexstring = b'\x02\x48\x47\x43\x03\x44\x37\x0D' #h02 h48 h47 h43 h03 h44 h37 h0D
        ser.write(request_hexstring)
        response_ascii_string = ser.read(12)
        output_current_hex = str(response_ascii_string)[9:13]
        output_current = round(int(output_current_hex, 16) * 4.980 * 10 ** -3, 2)
        print(response_ascii_string)
        print(str(output_current) + "mA")
        time.sleep(1)

    if request_com == 'HGT':
        request_hexstring = b'\x02\x48\x47\x54\x03\x45\x38\x0D' #h02 h48 h47 h54 h03 h45 h38 h0D
        ser.write(request_hexstring)
        response_ascii_string = ser.read(12)
        output_MPPCtemp_hex = str(response_ascii_string)[9:13]
        output_MPPCtemp = round((int(output_MPPCtemp_hex, 16) * 1.907 * 10 ** -5 - 1.035) / (-5.5 * 10 ** -3), 2)
        print(response_ascii_string)
        print(str(output_MPPCtemp) + "°C")
        time.sleep(1)

    if request_com == 'HOF':
        request_hexstring = b'\x02\x48\x4F\x46\x03\x45\x32\x0D'  #h02 h48 h4F h46 h03 h45 h32 h0D
        ser.write(request_hexstring)
        response_ascii_string = ser.read(12)
        print(response_ascii_string)
        print("High Voltage Output is OFF")

    if request_com == 'HON':
        request_hexstring = b'\x02\x48\x4F\x4E\x03\x45\x41\x0D'  #h02 h48 h4F h4E h03 h45 h41 h0D
        ser.write(request_hexstring)
        response_ascii_string = ser.read(12)
        print(response_ascii_string)
        print("High Voltage Output is ON")

    if request_com == 'HRE':
        request_hexstring = b'\x02\x48\x52\x45\x03\x45\x34\x0D'  #h02 h48 h52 h45 h03 h45 h34 h0D
        ser.write(request_hexstring)
        response_ascii_string = ser.read(12)
        print(response_ascii_string)
        print("The Power Will Reset")

    if request_com == 'HHH':
        a = '\x02\x48'
        request_hexstring = a + '\x47\x54\x03\x45\x38\x0D'
        ser.write(request_hexstring.encode('utf-8'))
        response_ascii_string = ser.read(12)
        print(response_ascii_string)



