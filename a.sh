#!/bin/bash

cd
rm -rf spynel
git clone https://github.com/Spyware0/spynel
rm -rf a.sh
cd spynel
python3 spynel.py
