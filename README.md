# SessionImporter
This is a basic Session Importer library meant to output Session import files for various Connection managers. 


``` python
from SessionImporter import SessionImporter,Session,Folder
importer = SessionImporter() #Creates SessionImporter object
folder = Folder("TEST-Folder") #Creates folder named TEST-Folder
session = Session("TEST-Session","session hostname") #Creates Session named TEST-Session

folder.add(session) #Adds TEST-Session into TEST-Folder
importer.add(folder) #Adds TEST-Folder to the SessionImporter
importer.write_securecrt("test.xml") #Tells SessionImporter to write sessions to test.xml in SecureCRT compatible format.

```



Currently only basic SecureCRT sessions are supported.
