from LibreNMSAPIClient import LibreNMSAPIClient #LibreNMSAPIClient https://github.com/electrocret/LibreNMSAPIClient
from SessionImporter import SessionImporter,Session,Folder

libreapi =  LibreNMSAPIClient()
importer = SessionImporter()

devices = libreapi.list_devices()

for device in devices:
    if(device['ip'] == ""):
        importer.add(Session(device['sysName'], device['hostname']))
    else:
        importer.add(Session(device['sysName'], device['ip']))

importer.write_securecrt("Librenms.xml")

