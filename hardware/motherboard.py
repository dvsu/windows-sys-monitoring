class Motherboard:

    def motherboard_info(self) -> dict:

        all_mobo_data = []

        for mobo in self.conn.Win32_BaseBoard():

            mobo_data = {}
            for key in vars(mobo)['properties'].keys():
                mobo_data[key] = getattr(mobo, key)

                if isinstance(mobo_data[key], str):
                    mobo_data[key] = mobo_data[key].strip()

            all_mobo_data.append(mobo_data)

        return all_mobo_data
