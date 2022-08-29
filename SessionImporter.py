import xml.etree.ElementTree as ET
import xml.dom.minidom
from abc import ABC, abstractmethod

class Import_Obj(ABC):
	@abstractmethod
	def name(self):
		pass
	@abstractmethod
	def import_securecrt(self,elm):
		pass
	

class SessionImporter(Import_Obj):
 def __init__(self):
  self._contents=[]

        
 def import_securecrt(self,file):
  tree = ET.Element("VanDyke")
  tree.set("version", "3.0")

  sessions = ET.SubElement(tree, "key")
  sessions.set("name", "Sessions")
  for content in self._contents:
    content.import_securecrt(elm)
  mydata = ET.tostring(tree)
  dom = xml.dom.minidom.parseString(mydata)
  xml_file=dom.toprettyxml()
  with open(file, "w") as xml_write:
   xml_write.write(xml_file)
	
 def get(self, Name, Type = None):
  for imp_obj in self._contents:
   if (Type == None or type(imp_obj) == Type) and imp_obj.name() == Name:
    return imp_obj
  return None
			
 def add(self, imp_obj):
  if isssubclass(imp_obj,Import_Obj) and type(imp_obj) != SessionImporter:
   self._contents.push(imp_obj)

 def hasFolder(self, Foldername):
  return self.get(Foldername,"Folder") != None

class Session(Import_Obj):
 def __init__(self, name,Hostname,Protocol_Name="SSH2",Jumphost=None):
  self._name=name
  self._Hostname=Hostname
  self._Protocol_Name=Protocol_Name
  if Jumphost is not None:
      self._Jumphost=Jumphost
		
 def import_securecrt(self,elm):
  session = ET.SubElement(elm, "key")
  session.set("name", self._name)
		
  session_hostname = ET.SubElement(session, "string")
  session_hostname.set("name", "Hostname")
  session_hostname.text = self._Hostname
		
  session_protocol = ET.SubElement(session, "string")
  session_protocol.set("name", "Protocol Name")
  session_protocol.text = self._Protocol_Name
  if hasattr(self,'_Jumphost'):
   session_jumphost = ET.SubElement(session, "string")
   session_jumphost.set("name", "Firewall Name")
   session_jumphost.text = self._Jumphost

class Folder (SessionImporter):
 def __init__(self, name):
  super().__init__()
  self._name=name
  
 def import_securecrt(self,elm):
  folder = ET.SubElement(elm, "key")
  folder.set("name", self._name)
  for content in self._contents:
   content.import_securecrt(folder)
