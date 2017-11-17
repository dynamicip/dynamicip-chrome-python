from subprocess import call

call(["docker", "build", "-t", "dynamicip-chrome-python-base", "-f", "Dockerfile.base", "."])