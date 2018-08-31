import jpype 
from jpype import *
# jvmPath = jpype.getDefaultJVMPath() 
jvmPath = u'C:\\Program Files\\Java\\jre-9.0.4\\bin\\server\\jvm.dll'
jpype.startJVM(jvmPath,"-Djava.class.path=C:\\Users\\ovewa\\Desktop\\lab\\cab.jar") 
cab = JClass('com.example.user.epcab.Cab')
c = cab()
apt=['-33', '-39', '-41', '-59', '-62', '-67', '-68', '-69', '-70', '-70', '-71', '-73', '-75', '-76', '-78', '-80', '-83', '-84', '-84', '-85', '-90', '-91', '-200', '-200', '-200', '-200', '-200', '-200', '-200', '-200', '-200', '-200']
# for x in range(-90,0):
for j in range(len(apt)):
            if int(apt[j]) != -200:
                apt[j] = c.getCabData("room_device",1,apt[j])
                print(apt[j])
jpype.shutdownJVM()