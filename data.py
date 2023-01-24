import re


class DataProcessing:
    """This class processes a data file"""

    data_sheet = list()

    def __init__(self):
        with open('datasheet.txt', 'r') as file:
            for text in file:
                self.data_sheet.append(text)

    def __delete_pc__(self, count):
        del self.data_sheet[count]
        file = open('datasheet.txt', 'w')
        file.writelines(self.data_sheet)
        file.close()

    @staticmethod
    def __add_pc__(user_name, password, ip, mac, port):
        # Validation for entered mac and ip addresses
        ip_valid = bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', ip))
        mac_valid = bool(re.match('^' + '[\:\-]'.join(['([0-9a-f]{2})'] * 6) + '$', mac.lower()))

        if ip_valid and mac_valid:
            data_pc = [user_name, ',', password, ',', ip, ',', mac, ',', port, '\n']
            file = open('datasheet.txt', 'a')
            file.writelines(data_pc)
            file.close()

            return True
        else:
            return False
