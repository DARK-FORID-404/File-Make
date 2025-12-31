import os,platform
os.system('clear')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    print('YOUR DEVICE 64 BIT')
    print('64 BIT NOT AVAIABLE NOW')
elif bit=='32bit':
    print('YOUR DEVICE 32 BIT ')
    import dump
