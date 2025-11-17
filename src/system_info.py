import socket
import uuid


def get_system_info():
return {
"hostname": socket.gethostname(),
"local_ip": socket.gethostbyname(socket.gethostname()),
"mac_address": hex(uuid.getnode())
}
