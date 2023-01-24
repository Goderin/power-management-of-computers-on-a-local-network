import paramiko
import socket
import struct
from pythonping import ping


class PcControl:
    data_sheet = list()

    def __init__(self):
        """Adding data from a file to a sheet"""

        with open('datasheet.txt', 'r') as file:
            for text in file:
                self.data_sheet.append(text)

    def off_pc(self, count_id):
        """Turning off the PC using the ssh network protocol"""

        host = self.data_sheet[count_id].split(',')

        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            client.connect(host[2], int(host[4]), username=host[0], password=host[1])
            client.exec_command("shutdown /s /f /t 0")
            return True

        except Exception:
            return False

    def on_pc(self, count_id):
        """Waking up the computer using Wake On Lan"""

        host = self.data_sheet[count_id].split(',')
        mac_addr = host[3].split("-")
        hw_addr = struct.pack("BBBBBB", int(mac_addr[0], 16), int(mac_addr[1], 16),
                              int(mac_addr[2], 16), int(mac_addr[3], 16), int(mac_addr[4], 16),
                              int(mac_addr[5], 16))

        magic = b"\xFF" * 6 + hw_addr * 16

        user_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        user_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        user_socket.sendto(magic, (host[2], 9))
        user_socket.close()

    def status_pc(self, count_id):
        """Getting a response from the computer"""

        host = self.data_sheet[count_id].split(',')
        response_list = ping(host[2], size=1, count=1)
        if response_list.rtt_avg_ms != 2000:
            return True
        else:
            return False
