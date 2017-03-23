import smbus
import time
from bottle import route, run, template


bus = smbus.SMBus(1) # Rev 2 Pi uses 1

DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
OLATA  = 0x14 # Register for outputs
GPIOA  = 0x12 # Register for inputs


a0=1
a1=1
a2=1
a3=1
a4=1
a5=1
a6=1
a7=1

@route('/maly/<val>')
def maly(val):
    global a0
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    if (val == 'on'):
        a1=0
    if (val == 'off'):
        a1=1
    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a) 

    return template('<b>Swiatlo maly:  {{val}}</b>!', val=val)

@route('/duzy3/<val>')
def duzy3(val):
    global a0
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    if (val == 'on'):
        a2=0
    if (val == 'off'):
        a2=1
    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a)

    return template('<b>Swiatlo duzy3:  {{val}}</b>!', val=val)

@route('/duzy2/<val>')
def duzy2(val):
    global a0
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    if (val == 'on'):
        a3=0
    if (val == 'off'):
        a3=1
    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a)

    return template('<b>Swiatlo duzy2:  {{val}}</b>!', val=val)


@route('/hol2/<val>')
def hol2(val):
    global a0
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    if (val == 'on'):
        a4=0
    if (val == 'off'):
        a4=1
    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a)

    return template('<b>Swiatlo hol2:  {{val}}</b>!', val=val)


@route('/hol1/<val>')
def hol1(val):
    global a0
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    if (val == 'on'):
        a5=0
    if (val == 'off'):
        a5=1
    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a)

    return template('<b>Swiatlo hol1:  {{val}}</b>!', val=val)




# Set all GPA pins as outputs by setting
# all bits of IODIRA register to 0
bus.write_byte_data(DEVICE,IODIRA,0x00)

# Set output all 7 output bits to 1
bus.write_byte_data(DEVICE,OLATA,255) 


run(host='0.0.0.0', port=8080)

