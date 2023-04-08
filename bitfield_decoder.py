
class BitfieldDecoder():
    ''' Class to decode bitfield into consituient flags.
    Expecting a config dict format of the following form 
     {
        [
            {"id":0,"description":"PREFLIGHT"}
        ]
    }

    will return a dict of the following form
    {"flag1":"1/0",
    "flag2":"1/0"}
    '''

    def __init__(self,config):
        self.flagLookup = self.__processConfig__(config)
        self.largestFlagId = max(self.flagLookup.keys())

    def decode(self,bitfield:int):
        binaryString = "{0:b}".format(bitfield)[::-1]#get binary representation and reverse
        #okay but this is kinda cool, only iterates thru stored flags, and only if the flag id is less than the maximum flag id/ the lenght of the binary string
        return {value:(int(binaryString[key]) if key < len(binaryString) else 0) for key,value in self.flagLookup.items()}

    def __processConfig__(self,config):
        ''' 
        Generates a flag lookup dict of the following format -> this is because json doesnt support integers as keys
        {id:"flag_description"} // note id is an integer
        '''
        return {int(flag_config["id"]):flag_config["description"] for flag_config in config}



