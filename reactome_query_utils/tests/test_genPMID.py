from reactome_query_utils.getPMID import getPMID
import sys
import os
import requests
sys.path.append('../../')


def test_getPMID():
    term = "DMRT1,20"
    pmid_list_path = "pmid_list.txt"
    getPMID([term], 5, pmid_list_path)
    assert os.path.exists(pmid_list_path)
