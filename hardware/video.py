class Video:

    def video_info(self) -> dict:

        all_vid_data = []

        for vid in self.conn.Win32_VideoController():

            vid_data = {}
            for key in vars(vid)['properties'].keys():
                vid_data[key] = getattr(vid, key)

                if isinstance(vid_data[key], str):
                    vid_data[key] = vid_data[key].strip()

            all_vid_data.append(vid_data)

        return all_vid_data
