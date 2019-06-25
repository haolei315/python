import re
str1='Port-channel1.189   192.168.189.254  YES   CONFIG  up'
a=re.match('(\w*\-[a-z0-9A-Z]*\.\d*)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(YES|NO)\s+([A-Z]*)\s+([a-z]*)',str1).groups()
print(a)
print('-'*63)
print('%-5s:%-10s'%('接口',a[0]))
print('%-5s:%-10s'%('IP地址',a[1]))
print('%-5s:%-10s'%('状态',a[2]))
print('%-6s:%-10s'%('起',a[4]))