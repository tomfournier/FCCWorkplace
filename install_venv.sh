#!/bin/bash
export ROOTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# check if python3 is available locally
if ! [[ $(command -v python3) ]] 
then
    echo "Error: python3 not available locally, cannot continue!"
    exit 1
fi

echo "> getting latest pip"
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#python get-pip.py --user
#rm get-pip.py
pip install --upgrade pip
echo "> getting tools for local running"
python3 -m venv $ROOTDIR/local_env
source $ROOTDIR/local_env/bin/activate
python3 -m pip install -r $ROOTDIR/requirements.txt
