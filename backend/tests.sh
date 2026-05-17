#!/bin/bash

if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    echo "This script must not be sourced"
    exit 1
fi

echo -e "\n---> Running PyRestTest APIs..."
pyresttest http://proxy ./tests/api.yml

echo -e "\n---> Running PyTest Frontend Selenium Tests..."
pytest tests/test_ui.py
