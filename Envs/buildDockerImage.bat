@echo off

set imageName=%1

if defined imageName (

    docker build -t %imageName% .

)