from xml.etree.ElementTree import parse
from urllib.request import urlopen
import time
import os
import requests


def getAbstracts(abstract_filepath, pmid_path):
    """
    Get abstracts from PMID and generate input file for MESH Batch processing

    Parameters:
    ---
    abstract_filepath:
        File path where abstracts will be written.
    pmid_path:
        File path to list of PMIDs to process
    """
    with open(pmid_path) as file:
        with open(abstract_filepath, 'wb') as abstract_file:
            for inp in file:
                pmid = inp.strip().split("~")[0]
                flag = True
                while flag:
                    try:
                        var_url = urlopen(
                            'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=' + pmid)
                        flag = False
                    except:
                        time.sleep(.5)
                xmldoc = parse(var_url)
                for item in xmldoc.iterfind('PubmedArticle'):
                    try:
                        abstract_text = item.findtext(
                            'MedlineCitation/Article/Abstract/AbstractText')
                        article_title = item.findtext(
                            'MedlineCitation/Article/ArticleTitle')
                        if abstract_text:
                            abstract_file.write(
                                f"UI  - {pmid}\nTI  - {article_title}\nAB  - {abstract_text}\n\n".encode("ascii", "ignore"))
                        else:
                            print("Err: MESH: ", "Undefined Abstract")
                    except Exception as e:
                        print("Err: MESH: ", e)


def getMeSH(mti_email_id, mti_username, mti_password, batch_processor, pmid_path="pmid_list.txt", abstract_filepath='abstract.txt', mesh_output_file="mesh.txt"):
    """
    Extracts MeSH terms from PMID extracts.
    MTI login details from https://utslogin.nlm.nih.gov/cas/login are required

    Parameters:
        mti_email_id  
        mti_username  
        mti_password  
        batch_processor  
        pmid_path:
            File Path to list of PMIDs
        abstract_filepath:
            File Path where abstracts will be written
        write_to_file:
            If True, output will be written to a file
        mesh_output_file:
            File Path where output file will be generated

    Returns:
        String:
            Result from MTI after processing the abstracts
    """
    getAbstracts(abstract_filepath, pmid_path)

    result = batch_processor.processor(
        ["--email", mti_email_id, abstract_filepath], mti_username, mti_password)

    with open(mesh_output_file, "w") as op_file:
        op_file.write(result)

    return result
