#!/usr/bin/env bash

progress ()
{
    echo -n "   $1"
    spin='-\|/'
    PID=$!
    while kill -0 $PID 2> /dev/null; do
        i=$(( (i+1) %4 ))
        printf "\r ${spin:$i:1}"
        sleep .1
    done
    if [ "$2" != "0" ]; then
        wait $!
        if [ $? -ne 0 ]; then
            printf "\r ! "
            echo
            echo $2
            exit 1
        fi
    fi
    printf "\r ✔ "
    echo
}

git push origin master > /dev/null 2>&1 &
progress "pushing to github" "Probable network problem - try pushing manually."

git push heroku master > /dev/null 2>&1 &
progress "deploy to heroku" "Try to deploy manually with git push heroku master."
