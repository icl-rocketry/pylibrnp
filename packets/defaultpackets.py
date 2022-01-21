import struct
import copy
from packets.rnppacket import RnpPacket

class TelemetryPacket(RnpPacket):
	
    struct_str = '<fffffffffffffffffflBffffffffffffHHfflLQhf'
    size = struct.calcsize(struct_str)
    packet_type = 0

    def __init__(self,
                pn: float = 0, pe: float = 0, pd: float = 0,
                vn: float = 0, ve: float = 0, vd: float = 0,
                an: float = 0, ae: float = 0, ad: float = 0,
                roll: float = 0, pitch: float = 0, yaw: float = 0,
                q0: float = 0, q1: float = 0, q2: float = 0, q3:float = 0,
                lat: float = 0, lng: float = 0, alt: int = 0, sat: int = 0,
                ax: float = 0, ay: float = 0, az: float = 0,
                gx: float = 0, gy: float = 0, gz: float = 0,
                mx: float = 0, my: float = 0, mz: float = 0,
                baro_temp: float = 0, baro_press: float = 0,baro_alt: float = 0,
                batt_voltage: int = 0, batt_percent: int = 0,
                launch_lat: float = 0, launch_lng: float = 0, launch_alt: int = 0,
                system_status: int = 0,
                system_time: int = 0,
                rssi: int = 0, snr: float = 0):

        self.pn = pn
        self.pe = pe
        self.pd = pd
        self.vn = vn
        self.ve = ve
        self.vd = vd
        self.an = an
        self.ae = ae
        self.ad = ad
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.q0 = q0
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.lat = lat
        self.lng = lng
        self.alt = alt
        self.sat = sat
        self.ax = ax
        self.ay = ay
        self.az = az
        self.gx = gx
        self.gy = gy
        self.gz = gz
        self.mx = mx
        self.my = my
        self.mz = mz
        self.baro_temp = baro_temp
        self.baro_press = baro_press
        self.baro_alt = baro_alt
        self.batt_voltage = batt_voltage
        self.batt_percent = batt_percent
        self.launch_lat = launch_lat
        self.launch_lng = launch_lng
        self.launch_alt = launch_alt
        self.system_status = system_status
        self.system_time = system_time
        self.rssi = rssi
        self.snr = snr

        
        super().__init__(list(vars(self).keys()),
                         TelemetryPacket.struct_str,
                         TelemetryPacket.size,
                         TelemetryPacket.packet_type)

    def __str__(self):
        header_str = self.header.__str__() + '\ns'
        desc_str = f'TELEMETRY PACKET BODY: Havent done this yet oops\n'
        return header_str

class SimpleCommandPacket(RnpPacket):
    struct_str = '<BI'
    size = struct.calcsize(struct_str)
    packet_type = 0

    def __init__(self, command: int = 0, arg: int = 0):

        self.command = command
        self.arg = arg

        super().__init__(['command','arg'],
                         SimpleCommandPacket.struct_str,
                         SimpleCommandPacket.size,
                         SimpleCommandPacket.packet_type)

    def __str__(self):
        header_str = self.header.__str__() + "\n"
        param_str = f'SIMPLE COMMAND PACKET BODY: \tcommand = {self.command}\n \t\t\targument = {self.arg}\n'
        return header_str + param_str