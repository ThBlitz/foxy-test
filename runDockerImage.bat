@echo off

set imageName=%1
set containerName=%2

if defined imageName (

    if not defined containerName (
        containerName = test
    )

        docker run --rm -d -t --name=%containerName% ^
        -p 8888:8888 -p 3000:3000 ^
        --mount src=%cd%,target=/home/mount,type=bind ^
        %imageName%

        docker exec -ti %containerName% bash

)