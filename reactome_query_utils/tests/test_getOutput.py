from reactome_query_utils.generateOutput import mergeOutputs
import sys
import os
sys.path.append('../../')


def test_mergeOutputs():
    generated_file = "merged_output.tsv"
    mesh_output_file = "mesh.txt"
    with open(mesh_output_file, 'w') as mesh_file:
        mesh_file.write("32793114|Male|C0086582|4978\n32793114|Spermatogenesis|C0037864|3978\n32793114|Testis|C0039597|1590\n32793114|Follicle Stimulating Hormone|C0733758|1508\n32793114|Spermatogonia|C0037866|1471\n32793114|Luteinizing Hormone|C0023607|1116\n32793114|Spermatozoa|C0037868|564\n32793114|Meiosis|C0025186|279\n32793114|Adult Germline Stem Cells|C3658291|216\n32765585|Animals|C0003062|14576\n32765585|Sea Bream|C0329120|13576\n32765585|Gonads|C0018067|8508\n32765585|Gene Expression Profiling|C0752248|2220\n32765585|Sex Determination Processes|C0524972|367\n32752987|Animals|C0003062|12448\n32752987|Female|C0086287|12448\n32752987|Male|C0086582|12448\n32752987|Temperature|C0039476|11448\n32752987|Hot Temperature|C2350229|2029\n32752987|Phenotype|C0031437|3723\n32752987|Radiation|C0851346|2019\n32752987|Sex Determination Processes|C0524972|1507\n32752987|Sex Ratio|C0036893|979\n32752987|Reptiles|C0035161|813\n32752987|Turtles|C0041412|716\n32752987|Electromagnetic Phenomena|C2350450|324\n32741963|Humans|C0086418|80016\n32741963|Male|C0086582|80016\n32741963|Arrest of spermatogenesis|C0232981|79016\n32741963|Azoospermia|C0004509|79015\n32741963|Exome|C3178814|6458\n32741963|Oligospermia|C0028960|3672\n32741963|Infertility, Male|C0021364|3068\n32741963|Spermatogenesis|C0037864|1239\n32741963|Testis|C0039597|802\n32741963|Spermatozoa|C0037868|630\n32741963|Dissection|C0012737|339\n32731992|Animals|C0003062|97380\n32731992|Female|C0086287|97380\n32731992|Male|C0086582|97380\n32731992|Gastrointestinal Microbiome|C4018878|96380\n32731992|Chickens|C0008051|31532\n32731992|RNA, Ribosomal, 16S|C0035702|9580\n32731992|Body Weight|C0005910|17874\n32731992|Genotype|C0017431|6954\n32731992|Bacteria|C0004611|2726\n32731992|Microbiota|C3887843|1346\n32731992|Thinness|C0039870|1212\n32731992|Feces|C0015733|1071\n32731992|Overweight|C0497406|254\n")

    mergeOutputs(generated_file, "eutils_output.tsv", mesh_output_file)
