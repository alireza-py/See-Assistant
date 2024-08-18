from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume 
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

class speakers:
    def __init__(self) -> None: 
        pass
    
    def devices(self, any: float):
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            currentVolumeDb = volume.GetMasterVolumeLevel()
            volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0] / any, None)

            return 'I do it'
        except:
            return 'speakers have a problem'

    def range_sunde(self):
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            return volume.GetVolumeRange()
        except:
            return 'speakers have a problem'
