#!/bin/bash

# A script to set up dev environment, in particular creating virtual environment.
# TODO: Make this install requirements.txt to the virtual environment as well.

# Verify that the 'env' folder doesn't exist
if [ -d "env" ]; then
    echo "ERROR: The folder env already exists. This directory must be delted before the developer environment can be set up."
    exit 1
fi

# Output commands as they are run
set -x

# Create virtual environment
echo "+++ Creating Virtual Environment"
mkdir env
pip install virtualenv
python -m venv env

# Populate virtual environment with required packages
echo "+++ Creating Virtual Environment"