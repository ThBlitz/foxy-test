@echo off

set imageName=%1
set arg2=%2

if defined imageName (

    if not defined arg2 (
        set containerName=%imageName%
    ) else (
        set containerName=%arg2%
    )

        echo image name     : %imageName%
        echo container name : %containerName%

        docker run --rm -d -t --name=%containerName% ^
        -p 8888:8888 -p 3000:3000 ^
        --mount src=%cd%,target=/home/mount,type=bind ^
        %imageName%

)