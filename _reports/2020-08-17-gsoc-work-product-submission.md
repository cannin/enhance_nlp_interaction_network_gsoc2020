---
layout: post
title:  "GSoC 2020 | Work Product Submission"
tags: [gsoc, 2020, coding period , third phase, final evaluation, final report ]
author: Priti Shaw
---

## Enhance NLP Interaction Network

### Table of Contents
1. [Project Details](#Project-Details)
2. [Work Done](#Work-Done)  
    a. [Reactome Query Analysis](#Reactome-Query-Analysis)  
    b. [INDRA](#INDRA)  
    c. [IHOP REACH](#IHOP-REACH)
3. [Work Left](#Work-Left)
4. [Conclusion](#Conclusion)

### Project Details
[**GSoC Project URL**](https://summerofcode.withgoogle.com/projects/#5223231348277248) , [**Work Repository**](https://cannin.github.io/enhance_nlp_interaction_network_gsoc2020/)  
**Objective:** The aim of the project is to make it easy for curators to get meaningful information from the failed search queries in Reactome.  

**Student**: [Priti Shaw](https://linkedin.com/in/pritishaw01)  
**Mentor**: [Augstin Luna](https://github.com/cannin)  
**Organisation**: [National Resource for Network Biology (NRNB)](https://summerofcode.withgoogle.com/organizations/5848353922875392/)

### Work Done
The project involved contribution to multiple open source projects as listed below
### Reactome Query Analysis
Performing analysis on failed Reactome search terms to make it easy for curators to curate.
#### Tasks
1. [Commit R Code for Reactome Analysis](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/18)
2. [Python Code Cleanup with Pylint](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/20)
3. [Documentation for Google Colab Notebooks](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/11)
4. [Add Documentation/Tests/Dockerfile to Reactome Failed Search Code](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/12)
5. [Add Count of INDRA Statements for Individual Terms](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/10)
6. [Add Citations from OpenCitations to Reactome Search](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/9)
7. [Clean Up Code Repo; Provide Pipfiles for Code](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/8)
8. [Retrieve Information for Reactome Failed Searches](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/7)
9. [Extract Data for Reactome Articles (MeSH Terms, Journal)](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/6)
10. [Cron and GitHub Actions](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/22)

#### Pull Requests
1. [Add Binder Support for the Notebooks](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/pull/16)
2. [Add Rmd file along with documentation to run the same](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/pull/21)
3. [Add MTI Web API Consistency check Github Action](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/pull/23)

### INDRA
It is an automated model assembly system interfacing with NLP systems and databases. Our project uses this to extract information regarding the medical papers.
#### Tasks
1. [Make Indra HTML Assembler Work With Chrome Plugin](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/5)
2. [Colab Notebook Showing Use of MTI with Arbitrary Text](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/15)
3. [Fix make_model Documentation](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/11)
4. [Extracting MeSH Terms for Articles](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/1)
5. [MeSH to INDRA](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/19)
#### Pull Requests
1. [Improve documentation of IndraNet assembler](https://github.com/sorgerlab/indra/pull/1096)
2. [Fix documentation of HTML Assembler](https://github.com/sorgerlab/indra/pull/1135)
3. [Add Full Text search links for PMC in HTML Assembler](https://github.com/sorgerlab/indra/pull/1120)

**Repository :** Developed script for extracting MeSH terms from medical papers for INDRA, the code is available at [PritiShaw/Analyze-MESH](https://github.com/PritiShaw/Analyze-MESH/tree/python)

### IHOP-REACH
Continuing previous year's project, my task was to develop a Chrome Extension to highlight Text Segments in PMC journals. 
#### Tasks
1. [Make Chrome Plugin into Separate GitHub Repo](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/3)  
2. [Test Chrome Extension in Microsoft Edge](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/4)   

**Repository :** [PritiShaw/highlight-pmc-chrome-extension](https://github.com/PritiShaw/highlight-pmc-chrome-extension)

### Work Left
The code has not yet been used by the end user, we are expecting it to be used by them after GSoC ends hence I will stay involved with the project after the program ends.

### Conclusion
Any project cannot address its objectives without proper guidance. I would like to thank [Augustin Luna](https://github.com/cannin) for the constant support he has given throught the program. I would also like to thank [Benjamin Gyori](https://github.com/bgyori), [Guanming Wu](https://github.com/guanmingwu) for their help from time to time.  
It was a great learning experience to be able to interact with such great researchers. I hope that my work will help them.
