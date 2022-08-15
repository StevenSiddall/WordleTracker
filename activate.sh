#!/bin/bash

# A script to activate the python virtual environment. Source this script rather than executing to 
# run in context of forking process.

# Verify that the 'env' folder doesn't exist
if [ -d "env" ]; then
    # Verify activate was sourced, otherwise remind developer to source this script
    if [ "$0" = "$BASH_SOURCE" ]; then
        echo "ERROR: The activate script must be called as 'source activate.sh'"
        exit 1
    fi

    echo "+++ Activating virtual environment..."
    source env/Scripts/activate

    echo "Complete - Run 'deactivate' to deactivate the virtual environment"
else
    echo "ERROR: The virtual environment has not been created yet. Please run './setup.sh' to create the virtual environment."
    exit 1
fi