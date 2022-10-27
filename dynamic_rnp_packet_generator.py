# from pylibrnp.utils.json_rnp_packet_parser import JsonRnpPacketParser
from rnppacket import RnpPacket
from json_rnp_packet_parser import JsonRnpPacketParser

class DynamicRnpPacketGenerator():
    def __init__(self,classname,json_packet_structure): 
        self.classname = classname
        self.parsed_json_packet = JsonRnpPacketParser(json_packet_structure)
        self.new_class = self.__generate__()


    def __generate__(self):
        def packet_init(this):

            for elem in self.parsed_json_packet.var_dict.keys():
                setattr(this,elem,0)

            RnpPacket.__init__(this,
                              list(self.parsed_json_packet.var_dict.keys()),
                              self.parsed_json_packet.struct_str,
                              self.parsed_json_packet.size,
                              0)

        new_type = type(self.classname,(RnpPacket,),{'__init__':packet_init})
        return new_type

    def getClass(self):
        return self.new_class

    
# test_json = {
#         "pn": "float",
#         "pe": "float",
#         "pd": "float",
#         "vn": "float",
#         "ve": "float",
#         "vd": "float",
#         "an": "float",
#         "ae": "float",
#         "ad": "float",
#         "roll": "float",
#         "pitch": "float",
#         "yaw": "float",
#         "q0": "float",
#         "q1": "float",
#         "q2": "float",
#         "q3": "float",
#         "lat": "float",
#         "lng": "float",
#         "alt": "int",
#         "sat": "uint8_t",
#         "ax": "float",
#         "ay": "float",
#         "az": "float",
#         "h_ax": "float",
#         "h_ay": "float",
#         "h_az": "float",
#         "gx": "float",
#         "gy": "float",
#         "gz": "float",
#         "mx": "float",
#         "my": "float",
#         "mz": "float",
#         "baro_temp": "float",
#         "baro_press": "float",
#         "baro_alt": "float",
#         "batt_voltage": "uint16_t",
#         "batt_percent": "uint16_t",
#         "launch_lat": "float",
#         "launch_lng": "float",
#         "launch_alt": "int",
#         "system_status": "uint32_t",
#         "system_time": "uint64_t",
#         "rssi": "int16_t",
#         "snr": "float"
#     }



            

# test = DynamicRnpPacketGenerator('test_class',test_json)
# test_class = test.new_class()
# print(vars(test_class))
# print(test_class.serialize())



