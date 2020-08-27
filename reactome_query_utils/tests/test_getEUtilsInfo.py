from reactome_query_utils.getEUtilsInfo import getEUtilsInfo, getIndraQueryTermStmtCount
import sys
import os
sys.path.append('../../')


def test_getEUtilsInfo():
    os.environ["INDRA_DB_REST_URL"] = "https://db.indra.bio"
    pmid_list_path = "pmid_list.txt"
    
    getEUtilsInfo(pmid_list_path)
    assert os.path.exists("eutils_output.tsv")


def test_getIndraQueryTermStmtCount_scopedAPI():
    assert type(getIndraQueryTermStmtCount("DMRT1", ['reach'])) is int
