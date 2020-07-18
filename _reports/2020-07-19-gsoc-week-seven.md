---  
layout: post
title:  "Week Seven | Retrieving Reactome Failed Query details"
tags: [gsoc, weekly report, coding period ]
author: Priti Shaw
---  

Continuing to last week's work, this week we continued to run the code to retrieve the information for the Reactom [failed queries](https://raw.githubusercontent.com/cannin/reach-query/master/queries.csv) with some additional columns.        

## Work Progress  

1. **Fix make_model Documentation**  

    Status: **Complete**  
    Fixed small indentation error in the make_model documentation and made a Pull Request.  

    **Issue:**  [Fix make_model Documentation](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/11)   
    **Pull Request:** [Fix documentation of HTML Assembler](https://github.com/sorgerlab/indra/pull/1135)  

2. **Clean Up Code Repo Provide Pipfiles for Code**   

    Status: **In Progress**   
    The aim is to provide proper Pipfiles for the existing code, maintain and clean up the code repository.   

    **Issue:** [Provide Pipfiles for code](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/8)     

3. **Add PMID_COUNT column**  
    
    Status: **In Progress**  
    The objective was to add additional column *PMID_COUNT* with the result count from PubMed to the previously created table. The total number of failed queries is greater than 10 million so I am again running the rest of queries on Google Colaboratory after adding the additional column.   

    **Issue:** [Retrieve Information for Reactome Failed Searches](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/7)  
    **Output:** [Output.tsv](https://github.com/PritiShaw/Reactome-Failed-Queries-Processing/blob/master/output.tsv)   

## Conclusion  

For the next week, we aim to add documentation, tests, docker file to the Reactome Failed Search Code.   
