#!/bin/bash
# This script installs the Uzbek Latin Hunspell dictionary on different platforms.
# Detect the platform

OS="$(uname)"

case "$OS" in 
  'Linux')
    # Debiloid only
    echo "🔧 Copying to /usr/share/hunspell (requires sudo)"
    sudo cp ./uz_UZ.dic /usr/share/hunspell/uz_UZ.dic
    sudo cp ./uz_UZ.aff /usr/share/hunspell/uz_UZ.aff
    sudo cp ./uz_UZ_Cyrl.dic /usr/share/hunspell/uz_UZ_Cyrl.dic
    sudo cp ./uz_UZ_Cyrl.aff /usr/share/hunspell/uz_UZ_Cyrl.aff
    sudo cp ./uz_UZ_2026.dic /usr/share/hunspell/uz_UZ_2026.dic
    sudo cp ./uz_UZ_2026.aff /usr/share/hunspell/uz_UZ_2026.aff
    echo "✅ Installed on Linux"
    ;;

  'Darwin')
    echo "🔧 Copying to ~/Library/Spelling"
    mkdir -p ~/Library/Spelling
    cp ./uz_UZ.dic ~/Library/Spelling/uz_UZ.dic
    cp ./uz_UZ.aff ~/Library/Spelling/uz_UZ.aff
    cp ./uz_UZ_Cyrl.dic ~/Library/Spelling/uz_UZ_Cyrl.dic
    cp ./uz_UZ_Cyrl.aff ~/Library/Spelling/uz_UZ_Cyrl.aff
    cp ./uz_UZ_2026.dic ~/Library/Spelling/uz_UZ_2026.dic
    cp ./uz_UZ_2026.aff ~/Library/Spelling/uz_UZ_2026.aff
    echo "✅ Installed on macOS"
    ;;

  'FreeBSD')
    echo "Detected FreeBSD (not supported yet)"
    ;;

  'WindowsNT' | 'MINGW'* | 'CYGWIN'*)
    echo "Detected Windows (not supported by this script)"
    ;;

  *)
    echo "Unknown OS: $OS"
    ;;

esac