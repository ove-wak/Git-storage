import jpype 
from jpype import *
# jvmPath = jpype.getDefaultJVMPath() 
jvmPath = u'C:\\Program Files\\Java\\jre-9.0.4\\bin\\server\\jvm.dll'
jpype.startJVM(jvmPath,"-Djava.class.path=C:\\Users\\ovewa\\Desktop\\lab\\cab.jar") 
cab = JClass('com.example.user.epcab.Cab')
c = cab()
for x in range(-90,0):
    print(c.getCabData("VIE-AL10",1,x))
jpype.shutdownJVM()