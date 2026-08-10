import serial       
from pylogger.frame_parser import MarkerReader


port = serial.serial_for_url("loop://", timeout=1)




frame = bytes([0xAA, 0x55, 0x04, 0x2A, 0x00, 0x0F, 0xFF])
port.write(frame)

received = port.read(len(frame))
print(" ".join(f"[{b:02X}]" for b in received))