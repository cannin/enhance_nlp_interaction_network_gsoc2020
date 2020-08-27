import jnius_config
jnius_config.add_classpath("./reactome_query_utils/tests/lib/*")
from reactome_query_utils.getMeSH import getMeSH
import sys
import os
from jnius import autoclass
GenericBatchNew = autoclass("GenericBatchNew")

sys.path.append('../../')


def test_getMeSH():
    pmid_path = "pmid_list.txt"
    abstract_path = "abstract.txt"
    mesh_output_file = "mesh.txt"
    username = "PritiShaw"
    password = "Gsoc2020"
    processor = GenericBatchNew()
    result = getMeSH("ci@github.com", username, password, processor,
                     abstract_filepath=abstract_path,
                     mesh_output_file=mesh_output_file,
                     pmid_path=pmid_path
                    )
    assert len(result.splitlines()) > 1 and os.path.exists(
        abstract_path) and os.path.exists(mesh_output_file)
