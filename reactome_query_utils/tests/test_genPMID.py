from reactome_query_utils.getPMID import getPMID
import sys
import os
import requests
sys.path.append('../../')


def test_getPMID_1():
    term = "DMRT1,20"
    pmid_list_path = "pmid_list.txt"
    getPMID([term], -1, pmid_list_path)
    assert os.path.exists(pmid_list_path)


def test_getPMID_2():
    term = "DMRT1,20"
    pmid_list_path = "pmid_list.txt"
    
    with open(pmid_list_path,"w") as f:
        f.write("")

    getPMID([term], 5, pmid_list_path)
    assert os.path.exists(pmid_list_path)
