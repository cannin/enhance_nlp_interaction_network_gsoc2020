---
layout: post
title:  "Week Four | First Evaluation"
tags: [gsoc, weekly report, coding period, first evaluation]
author: Priti Shaw
---

Hard to believe that the first phase of the journey has come to an end. I hope I have performed up to the mark.    
First Evaluation marks the end of one-third of the program.  

## Work Progress  

1. **Implement the text fragment search**  
    Status: **Complete**  
    
    I worked on making full text search using the new [Scroll to Text feature](https://chromestatus.com/feature/4733392803332096) of Chromium. I had to improvise on cases where the sentence has special terms or characters. To solve this I implemented the logic using a prefix and a suffix of our target instead of a complete sentence. The first six words are considered as start terms, the last two words are considered as end terms and the words with XREF are skipped. 
The will automatically search for the sentence, scroll to it, and highlight, without using any plugin.  

    ![Sample Output](https://user-images.githubusercontent.com/34039705/85835606-f58de400-b7b2-11ea-80df-04c8381c62af.png)  
    **Browser Supported:** Chrome v80+for both desktop and android, Chromium-based Edge, Opera.  
    **Issue:** [New Chrome plugin for links to text fragments](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/5)  
    **Pull Request:** [Add Full Text search links for PMC in HTML Assembler](https://github.com/sorgerlab/indra/pull/1120)  

## Conclusion  

Any project is incomplete without great guidance. I am thankful to my mentor, [Augustin Luna](https://github.com/cannin) for keeping faith in me and constantly supporting me.<br> 
I am grateful to [Rohit Chattopadhyay](https://github.com/rohitchattopadhyay) for helping and guiding me for making a pull request. Looking forward to the reviews from my mentors.    
