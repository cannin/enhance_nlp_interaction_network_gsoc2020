from reactome_query_utils.getEUtilsInfo import getEUtilsInfo, getIndraQueryTermStmtCount
import sys
import os
sys.path.append('../../')


def test_getEUtilsInfo():
    os.environ["INDRA_DB_REST_URL"] = "https://db.indra.bio"
    pmid_list_path = "pmid_list.txt"
    with open(pmid_list_path, "w") as f:
        f.write("32793114~DMRT1~720\n32765585~DMRT1~720\n32752987~DMRT1~720\n32741963~DMRT1~720\n32731992~DMRT1~720\n")
    getEUtilsInfo(pmid_list_path)
    assert os.path.exists("eutils_output.tsv")


def test_getIndraQueryTermStmtCount_scopedAPI():
    assert type(getIndraQueryTermStmtCount("DMRT1", ['reach'])) is int
