Enhance NLP Interaction Network
---

This repository contains the code used to get information required for analysis.

## Python Notebooks
1. [Reactome Failed Query Analysis](Reactome_Failed_Query_Analysis.ipynb)
2. [MTI MeSH Extraction Example](MTI_MeSH_Extraction_Example.ipynb)

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