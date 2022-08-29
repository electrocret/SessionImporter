# SessionImporter
This is a basic Session Importer library meant to output Session import files for various Connection managers. 


``` python
importer = SessionImporter()
folder = Folder("test folder")
session = Session("session name","session hostname")

folder.add(session)
importer.add(folder)
importer.write_securecrt("test.xml")

```



Currently only basic SecureCRT sessions are supported.
