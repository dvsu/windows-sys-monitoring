class OperatingSystem:

    def os_info(self) -> dict:

        all_os_data = []

        for os in self.conn.Win32_OperatingSystem():

            os_data = {}
            for key in vars(os)['properties'].keys():
                os_data[key] = getattr(os, key)

                if isinstance(os_data[key], str):
                    os_data[key] = os_data[key].strip()

            all_os_data.append(os_data)

        return all_os_data
