#!/bin/bash -e

# run unit tests
cd ./tools/tests
python jsonschematests.py -v
