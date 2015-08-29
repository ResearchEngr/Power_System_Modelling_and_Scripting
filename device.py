import system

class device:
    
    self.n = 0
    self.gcall = []
    self.gycall = []
    self.fcall = []
    self.fxcall =[]
    
    def __init__(self, device_list):
        
        self.devices = device_list
        
    def setup(self):
        
        self.n = 0
        for item in self.devices:
            if system.__dict__[item].n:
                self.n += 1
                self.devices.append(item)
                properties = system.__dict__[item].properties
                for key in properties.keys():
                    self.__dict__[key].append(properties[key])
                    
        string = '"""\n'
        for gcall, device in zip(self.gcall, self.devices):
            if gcall:string += 'system.' + device + '.gcall(system.DAE)\n'
        string += '\n'
        for gycall, device in zip(self.gycall, self.devices):
            if gycall: string += 'system.' + device + '.gycall(system.DAE)\n'
        string += '\n'
        for fcall, device in zip(self.fcall, self.devices):
            if fcall: string += 'system.' + device + '.fcall(system.DAE)\n'
        string += '\n'
        for fxcall, device in zip(self.fxcall, self.devices):
            if fxcall: string += 'system.' + device + '.fxcall(system.DAE)\n'
        string += '\n'
        self.call_int = compile(eval(string), '', 'exec')
        