#!/usr/bin/env bash
push_to_remote ()
{
    echo -n "   $1"
    git push $1 master > /dev/null 2>&1 &
    spin='-\|/'
    PID=$!
    while kill -0 $PID 2> /dev/null; do
        i=$(( (i+1) %4 ))
        printf "\r ${spin:$i:1}"
        sleep .1
    done
    printf "\r ✔ "
    echo
}

push_to_remote origin
push_to_remote heroku

# if the above doesn't work out well just
# git push origin master
# git push heroku master
