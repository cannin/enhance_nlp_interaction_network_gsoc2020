---
layout: post
title:  "Week Six | Information Retrival"
tags: [gsoc, weekly report, coding period ]
author: Priti Shaw
---  
Continuing to last week's work, this week we aimed to retrieve the information for the Reactome [failed queries](https://raw.githubusercontent.com/cannin/reach-query/master/queries.csv).  


## Work Progress  

1. **Retrieve Information for Reactome Failed Searches**  

    Status: **In Progress**  
    The objective was to add additional columns DOI, PMC_CITATION_COUNT, INDRA_STATEMENT_COUNT to the previously created table. The total number of failed queries is greater than 10 million so I am still running the rest of queries on my system.  

    **Issue:** [Retrieve Information for Reactome Failed Searches](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/7)  
    **Repository:** [Reactome-Failed-Queries](https://github.com/PritiShaw/Reactome-Failed-Queries)  
    **Output:** [final_output.tsv](https://github.com/PritiShaw/Reactome-Failed-Queries/blob/master/outputs/final_output.tsv)  


2. **Clean Up Code Repo Provide Pipfiles for Code**  

    Status: **In Progress**  
    The aim is to provide proper Pipfiles for the existing code, maintain and clean up the code repository.  

    **Issue:** [Provide Pipfiles for code](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/8)  

3. **Add Citations from OpenCitations to Reactome Search**  

    Status: **Complete**  
    Along with the columns mentioned in WorkProgress#1, the aim was to add one more column(OC_CITATION_COUNT) citations from OpenCitations to Reactome Search.  

    **Issue:**  
        - [Retrieve Information for Reactome Failed Searches](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/7)  
        - [Add citation count](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/9)  
    **Output:** [final_output.tsv](https://github.com/PritiShaw/Reactome-Failed-Queries/blob/master/outputs/final_output.tsv)  


4. **Add Count of INDRA Statements for Individual Terms**  

    Status: **In Progress**  
    Again, along with the columns mentioned in WorkProgress#1, the aim was to add one more column(INDRA_QUERY_TERM_STATEMENT_COUNT) to count INDRA Statements for Individual Terms. Along with this, we are trying to submit a PR related to only return back those statements which are from specific source_apis(e.g: reach).  

    **Issue:**  
    - [Add Count of INDRA Statements](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/10)  
    - [Retrieve Information for Reactome Failed Searches](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/7)  
    **Output:** [final_output.tsv](https://github.com/PritiShaw/Reactome-Failed-Queries/blob/master/outputs/final_output.tsv)  


5. **Pull Requests**  
    - [Add Full Text search links for PMC in HTML Assembler](https://github.com/sorgerlab/indra/pull/1120)  
    - [Fix typographical error in Base html](https://github.com/indralab/gilda/pull/34)  
    
## Conclusion  

For the next week, we aim to complete the retrieval of information for Reactome Failed Searches.  
