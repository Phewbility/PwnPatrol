#!/bin/bash

tpBlue=$(tput setaf 4)
tpEnd=$(tput sgr0)
tpGreen=$(tput setaf 2)
tpRed=$(tput setaf 1)
tpYellow=$(tput setaf 3)

if [ "$EUID" -ne 0 ]; then
  echo "${tpRed}This needs to be installed as root (use sudo).${tpEnd}" >&2
  exit 1
fi

echo "${tpYellow} Checking git ..."

if ! command -v git &> /dev/null; then
  echo "${tpRed}Git not found!${tpEnd}"
  echo "${tpYellow}Installing git...${tpEnd}"
  apt-get install -y git
  echo "${tpGreen}Git installed successfully.${tpEnd}"
else
  echo "${tpGreen}Git found and already installed.${tpEnd}"
fi

echo "${tpYellow} Checking Python3 ..."
if ! command -v python3 &> /dev/null; then
  echo "${tpRed}Python3 not found!${tpEnd}"
  echo "${tpYellow}Installing Python3...${tpEnd}"
  apt-get install -y python3
  echo "${tpGreen}Python3 successfully installed.${tpEnd}"
else
  echo "${tpGreen}Python3 found and already installed.${tpEnd}"
fi


echo "${tpYellow} Checking Radare2..."
if ! command -v r2 &> /dev/null; then
  echo "${tpRed}Radare2 not found!${tpEnd}"
  echo "${tpYellow}Installing Radare2...${tpEnd}"
  cd $HOME
  git clone https://github.com/radareorg/radare2
  radare2/sys/install.sh
else
  echo "${tpGreen}Radare2 Found !${tpEnd}"
fi

echo "${tpYellow} Checking r2pm libraries needed..."
echo "${tpYellow} Checking r2ghidra..."
if ! r2pm -l|grep "r2ghidra" &> /dev/null; then
  echo "${tpRed}r2ghidra not found!${tpEnd}"
  echo "${tpYellow}Installing ...${tpEnd}"
  r2pm -ci r2ghidra
  echo "${tpGreen}r2ghidra successfully installed.${tpEnd}
else
  echo "${tpGreen}r2ghidra Found !"
fi
echo "${tpYellow} Checking r2dec..."
if ! r2pm -l|grep "r2dec" &> /dev/null; then
  echo "${tpRed}r2dec not found!${tpEnd}"
  echo "${tpYellow}Installing ...${tpEnd}"
  r2pm -ci r2dec
  echo "${tpGreen}r2dec successfully installed.${tpEnd}
else
  echo "${tpGreen}r2dec Found !${tpEnd}"
fi
echo "${tpYellow} Checking r2ghidra-sleigh..."
if ! r2pm -l|grep "r2ghidra-sleigh" &> /dev/null; then
  echo "${tpRed}r2ghidra-sleigh not found!${tpEnd}"
  echo "${tpYellow}Installing ...${tpEnd}"
  r2pm -ci r2ghidra-sleigh
  echo "${tpGreen}r2ghidra-sleigh successfully installed.${tpEnd}
else
  echo "${tpGreen}r2ghidra Found !${tpEnd}"
fi 
echo "${tpYellow} Checking Hardening-check..."
if ! command -v hardening-check &> /dev/null; then
  echo "${tpRed}Hardenig-Check not found!${tpEnd}"
  echo "${tpYellow}Installing Hardening-Check...${tpEnd}"
  apt install devscripts -y
  echo "${tpGreen}devscript successfully installed.${tpEnd}
else
  echo "${tpGreen}Hardening Check Found !${tpEnd}"
fi
echo "${tpYellow} Intstalling pip requirements...${tpEnd}"
pip3 install -r requirements.txt
echo "${tpBlue} Installation COMPLETE !"
echo "${tpBleu} Enjoy Pwning !${tpEnd}"

