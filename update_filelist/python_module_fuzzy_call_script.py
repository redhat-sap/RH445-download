#!/usr/bin/env python3
import sys
input_search_file=sys.argv[1]
input_search_file_name_and_version_only=sys.argv[2]
username=sys.argv[3]
password=sys.argv[4]
sys.path.append('/tmp/ansible_collection/ansible_collections/community/sap_launchpad/plugins')
from module_utils.sap_launchpad_software_center_download_search_fuzzy import *
sap_sso_login(username, password)
query_result = search_software_fuzzy(input_search_file)
if len(query_result) >= 2:
    if '70SWPM' in query_result[0]['Title']:
        print(query_result[-1]['Title'])
    elif any('DBATL' in sublist['Title'] for sublist in query_result):
        for sublist in query_result:
            if sublist['Title'].startswith('DBATL'):
                print(sublist['Title'])
    elif any('SYBCTRL' in sublist['Title'] for sublist in query_result):
        for sublist in query_result:
            if sublist['Title'].startswith('SYBCTRL'):
                print(sublist['Title'])
    elif any('IMDB_CLIENT20' in sublist['Title'] for sublist in query_result):
        input_imdb_client = input_search_file_name_and_version_only[:-2]
        list_imdb_client = []
        for sublist in query_result:
            if sublist['Title'].startswith(input_imdb_client):
                list_imdb_client.append(sublist['Title'])
        list_imdb_client.sort(reverse=True)
        print(list_imdb_client[0])
    elif any('IMDB_AFL' in sublist['Title'] for sublist in query_result):
        input_imdb_afl = input_search_file_name_and_version_only[:-1]
        list_imdb_afl = []
        for sublist in query_result:
            if sublist['Title'].startswith(input_imdb_afl):
                list_imdb_afl.append(sublist['Title'])
        list_imdb_afl.sort(reverse=True)
        print(list_imdb_afl[0])
    elif any('IMDB_LCAPPS' in sublist['Title'] for sublist in query_result):
        input_imdb_lcapps = input_search_file_name_and_version_only[:-1]
        list_imdb_lcapps = []
        for sublist in query_result:
            if sublist['Title'].startswith(input_imdb_lcapps):
                list_imdb_lcapps.append(sublist['Title'])
        list_imdb_lcapps.sort(reverse=True)
        print(list_imdb_lcapps[0])
    elif any('IMDB_SERVER' in sublist['Title'] for sublist in query_result):
        for sublist in query_result:
            input_imdb_server = input_search_file_name_and_version_only[:-1]
            if sublist['Title'].startswith(input_imdb_server):
                print(sublist['Title'])
    # As SAP WebDisp file name numbering does not use preceeding 0's, manually filter out v7 which is older than v69:
    elif any('SAPWEBDISP' in sublist['Title'] for sublist in query_result):
        input_webdisp = input_search_file_name_and_version_only[:-2]
        list_webdisp = []
        for sublist in query_result:
            if sublist['Title'].startswith(input_webdisp) and not sublist['Title'].startswith('SAPWEBDISP_SP_7'):
                list_webdisp.append(sublist['Title'])
        list_webdisp.sort(reverse=True)
        print(list_webdisp[0])
    else:
        print("\nERROR. More than 1 result, manual intervention required....")
        for item in query_result:
            print('Identified ' + item['Title'] + ' : ' + item['Description'] + ', ' + item['Infotype'],end='\n')
else:
    print(query_result[0]['Title'])
