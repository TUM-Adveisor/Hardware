import gcodelib
import time

connection = gcodelib.Connection("COM4")
connection.console_read()

connection.home()
# time.sleep(5)
# while(True):   
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
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)
connection.send_coords(0,180)
connection.wait_for_movement_start()
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)
connection.send_coords(0,100)
connection.wait_for_movement_start()
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)
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
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)


# time.sleep(1)

# connection.send_coords(15,0)
# connection.wait_for_movement_start()
# print("header started")
# while (connection._status != "Idle"):
#     connection.print_coords()
#     time.sleep(1/10)
    # print("header stopped")

# time.sleep(1)

###################
# connection.send_coords(15,0)
# connection.home()
# connection.wait_for_movement_stop()
# magnes.wlacz()
# connection.send_coords(0,0)
# connection.wait_for_movement_stop()
# magnes.wylacz()




    ##################