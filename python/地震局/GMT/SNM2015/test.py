#python调用bat文件
import subprocess
p = subprocess.Popen("cmd.exe /c" + "C:\\Users\\ovewa\\Desktop\\GMT\\GMT\\SNM2015\\SNM2015_test.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
curline = p.stdout.readline()
while(curline != b''):
    print(curline)
    curline = p.stdout.readline()
     
#注意wait可能引起的死锁
p.wait()
print(p.returncode)