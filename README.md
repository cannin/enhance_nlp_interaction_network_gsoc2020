Enhance NLP Interaction Network
---

This repository contains the code used to get information required for analysis.

## Python Notebooks 
1. [Reactome Failed Query Analysis](Reactome_Failed_Query_Analysis.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://gesis.mybinder.org/binder/v2/gh/cannin/enhance_nlp_interaction_network_gsoc2020/767dab746f7d4518c007ffbdac84f1f19ae26a98)   
    The purpose of this notebook is to process failed Reactome query terms to get information of the Pubmed articles where the term is found
2.  [MTI MeSH Extraction Example](MTI_MeSH_Extraction_Example.ipynb)  [![Binder](https://mybinder.org/badge_logo.svg)](https://gesis.mybinder.org/binder/v2/gh/cannin/enhance_nlp_interaction_network_gsoc2020/767dab746f7d4518c007ffbdac84f1f19ae26a98)  
    This is an example demonstrating how MeSH terms can be extracted from arbitraty text can be using [MTI WebAPI](https://ii.nlm.nih.gov/Interactive/MTI/mti.shtml)
    
### Using papermill
[Papermill](https://papermill.readthedocs.io/) is used to paramete the notebook **Reactome Failed Query Analysis** , to use this, make a yaml file as following:  
```
mti_email_id: email@address.com
mti_username: Username
mti_password: password
```
If you do not have account, register at https://utslogin.nlm.nih.gov/cas/login

**To install Papermill**  
`pip install papermill`  

**To Run the program**  
`papermill Reactome_Failed_Query_Analysis.ipynb output.ipynb -f path/to/parameters.yaml`
