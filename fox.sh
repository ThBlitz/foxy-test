#!/usr/bin/bash

#sed -i.bak s/$'\r'//g ./path_settings


if [ -z ${VIRTUAL_ENV} ]
then
    VIRTUAL_ENV="__none__"
fi

workingDirectory=$PWD

. $workingDirectory/.foxy

if [ -n ${py_envs} ]
then
    py_envs=$workingDirectory$py_envs
else
    py_envs=$workingDirectory
fi

# if [ $arg1 == "activate" ]
# then
#     source $py_envs/$arg2/bin/activate
if [ -n ${fox_path} ] && [ -n ${py_exe} ]
then
    $py_exe $fox_path $@ $PWD $VIRTUAL_ENV $py_envs
fi



