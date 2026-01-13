import os,platform
os.system('clear')
os.system('git pull')
os.system('xdg-open https://t.me/teamDTT404')
bit = platform.architecture()[0]
if bit=='64bit':
    print('YOUR DEVICE 64 BIT')
    import dump64
elif bit=='32bit':
    print('YOUR DEVICE 32 BIT ')
    import dump
