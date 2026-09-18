---
title: "Open-source AI tool beats giant LLMs in literature reviews — and gets citations right"
source: "https://www.nature.com/articles/d41586-026-00347-9?utm_source=x&utm_medium=social&utm_campaign=nature&linkId=47294563"
author:
  - "[[Elizabeth Gibney]]"
published: 2026-02-04
created: 2026-02-05
description: "Researchers can deploy the cheap and transparent model on their own computer system."
tags:
  - "clippings"
---
![Shelves full of books curving away within the distance in a large library.](https://media.nature.com/lw767/magazine-assets/d41586-026-00347-9/d41586-026-00347-9_52015396.jpg?as=webp)

OpenScholar is an LLM that performs scientific literature reviews using a database of 45 million open-access articles.Credit: dpa via Alamy

Researchers have published the recipe for an artificial-intelligence model that reviews the scientific literature better than some major large language models (LLMs) are able to, and gets the citations correct as often as human experts do.

OpenScholar — which combines a language modelwith a database of 45 million open-access articles — links the information it sources directly back to the literature, to stop the system from [making up or ‘hallucinating’ citations](https://www.nature.com/articles/d41586-025-02853-8).

[Several commercial AI-based literature-review tools](https://www.nature.com/articles/d41586-024-03676-9) already exist that use similar techniques, but few have been released as open source, says Akari Asai, an AI researcher at Carnegie Mellon University in Pittsburgh, Pennsylvania, and a co-author of the work, published in *Nature* on 4 February <sup><a href="https://www.nature.com/articles/?utm_source=x&amp;utm_medium=social&amp;utm_campaign=nature&amp;linkId=47294563#ref-CR1">1</a></sup>. Being open source means that researchers can not only try OpenScholar for free in an [online demonstration](https://openscilm.allen.ai/), but also deploy it on their own machine and use the method in the paper to boost the literature-review skills of any LLM, says Asai.

In the 14 months since OpenScholar was first published in the arXiv repository <sup><a href="https://www.nature.com/articles/?utm_source=x&amp;utm_medium=social&amp;utm_campaign=nature&amp;linkId=47294563#ref-CR2">2</a></sup>, AI firms such as OpenAI have used similar methods to tack [‘deep research’ tools](https://www.nature.com/articles/d41586-025-00377-9) onto their commercial LLMs, which has greatly improved their accuracy. But as a small and efficient system, running OpenScholar costs a fraction of the price of using OpenAI’s GPT-5 with deep research, co-author Hannaneh Hajishirzi, a computer scientist at the University of Washington in Seattle, tells the *Nature* podcast.

However, the authors acknowledge that OpenScholar has limitations. For example, it doesn’t always retrieve the most representative or relevant papers for a query, and it is limited by the scope of its database.

But if researchers are able to access the tool for free, “it can become one of the most popular apps for scientific searches,” says Mushtaq Bilal, a researcher at Silvi, a Copenhagen-based firm that has its own AI-based literature-review tool.

## Outperforming humans?

LLMs can write fluently, but they often [struggle with citations.](https://www.nature.com/articles/d41586-025-00068-5) This is because they learn by building links between words in their training data, which include sources outside science, and then generate text on the basis of probable associations that are not always correct or up to date. This is a feature of LLMs, not a bug, and it is proving to be a problem when people use LLMs in research. For example, at least 51 papers accepted to the high-profile machine learning NeurIPS conference in December 2025, contained non-existent or inaccurate citations, according to [an analysis using the GPTZero tool](https://gptzero.me/news/neurips/).

OpenScholar is a way to force an LLM to answer queries using a specific data store, says Hajishirzi. When a user asks a question, a retrieval system finds related scientific articles within the repository, then ranks them by relevance and generates a response that is based only on the most useful. The LLM — trained on examples of questions and answers — then refines the answer to improve it. “We designed an efficient pipeline where the model generates an answer once, but then keeps improving if needed,” says Asai.

Although the data store used in the paper contains scientific articles up to October 2024, Asai says that the demo version of OpenScholar can tap into [the academic search engine Semantic Scholar](https://www.semanticscholar.org/), from the Allen Institute for Artificial Intelligence in Seattle, to access current papers. And because responses are built around real, specific papers, the system very rarely fabricates citations. It can, however, still cite a paper that doesn’t support a claim very well, in the same way that humans can, says Asai.

To test OpenScholar, the team compared its ability to answer realistic queries with that of other AI tools and with answers written by experienced, PhD-level humans, in computer science, physics, neuroscience and biomedicine. They found that experts preferred the models’ responses over human-written ones in most cases. OpenScholar also outperformed GPT-4o, as well as rival tools such as PaperQA2, from FutureHouse in San Francisco, California, on machine-judged evaluations of citation and factual accuracy.

A limitation of the tool is that it cannot ensure that it accesses only scientifically rigorous articles, says Bilal. It also cannot access paywalled papers, which means it is much less useful in disciplines, such as engineering or social sciences, in which open-access preprints are not the norm, he says. “Lack of access to copyrighted, licensed, or paywalled research is one of the biggest bottlenecks in improving these AI tools,” he says.

In the future, the team would like to develop a more flexible system that allows users to tap into papers they hold subscriptions for and that they have downloaded locally, says Asai.

*doi: https://doi.org/10.1038/d41586-026-00347-9*

## References

[^1]: Asai, A. *et al.**Nature* https://doi.org/10.1038/s41586-025-10072-4 (2026).

[^2]: Asai, A. *et al.* Preprint at arXiv [https://doi.org/10.48550/arXiv.2411.14199](https://doi.org/10.48550/arXiv.2411.14199) (2024).