from LibreNMSAPIClient import LibreNMSAPIClient #LibreNMSAPIClient https://github.com/electrocret/LibreNMSAPIClient
from SessionImporter import SessionImporter,Session,Folder

libreapi =  LibreNMSAPIClient()
importer = SessionImporter()
lnmssessions=Folder("LibreNMS Sessions")

devices = libreapi.list_devices()

for device in devices:
    if(device['ip'] == ""):
        lnmssessions.add(Session(device['sysName'], device['hostname']))
    else:
        lnmssessions.add(Session(device['sysName'], device['ip']))

importer.add(lnmssessions)
importer.write_securecrt("Librenms.xml")

