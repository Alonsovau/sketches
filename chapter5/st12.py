import os
print(os.path.exists('/etc/passwd'))
print(os.path.exists('c:/users'))
print(os.path.isfile('c:/users'))
print(os.path.isdir('c:/users'))
print(os.path.getsize('c:/users/alons/hsqlprefs.dat'))
print(os.path.getmtime('c:/users/alons/hsqlprefs.dat'))