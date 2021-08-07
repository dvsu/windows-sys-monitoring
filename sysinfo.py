import wmi
from hardware.disk import Disk
from hardware.memory import Memory
from hardware.motherboard import Motherboard
from hardware.processor import Processor
from hardware.video import Video
from software.operatingsystem import OperatingSystem


class SysInfo(Disk, Memory, Motherboard, OperatingSystem, Processor, Video):

    def __init__(self):
        self.conn = wmi.WMI()

    def all_hardware_info(self):
        return {
            "disk": self.disk_info(),
            "memory": self.memory_info(),
            "motherboard": self.motherboard_info(),
            "processor": self.processor_info(),
            "video": self.video_info()
        }

    def all_software_info(self):
        return {
            "os": self.os_info()
        }

    def all_info(self):
        return {
            "hardware": {
                "disk": self.disk_info(),
                "memory": self.memory_info(),
                "motherboard": self.motherboard_info(),
                "processor": self.processor_info(),
                "video": self.video_info()
            },
            "software": {
                "os": self.os_info()
            }
        }
