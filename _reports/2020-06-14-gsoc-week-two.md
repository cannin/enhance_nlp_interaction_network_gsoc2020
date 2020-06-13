---
layout: post
title:  "Week Two | Developing the solution"
tags: [gsoc, weekly report, coding period ]
author: Priti Shaw
---

This week our focus was to convert the java(GenericBatchNew) code to python using pyjinius for extracting the MESH terms.  

## Work Progress  

1. **Build the python script for extracting MESH terms**    
    Status: **In Progress**  
    It involves three steps   
    1. Generate a Ticket Granting Ticket(TGT)  
    2. Generate a Service Ticket(ST)  
    3. Send file for processing  
    But I could not find any documentation or reference for the #3.  

    **Documentation:**  
    [Generate TGT and ST](https://documentation.uts.nlm.nih.gov/rest/home.html)   
    [Send file for processing](https://ii.nlm.nih.gov/cgi-bin/II/UTS_Required/API_batchValidationII.pl)  

2. **MTI Batch Process using Pyjnius**  
    Status: **Complete**  
    JAR files included by Pyjnius are present in lib folder. I have used the 1.1.4 version of Pyjnius.  
    **Repository:** [MTI Batch Process](https://github.com/PritiShaw/Analyze-MESH/tree/python)  

3. **Analysis on time taken per abstract**        
    An analysis table represents the average time taken, time taken per abstract and Estimated Abstract processed in 24 hrs based on number of abstracts in an input file.  
    **Gist:** [Batch Processor](https://gist.github.com/PritiShaw/f2bf83ca89c86fc5d94b0eea344cdc08)  

4. **Analyse the effect of PMID in input**    
    I ran the Abstracts with and without Unique Identifier(UI) for a comparative study.  
    **Gist**: [Compare MESH terms with and without UI](https://gist.github.com/PritiShaw/259273b452d93a5f9608f8bea24b843f)  
    
## Conclusion  
This week, I got stuck in converting the Java code to Python but my mentor, Augustin helped me and I was able to complete that. I am thankful to him for giving time and valuable advice.
