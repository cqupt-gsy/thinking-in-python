"forks child processes until you type 'q'"

import os

def child():
    print('Hello from child',  os.getpid())
    os._exit(0)  # else goes back to parent loop

def parent():
    while True:
        newpid = os.fork()#如果开启了子进程成功返回0
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break

parent()
