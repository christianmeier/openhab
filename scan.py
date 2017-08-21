#! /usr/bin/python 

from zeroconf import ServiceBrowser, Zeroconf
from time import sleep

class MyListener(object):
	def remove_service(self, zeroconf, type, name):
		print("Service %s removed" % (name,))
	def add_service(self, zeroconf, type, name):
		info = zeroconf.get_service_info(type, name)
		print("Service %s added, service info: %s" % (name, info))

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_zapp._tcp.local.", listener)
sleep(5.0)
zeroconf.close()
# End
# DEV
