from reactome_query_utils.getPMID import _extractListID
import sys
import os
import requests
sys.path.append('../../')


def test_extractListID():
    term = "DMRT1"
    pmid_list_path = "pmid_list.txt"
    xml_content = requests.get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=hasabstract%20AND%20"+term)
    _extractListID(xml_content.text, term, pmid_list_path)
    assert os.path.exists(pmid_list_path)
