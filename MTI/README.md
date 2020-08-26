MTI WEB API Consistency Check
---

### Supporting libraries
The workflow requires MTI WebApi libraries to perform Batch MeSH extraction from abstracts. The supporting files are available at [ziy/skr-webapi](https://github.com/ziy/skr-webapi) and [NLM Official Site](https://ii.nlm.nih.gov/Web_API/index.shtml).

### Secrets
`MTI_USERNAME` and `MTI_PASSWORD` are to be set in repository settings under **Secrets** tab with MTI credentials.  
To get MTI Credentials register at https://utslogin.nlm.nih.gov/cas/login 

### Workflow
1. The [sample abstract file](./inputs/sample_abstract.txt) is uploaded to MTI for Batch MeSH processing and the output is written to file, `./results/expected_output.txt`
2. The output file is matched with expected output file. If they match then the Workflow succeds else fails.

### Workflow Result
**Success** indicates that there are no changes in MTI, hence no action is required.  
**Failure** indicates that either the credentials have failed or MTI batch processing has failed.

