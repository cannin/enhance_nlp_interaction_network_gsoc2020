Enhance NLP Interaction Network
---

This repository contains the code used to get information required for analysis of Reactome failed queries.

## Requirements
For extraction of MeSH terms, an UMLS license/account is required. If you do not have account, register at https://utslogin.nlm.nih.gov/cas/login and set the credentials in the parameter cell.

## Notebooks
1. [Reactome_PMID_Metadata_Extraction](./Reactome_PMID_Metadata_Extraction.ipynb) , generates `reactome_pmid_metadata.tsv` , which contains metadata of PMIDs present in Reactome.
2. [Reactome_Failed_Query_Analysis](./Reactome_Failed_Query_Analysis.ipynb) , generates `failed_query_analysis_output.tsv`, which contains details regarding the failed query terms.
3. [Reactome_Analysis](./Reactome_Analysis.Rmd) , performs the analysis using above generated files

### Supporting files
MTI WebAPI is used to get MeSH terms using their [batch processing](https://ii.nlm.nih.gov/Interactive/MTI/mti.shtml). Their code is in Java hence [pyjnius](https://pyjnius.readthedocs.io/en/stable/) to run the JAR files. The files are present in [/lib](./lib).  
These JAR files can be found in [ziy/skr-webapi](https://github.com/ziy/skr-webapi/) repository.

## Steps to follow
Please note: Steps 1 and 2 can be performed parallely as they are independent.  

1. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cannin/enhance_nlp_interaction_network_gsoc2020/master?filepath=Reactome_PMID_Metadata_Extraction.ipynb) Run **Reactome_PMID_Metadata_Extraction.ipynb** after setting the initial parameters, this will generate `reactome_pmid_metadata.tsv` file, which is required in step 3
2. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cannin/enhance_nlp_interaction_network_gsoc2020/master?filepath=Reactome_Failed_Query_Analysis.ipynb) Run **Reactome_Failed_Query_Analysis.ipynb** after setting the initial parameters, this will generate `failed_query_analysis_output.tsv` file, which is required in step 3
3. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cannin/enhance_nlp_interaction_network_gsoc2020/master?urlpath=rstudio) Follow instructions in **Reactome_Analysis.Rmd** to run it in RStudio and generate the analysis.

## How to run locally using [jupyter/repo2docker]()

1. **Installation**
`pip install jupyter-repo2docker`
2. **Build and Start Notebooks**
`jupyter-repo2docker https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020`  
Note: Docker needs to be running in local machine
3. An URL with token will be printed in terminal, you can access Jupyter Notebooks and RStudio using that link as follows:  
    *Jupyter Notebooks* : Open the link directly, all Notebooks will be visible  at `/notebooks`
    *RStudio* : Go to `/rstudio` to open RStudio
4. Follow sequence of execution as mentioned above

## How to use papermill
[Papermill](https://papermill.readthedocs.io/) is used to paramete the notebook **Reactome Failed Query Analysis** , to use this, make a yaml file as following:  

### Parameters of `Reactome_Failed_Query_Analysis.ipynb`
```
mti_email_id = "example@example.com"
mti_username = "username"
mti_password = "password"

pmid_threshold = 20
indra_db_rest_url = "SET_INDRA_DB_URL"

reactome_failed_terms_link = "https://gist.githubusercontent.com/PritiShaw/03ce10747835390ec8a755fed9ea813d/raw/cc72cb5479f09b574e03ed22c8d4e3147e09aa0c/Reactome.csv"
final_output_file_path = "failed_query_analysis_output.tsv"
```

### Parameters of `Reactome_PMID_Metadata_Extraction.ipynb`
```
mti_email_id = "example@example.com"
mti_username = "username"
mti_password = "password"

reactome_pmid_url = "https://reactome.org/download/current/ReactionPMIDS.txt"
pmid_chunk_limit = 0 
output_path = "reactome_pmid_metadata.tsv"
```


**To install Papermill**  
`pip install papermill`  

**To Run the program**  

`papermill Reactome_Failed_Query_Analysis.ipynb failed_query_analysis.ipynb -f path/to/parameters.yaml`  

`papermill Reactome_PMID_Metadata_Extraction.ipynb pmid_metadata_extraction.ipynb -f path/to/parameters.yaml`