# disk_type = {
#     0: "Unknown",
#     1: "No Root Directory",
#     2: "Removable Disk",
#     3: "Local Disk",
#     4: "Network Drive",
#     5: "Compact Disc",
#     6: "RAM Disk"
# }


class Disk:

    def disk_info(self) -> dict:

        all_disk_data = []

        for disk in self.conn.Win32_LogicalDisk():

            disk_data = {}
            for key in vars(disk)['properties'].keys():
                disk_data[key] = getattr(disk, key)

                if isinstance(disk_data[key], str):
                    disk_data[key] = disk_data[key].strip()

            all_disk_data.append(disk_data)

        return all_disk_data
