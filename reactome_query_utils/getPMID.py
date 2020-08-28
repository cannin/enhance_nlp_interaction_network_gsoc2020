"""Extaction of PMID from search terms"""

import time
import xml.etree.ElementTree as ET
import requests
import logging as logger


def _extractListID(filecontent, term, pmid_list_path):
    tree = ET.fromstring(filecontent, ET.XMLParser(encoding='utf-8'))
    ID = tree.findall('./IdList/Id')
    count = tree.find('./Count').text
    with open(pmid_list_path, "a") as op_file:
        for i in ID:
            print(i.text + "~" + term + "~" + count, file=op_file)


def getPMID(terms, pmid_threshold=20, pmid_list_path="pmid_list.txt"):
    """
    Get PMID for the Query terms
    Parameters:
    terms: List of failed query terms
    pmid_threshold: Limit of Pubmed articles to process, default is 20
    """
    if pmid_threshold < 1:
        pmid_threshold = 20
    for term in terms:
        term = term.strip().rpartition(",")[0]
        flag = True
        while flag:
            try:
                xml_content = requests.get(
                    f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax={pmid_threshold}&term=hasabstract%20AND%20{term}")
                _extractListID(xml_content.text, term, pmid_list_path)
                flag = False
            except Exception as err:
                logger.warning("%s: %s", term, err)
                time.sleep(.5)
