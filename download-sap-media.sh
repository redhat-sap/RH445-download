#!/bin/bash

cat << EOT

============
 Disclaimer
============

SAP does not allow us to provide the SAP Software for installing SAP S/4HANA Foundation with you.
Hence you need to bring the installation binaries on your own.

If you have an SAP S-User and oassword with the permission to download SAP Software from their software marketplace, 
this script downloads the SAP software for you to the right location. Please ask your SAP team to provide an S-User with
software download permission to you.

If you do not have an S-User and the software is stored centrally at your company, you can also upload the
software to the fileserver in this lab.

For this course we need the following Software:

- HANA 2 SPS 06 
- S4HANA 2021 Foundation 
- SWPM/SUM
- SAPCAR 

Here are the current versions of the files you need to provide:

On server utility in directory /export/sap-software/HANA2SPS06:
EOT

## Parse current sap-dl.yml
ansible -e @sap-dl.yml -m debug -a "msg='{{ hdb2sps06 + sapcar}}'" localhost  | egrep -v 'SUCCESS|msg|\]|\}'

echo ""
echo "On server utility in directory /export/sap-software/S4HANA.FQDN"

## Parse current sap-dl.yml
ansible -e @sap-dl.yml -m debug -a "msg='{{ s4fndn2021 + swpm + sapcar}}'" localhost  | egrep -v 'SUCCESS|msg|\]|\}'

echo ""
echo "Press Ctrl-C to stop downloading with S-User and provide the software on your own"
echo "or enter your SAP credentials with download permissions"
echo ""
ansible-galaxy collection install -r ./collections/requirements.yml 2>&1 > /dev/null
ansible-playbook -v -i utility, \
                 -u devops \
                 download-sap-media.yml 



