from reactome_query_utils.getMeSH import getAbstracts
import sys
import os

sys.path.append('../../')


def test_extractListID():
    pmid_path = "pmid_list.txt"
    abstract_path = "abstract.txt"
    with open(pmid_path, "w") as file:
        file.write(
            "32674038~DMRT1\n32628996~DMRT1\n32590948~DMRT1\n32497821~DMRT1\n32447491~DMRT1\n")
    getAbstracts(abstract_path, pmid_path)
    assert os.path.exists(abstract_path)
