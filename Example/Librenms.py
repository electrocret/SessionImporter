from LibreNMSAPIClient import LibreNMSAPIClient #LibreNMSAPIClient https://github.com/electrocret/LibreNMSAPIClient
from SessionImporter import SessionImporter,Session,Folder

libreapi =  LibreNMSAPIClient()
importer = SessionImporter()

devices = libreapi.list_devices()

for device in devices:
	importer.add(Session(device.hostname,device.ip))

importer.write_securecrt("Librenms.xml")
