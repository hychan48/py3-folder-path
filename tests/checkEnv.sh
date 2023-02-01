#!/bin/bash
PYTHONPATH=`printenv PYTHONPATH`
#tmpdir=`printenv TMPDIR`
#/Applications/Sublime Text.app/Contents/SharedSupport/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbinecho
#echo ${BASH_SOURCE}
#echo "$(readlink -f "${BASH_SOURCE}")" # relative doesnt work on macOS
#echo "$(readlink -f "~/")" # doesnt work
# up one, and to a

if [ -z "$PYTHONPATH" ]
then
    echo empty
    A_PATH=$(dirname $(dirname $BASH_SOURCE))/a
    export PYTHONPATH="$A_PATH"
else
    echo something
  # backup
  # append :
fi

# restore
printenv PYTHONPATH