import jpype 
from jpype import *

jvmPath = u'C:\\Program Files\\Java\\jre-9.0.4\\bin\\server\\jvm.dll'
jpype.startJVM(jvmPath,"-Djava.class.path=C:\\Users\\ovewa\\Desktop\\trans.jar")
trans = JClass('wak.Trans')
# transt = trans()
ab = []
ab.append(3378842.44752)
ab.append(34058.68693)
ba = trans.xy2LB(ab)
print(ba)
jpype.shutdownJVM()
