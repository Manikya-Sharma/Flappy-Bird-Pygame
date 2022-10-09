class Defaults:
    defaults = \
        {
            "SCREEN_WIDTH": 600,
            "SCREEN_HEIGHT": 600
        }


class Settings:
    @staticmethod
    def get_settings():
        with open('settings.csv', 'r') as f:
            data = f.read()
            dic = Settings.get_data_dic(data)
        return dic

    @staticmethod
    def make_default_settings():
        Settings.make_data_dic(Defaults.defaults)

    @staticmethod
    def get_data_dic(data):
        dic = {}
        rows = data.split(',')
        for element in rows:
            try:
                key, value = element.split(":")
            except ValueError as e:
                if e== "not enough values to unpack (expected 2, got 1)":
                    continue # Due to EOF
            dic[key] = value
        return dic

    @staticmethod
    def make_data_dic(dic):
        string = ''
        for key, value in dic.items():
            string += (str(key).strip() + ":" + str(value).strip() + ",")

        with open('settings.csv', 'w') as f:
            f.write(string)