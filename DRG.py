
import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
DRAGON=platform.architecture()[0]
if DRAGON=="32bit":__import__("DRAGON32")
elif DRAGON=="64bit":__import__("DRAGON64")
