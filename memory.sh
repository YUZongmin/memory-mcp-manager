#!/bin/bash

# Initialize configuration if it doesn't exist
if [ ! -f "config.json" ]; then
    python3 memory_manager.py init
fi

if [ "$#" -lt 1 ]; then
    echo "Usage:"
    echo "  Initialize config:  ./memory.sh init"
    echo "  Add memory path:    ./memory.sh add <name> <path>"
    echo "  Remove memory path: ./memory.sh remove <name>"
    echo "  List memory paths:  ./memory.sh list"
    echo "  Switch memory:      ./memory.sh switch <name>"
    echo "  Add client:         ./memory.sh add-client <name> <config_path>"
    echo "  List clients:       ./memory.sh list-clients"
    exit 1
fi

python3 memory_manager.py "$@" 