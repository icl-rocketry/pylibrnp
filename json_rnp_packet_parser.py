import struct
import json


class JsonRnpPacketParser():
    type_format_map = {
        "char":"c",
        "int8_t":"b",
        "uint8_t":"B",
        "bool":"?",
        "int16_t":'h',
        "uint16_t":"H",
        "int":"i",
        "int32_t":"i",
        "uint32_t":"I",
        "int64_t":"q",
        "uint64_t":"Q",
        "float":"f",
        "double":"d"      
    }

    def __init__(self,json_packet_structure):
        if isinstance(json_packet_structure,dict):
            self.packet_structure = json_packet_structure
        else:
            self.packet_structure = json.loads(json_packet_structure)
        self.struct_str = self.__parse_types__()
        self.size = struct.calcsize(self.struct_str)
        self.var_dict = dict.fromkeys(self.packet_structure,0)
       


    def __parse_types__(self):
        try:
            format_character_structure = [JsonRnpPacketParser.type_format_map[key] for key in self.packet_structure.values()]
        except KeyError as e:
            print("Invalid Type Provided!")
            raise e
        return "<" + "".join(format_character_structure) 
        

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


# test = JsonRnpPacketParser(test_json)

# print(test.struct_str)
# print(test.var_dict)