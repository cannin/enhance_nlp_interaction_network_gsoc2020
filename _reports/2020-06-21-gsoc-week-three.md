---
layout: post
title:  "Week Three | My code goes to server"
tags: [gsoc, weekly report, coding period ]
author: Priti Shaw
---

This week Ben have integrate the MTI Batch Process using Pyjnius with the INDRA DB workflow. They will test this at a larger scale. Hopefully it will run without any major issues.

## Work Progress

1. **Make Indra HTML Assembler Work With Chrome Plugin**  
    Status: **Complete**

    Since PMCID is missing from the text_refs, I fetched PMCID from PMID using function [id_lookup](https://indra.readthedocs.io/en/latest/modules/literature/index.html#indra.literature.id_lookup).  
    **Commits:** [Add plugin support](https://github.com/PritiShaw/indra/tree/add-plugin-support)  
    **Output:** [Output.html](https://gist.github.com/PritiShaw/3eb9aa6d1823813080a9d59cb94b3cd0#file-output-html)  
    **Issue:** [Make Indra HTML Assembler Work With Chrome Plugin](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/5)  

2. **Implement the text fragment search**  
    Status: **In Progress**  

    `Link to text fragment chrome extension` might remove the need for a custom plugin and make things more standardized and it will work without the [`Highlight PMC Chrome Extension`](https://github.com/PritiShaw/highlight-pmc-chrome-extension). Need to improvise on cases where the sentence has special terms or characters.  

    **Documentation:** [Text Fragments](https://web.dev/text-fragments/)  
    **Output:** [output_text_fragment.html](https://gist.github.com/PritiShaw/3eb9aa6d1823813080a9d59cb94b3cd0#file-output_text_fragment-html)  
    **Issue:** [New Chrome plugin for links to text fragments](https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020/issues/5#issuecomment-645989453)  

## Conclusion

Overall this has been quite a successful week.<br>
Next week, we have our first GSoC evaluation, and I hope I have performed up to the mark the program demands.
