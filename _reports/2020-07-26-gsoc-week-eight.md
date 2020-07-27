---  
layout: post
title:  "Week Eight | Reactome Failed Query Analysis"
tags: [gsoc, weekly report, coding period ]
author: Priti Shaw
---
This blog highlights the methodology used to retrive information required for analysis of failed query terms in Reactome.  

The Code is available as [Python Notebook](https://gist.github.com/PritiShaw/fb8abb610ec8267d21150544aa245257) and [Docker Image](https://hub.docker.com/r/pritishaw/reactome-query-processing).

## Table of Contents  
1. [Input Data](#1-input-data)  
2. [Processing](#2-processing)  
    2.1. [PMID Extraction](#21-pmid-extraction)  
    2.2. [MESH Terms Extraction](#22-mesh-terms-extraction)  
    2.3. [Fetch Article Metadata](#23-fetch-article-metadata)  
3. [Output](#3-output)  
4. [Related Tasks](#4-related-tasks)  

## 1. Input Data  
The input file can be found [here](https://raw.githubusercontent.com/cannin/reach-query/master/queries.csv). It contains 101,647 query terms and the Reactome database hits associated with it.  
For analysis we have considered only those terms with hits greater than equal to 10 ie `hits >=10`  

## 2. Processing  
The processing was done in Google Colaboratory using a Python notebook and can be found [here](https://colab.research.google.com/gist/PritiShaw/fb8abb610ec8267d21150544aa245257/reactome-failed-query-processing.ipynb).  
Following steps are performed on each failed terms, steps *2.2* and *2.3* are run in parallel in code to reduce time taken for processing.  

### 2.1. PMID Extraction  
<sup>[Code Snippet](https://colab.research.google.com/gist/PritiShaw/fb8abb610ec8267d21150544aa245257/reactome-failed-query-processing.ipynb#scrollTo=rGjJnEF2d8xP)</sup>   
Using [E-Utilities](https://www.ncbi.nlm.nih.gov/books/NBK25499/) and the query term, we fetch the Pubmed articles where the term was seen.  
Sample API request  
`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=hasabstract%20AND%20{Failed_Query_term}`
  
Total number of such Pubmed articles and the first **20 PMIDs** are stored in a text file for further processing.  


### 2.2. MESH Terms Extraction  
<sup>[Code Snippet](https://colab.research.google.com/gist/PritiShaw/fb8abb610ec8267d21150544aa245257/reactome-failed-query-processing.ipynb#scrollTo=YtbRKt3Hcp4H)</sup>

Using [Batch MetaMap](https://ii.nlm.nih.gov/Batch/index.shtml) MESH terms from Pubmed articles abstracts are extracted.

Following is an analysis on time taken, in **seconds**, to get MESH terms  

| Number of abstract | Average Time taken | Time taken per abstract | Abstract processed in 24hrs |
|-|-|-|-|
| 1 | 43.2 | 43.2 | 2,000 |
| 3 | 43.6 | 14.53 | 5,946 |
| 5 | 42 | 8.4 | 10,285 |
| 10 | 43 | 4.3 | 20,093 |
| 50 | 40.6 | 0.81 | 106,666 |
| 100 | 41.2 | 0.41 | 210,731 |
| 200 | 72.4 | 0.36 | 240,000 |
| 500 | 137.2 | 0.27 | 320,000 |
| 1000 | 233.4 | **0.23** | 375,652 |

Therefore in bulk processing each Pubmed article will take **0.23 seconds**.  

### 2.3. Fetch Article Metadata  
<sup>[Code Snippet](https://colab.research.google.com/gist/PritiShaw/fb8abb610ec8267d21150544aa245257/reactome-failed-query-processing.ipynb#scrollTo=pnArpnW-fmNy)</sup>   
Using E-Utilities API and the PMID of the article following informations are retrived/calculated:  

|Parameter|Description|
|---|---|
|JOURNAL_TITLE|Journal Title for the Pubmed article|
|YEAR|Publication year|
|PMCID|PMCID of the Pubmed article|
|DOI|DOI of the Pubmed article|
|PMC_CITATION_COUNT|PubMed Central Citations for PMID|
|INDRA_STATEMENT_COUNT|INDRA statements extracted from Abstract|
|OC_CITATION_COUNT|Citations as per [OpenCitations](https://opencitations.net/)|
|INDRA_QUERY_TERM_STATEMENT_COUNT|INDRA statements extracted from Abstract after grounding the query term using [Gilda](https://github.com/indralab/gilda)|
|PMID_COUNT|Number of Pubmed articles where the term is seen|  

**Used API Endpoints**  

|Parameters|Sample Request|
|---|---|
|JOURNAL_TITLE,YEAR, DOI, PMCID|https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=**{PMID}**|
|PMC_CITATION_COUNT|https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pmc_refs&id=**{PMID}**|
|INDRA_STATEMENT_COUNT|[`indra_db_rest.get_statements_for_paper(PMID)`](https://indra.readthedocs.io/en/latest/modules/sources/indra_db_rest/#indra.sources.indra_db_rest.api.get_statements_for_paper)|
|OC_CITATION_COUNT|https://opencitations.net/api/v1/metadata/**{DOI}**|

## 3. Output  

The outputs from processing steps are merged to generate a Tab Seperated file. Final output can be found [here](https://raw.githubusercontent.com/PritiShaw/Reactome-Failed-Queries-Processing/master/output.tsv).  

The file contains following columns.
* QUERY_TERM
* PMID
* JOURNAL_TITLE
* YEAR
* PMCID
* DOI
* PMC_CITATION_COUNT
* INDRA_STATEMENT_COUNT
* OC_CITATION_COUNT
* INDRA_QUERY_TERM_STATEMENT_COUNT
* MESH_TERMS
* PMID_COUNT

## 4. Related Tasks  

- [Retrieve Information for Reactome Failed Searches](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/7)  
- [Extract Mesh Terms, Journal for Reactome Articles](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/6)  
- [Extracting MeSH Terms for Articles](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/1)
- [Add Citations from OpenCitations to Reactome Search](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/9)  
- [Add Count of INDRA Statements for Individual Terms](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/10)  
- [Add Documentation/Tests/Dockerfile to Reactome Failed Search Code](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/12)
