@echo off

set imageName=%1
set versionName=%2

if defined imageName (

    docker build -t %imageName% -f Envs/%versionName%.Dockerfile .

)