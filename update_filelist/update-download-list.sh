#!/bin/bash

[ $# -ne 1 ] &&\
echo "USAGE: $0 <var_file>" &&\
exit 1

echo "Updating SAP Download Files"

# preparing python venv
if [ ! -d ~/.venv/check_software ]; then
   python3 -m venv ~/.venv/check_software
   . ~/.venv/check_software/bin/activate
   python3 -m pip install ansible-core requests beautifulsoup4 lxml
else
  . ~/.venv/check_software/bin/activate
fi

if [ ! -d /tmp/ansible_collection/ansible_collections/community/sap_launchpad/plugins ]; then
  ansible-galaxy install git+https://github.com/sap-linuxlab/community.sap_launchpad.git,main -p /tmp/ansible_collection
fi
ansible-playbook -e venv=~/.venv/check_software \
                 -e ansible_python_interpreter=~/.venv/check_software/bin/python3 \
  		 -e var_file=${1}  \
                 -vv update_download_list.yml 


