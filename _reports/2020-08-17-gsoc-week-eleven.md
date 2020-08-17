---  
layout: post
title:  "Week Eleven | Setting up Notebooks for deployment"
tags: [gsoc, weekly report, coding period, evaluation ]
author: Priti Shaw
---
This week, the Python and R notebooks were refactored and stored in a single repo for easy use. The repository has been made into docker container using [jupyterhub/repo2docker](repo2docker.readthedocs.io) thus enable it to be run in any infrastructure.  
The notebooks have been parameterized using [Papermill](https://pypi.org/project/papermill/), to make it easy for the user to set parameters and run the notebooks automatically from a configuration file.  
Detailed instruction has been added to README file for users' reference
### Pull Request
[Add Rmd file along with documentation to run the same #21
](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/pull/21)

### Conclusion
As we enter the last week of Google Summer of Code 2020, I am able to recapitulate all the new things I learned in these 3 months.  
In the following weeks, my target will be to create unit tests and integrate other tools to maintain the code quality so that it is easy for future contributors.
