from reactome_query_utils.generateOutput import mergeOutputs
import sys
import os
sys.path.append('../../')


def test_mergeOutputs():
    generated_file = "merged_output.tsv"
    mesh_output_file = "mesh.txt"
    eutils_op_file = "eutils_output.tsv"
    mergeOutputs(generated_file, eutils_op_file, mesh_output_file)
    assert os.path.exists(eutils_op_file)