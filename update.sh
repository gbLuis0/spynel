#!/bin/bash
rm -rf spynel
git clone https://github.com/Spyware0/spynel
rm -rf update.sh
cd spynel
python main.py
