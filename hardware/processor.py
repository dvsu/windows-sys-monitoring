class Processor:

    def processor_info(self) -> dict:

        all_cpu_data = []

        for cpu in self.conn.Win32_Processor():

            cpu_data = {}
            for key in vars(cpu)['properties'].keys():
                cpu_data[key] = getattr(cpu, key)

                if isinstance(cpu_data[key], str):
                    cpu_data[key] = cpu_data[key].strip()

            all_cpu_data.append(cpu_data)

        return all_cpu_data
