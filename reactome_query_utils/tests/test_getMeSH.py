from reactome_query_utils.getMeSH import getAbstracts
import sys
import os

sys.path.append('../../')


def test_extractListID():
    pmid_path = "pmid_list.txt"
    abstract_path = "abstract.txt"
    getAbstracts(abstract_path, pmid_path)
    assert os.path.exists(abstract_path)
