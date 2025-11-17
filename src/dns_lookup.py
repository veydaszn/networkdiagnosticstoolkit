import socket


def resolve_domain(domain):
try:
ip = socket.gethostbyname(domain)
return True, ip
except:
return False, "Unable to resolve domain"
