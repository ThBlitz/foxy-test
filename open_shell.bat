@echo off

set containerName=%1

docker exec -ti %containerName% bash