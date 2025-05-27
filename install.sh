#!/bin/bash
# This script installs the Uzbek Latin Hunspell dictionary on a Debian-based system.

# Check if the script is run as root

cp ./uz-lat.dic /usr/share/hunspell/uz_UZ.dic
cp ./uz-lat.aff /usr/share/hunspell/uz_UZ.aff

