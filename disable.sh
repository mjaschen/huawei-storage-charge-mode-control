#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

if [[ ! -f ".env" ]]; then
    echo "Please create a .env file (see .env.template)"

    exit 1
fi

if [[ ! -x "venv/bin/python" ]]; then
    echo "Please create a virtual environment and install dependencies (see README.md)"

    exit 1
fi

source .env
source venv/bin/activate

python ac-charge.py --ip "$IP_ADDRESS" --inverter "$INVERTER_ID" off
