import gcodelib
import time

connection = gcodelib.Connection("/dev/ttyUSB0")
connection.console_read()

connection.home()
# time.sleep(5)
# while(True):
connection.magnet_control(True)
connection.send_coords(130,100)
connection.wait_for_movement_start()
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)
connection.send_coords(130,180)
connection.wait_for_movement_start()