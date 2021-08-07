memory_type = {
    0: "Unknown",
    1: "Other",
    2: "DRAM",
    3: "Synchronous DRAM",
    4: "Cache DRAM",
    5: "EDO",
    6: "EDRAM",
    7: "VRAM",
    8: "SRAM",
    9: "RAM",
    10: "ROM",
    11: "Flash",
    12: "EEPROM",
    13: "FEPROM",
    14: "EPROM",
    15: "CDRAM",
    16: "3DRAM",
    17: "SDRAM",
    18: "SGRAM",
    19: "RDRAM",
    20: "DDR",
    21: "DDR2",
    22: "DDR2 FB-DIMM",
    23: "DDR2—FB",
    24: "DDR3",
    25: "FBD2",
    26: "DDR4"
}

form_factor = {
    0: "Unknown",
    1: "Other",
    2: "SIP",
    3: "DIP",
    4: "ZIP",
    5: "SOJ",
    6: "Proprietary",
    7: "SIMM",
    8: "DIMM",
    9: "TSOP",
    10: "PGA",
    11: "RIMM",
    12: "SODIMM",
    13: "SRIMM",
    14: "SMD",
    15: "SSMP",
    16: "QFP",
    17: "TQFP",
    18: "SOIC",
    19: "LCC",
    20: "PLCC",
    21: "BGA",
    22: "FPBGA",
    23: "LGA",
    24: "FB-DIMM"
}


class Memory:

    def memory_info(self) -> dict:

        all_mem_data = []

        for mem in self.conn.Win32_PhysicalMemory():

            mem_data = {}
            for key in vars(mem)['properties'].keys():
                mem_data[key] = getattr(mem, key)

                if key == 'MemoryType' or key == 'SMBIOSMemoryType':
                    mem_data[key] = memory_type[mem_data[key]]

                elif key == 'FormFactor':
                    mem_data[key] = form_factor[mem_data[key]]

                if isinstance(mem_data[key], str):
                    mem_data[key] = mem_data[key].strip()

            all_mem_data.append(mem_data)

        return all_mem_data
