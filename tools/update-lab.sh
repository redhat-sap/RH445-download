#!/bin/bash

cat << EOT
===========================================================================
Warning: this script makes updates to the environment that will break RH445
Only use, if you know what you are doing
===========================================================================
EOT

echo -n "Press Ctrl-C to stop or Enter to continue"
read ask

ansible-playbook -v -K -i localhost,utiliy update-lab.yml
