from subprocess import call

if  call(["docker", "build", "-t", "dynamicip-chrome-python", "."]) == 0:
    call(["docker", "run", "-v", "/dev/shm:/dev/shm", "dynamicip-chrome-python"])