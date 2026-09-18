---
title: "X"
source: "https://x.com/witcheer/article/2033646544315150824"
author:
  - "[[witcheer ☯︎@witcheer·16 Mar]]"
published: 2026-03-16
created: 2026-03-21
description:
tags:
  - "clippings"
---
## Klavye kısayollarını görüntülemek için soru işaretine basKlavye kısayollarını görüntüle

[![Resim](https://pbs.twimg.com/media/HDhEbpsWUAAf3Vt?format=jpg&name=large)](https://x.com/witcheer/article/2033646544315150824/media/2033450473596801024)

==Stop Writing Better Prompts. Start Building Better Context.==[49 B](https://x.com/witcheer/status/2033646544315150824/analytics)

==I spent weeks refining prompts. rewriting them, adding examples, tweaking tone instructions, structuring with XML tags. the outputs got marginally better. then I changed what Claude had access to== before ==I asked anything. loaded my working documents, wrote custom instructions that define how I want it to think, gave it tool access to my actual systems. the output quality jumped.==

that shift has a name: context engineering.

I picked it up going through

[Anthropic's own courses,](https://anthropic.skilljar.com/)

the prompt engineering tutorial, the AI Fluency certification, the API deep-dive. the biggest lesson across all of them was that prompting is only one layer of a much bigger system. here's the full picture.

## What Anthropic Actually Teaches

Anthropic runs a free course catalog on

[Skilljar](https://anthropic.skilljar.com/)

that most people either don't know about or haven't finished. it's worth the time.

the prompt engineering course covers 9 chapters, basic prompt structure, clarity and directness, role assignment, separating data from instructions, output formatting, chain-of-thought reasoning, few-shot examples, hallucination prevention, and complex industry workflows.

the five highest-impact techniques:

1/ use XML tags to separate instructions from data:

markdown

```markdown
<instructions>
analyse this protocol
</instructions> 
<data>
{{paste documentation here}}
</data>
```

2/ ask for evidence before conclusions:

markdown

```markdown
before giving your recommendation, 
list the three strongest arguments for and against 
in <pros> and <cons> tags.
```

3/ assign specific roles:

markdown

```markdown
you are a DeFi analyst specialising in CDP protocols. 
you have deep knowledge of liquidation mechanisms, stability pools, 
and collateral risk.
```

4/ request step-by-step reasoning:

markdown

```markdown
think through this step by step. 
first identify the problem, then list possible causes, 
then recommend a fix.
```

5/ show examples instead of writing long instructions:

instead of explaining your desired format, paste 2-3 examples of outputs you liked and say "match this format."

that's solid. but it's chapter 1 of a bigger story.

the

[AI Fluency course](https://anthropic.skilljar.com/ai-fluency-framework-foundations)

introduces something more fundamental: the 4D framework, developed by professors Rick Dakan and Joseph Feller. four competencies for working with AI effectively:

→ Delegation \- deciding whether, when, and how to engage AI. not everything should be delegated.

→ Description \- effectively describing your goals. this is prompt engineering.

→ Discernment \- accurately assessing AI output. catching errors, verifying claims, knowing when the model is wrong.

→ Diligence \- taking responsibility for what you do with AI output.

most people focus entirely on Description, writing better prompts. they skip Delegation (using AI for tasks it's bad at), ignore Discernment (blindly trusting output), and forget Diligence (not verifying before publishing or sending).

but even the 4D framework is missing a layer. it tells you how to interact with AI. it doesn't address what the AI knows when the interaction starts.

that's where context engineering comes in.

## ==What Context Engineering Actually Is==

Anthropic published

[a guide](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

on this. their definition: "what configuration of context is most likely to generate the desired behaviour?"

here's the distinction:

- ==prompt engineering = how you ask the question (Description in the 4D framework)==
- ==context engineering = everything the model sees when it generates a response: system prompts, loaded documents, tool access, conversation history, memory==

prompt engineering is a subset of context engineering. you can write a perfect prompt, but if the model doesn't have the right background information, you get a polished generic answer.

concrete example. same prompt, two different contexts:

prompt: " write a cold DM to a stablecoin protocol about a partnership with Yari."

blank chat output:

> =="hi, I'd love to explore potential synergies between our protocols. we think there's an interesting opportunity for collaboration. would you be open to a quick call?"==

inside a Claude Project loaded with Yari's docs, competitive positioning, and collateral roadmap:

> =="your token has a reliable price feed and issuer redemption path but \[redacted\]. Yari's \[redacted\] can \[redacted\]. happy to walk through the mechanics on a quick call."==

same prompt. completely different output. the variable was what the model knew.

## ==The Four Layers Of Context==

Anthropic's guide breaks context into four components. here's each one with how I actually use it.

system prompts - behaviour architecture, not preferences.

this is the most misunderstood layer. most people write system prompts like preferences: "be helpful and concise." that's too vague to shape behaviour.

here's a bad system prompt:

> =="you are a helpful writing assistant. be concise and professional."==

here's what my content project instructions actually look like:

and my research project uses a completely different set:

markdown

```markdown
always cite sources with dates. structure analysis as: 
problem → mechanism → why it matters for CDPs. 

flag when data is older than 30 days. 
compare against competitor protocols by default. 

output as comparative briefs, not summaries.
```

these are constraints that shape every output before I type a word. the prompt engineering course teaches XML tags and role assignment, system prompts are where those techniques live permanently instead of being re-typed every conversation.

knowledge base - persistent reference material.

my Claude Project for content has ~15 files loaded: voice guidelines, topic hierarchy, format templates, and the last 8 published articles.

without this layer, every conversation starts from zero. you upload your docs, explain what they are, get the output, then do the whole thing again next time. with it, Claude reasons against the same persistent knowledge base across dozens of conversations. the quality compounds.

Anthropic's courses teach few-shot examples, showing the model what good output looks like. a persistent knowledge base is few-shot at scale. my past 8 articles are the examples. Claude doesn't need me to describe my writing style, it can see it.

tools - what the model can do, not just what it knows.

this is the layer people skip entirely. MCP (Model Context Protocol) lets Claude connect to your filesystem, your GitHub repos, your database, your browser. I wrote a

[full setup guide](https://x.com/witcheer/status/2030320298919424492?s=20)

on this.

tool access is a context layer because it changes what information the model can pull in mid-conversation. without MCP, I paste files into Claude manually. with MCP, Claude reads them directly from my filesystem. the model's effective context expands from "what I remembered to paste in" to "everything in my project directory."

Anthropic's prompt engineering course appendix covers tool use and search & retrieval. that's where prompting ends and context engineering begins.

conversation history & memory - the compounding layer.

Anthropic's context engineering guide introduces three techniques for long-horizon tasks:

→ compaction \- summarising conversation history when approaching context limits. preserves architectural decisions and unresolved issues, discards redundant output.

→ structured note-taking \- the model writes persistent notes outside the context window, retrieved later. Claude playing Pokémon demonstrated this, maintaining precise tallies across thousands of game steps.

→ sub-agent architectures \- specialised agents handle focused tasks with clean context windows, returning condensed summaries (1,000-2,000 tokens).

in practice, this is why I start new conversations within the same Claude Project instead of running one infinite chat. the project context stays intact. the conversation context stays fresh.

## ==Context Rot - Why More Isn't Better==

more context doesn't always mean better output.

Anthropic calls this "context rot", the model's ability to accurately recall information from context decreases as token count increases. the technical reason: transformer models create n² pairwise relationships between tokens. longer contexts stretch the model's attention capacity thin. there's not a sharp cliff, it's a gradient. but it's real.

don't dump everything into one project and hope for the best.

I learned this the hard way. my first Claude Project was called "content" and had everything. Claude couldn't prioritise any of it. the outputs were unfocused, pulling from irrelevant documents, mixing contexts.

splitting into purpose-built projects with specific, curated documents was the single biggest quality jump. 15 targeted files in a content project beats 50 random files every time.

the Anthropic guide frames it perfectly: " find the smallest set of high-signal tokens that maximise the likelihood of your desired outcome."

## ==What Most People Get Wrong==

after months of building this workflow, here are the patterns I see people repeat:

1/ treating projects like folders.

they create projects named "work" and "personal" and dump files in, expecting organisational benefits. projects aren't about organisation, but about specialisation. each one should have a specific purpose, specific documents, and specific behavioural instructions.

2/ writing vague system prompts.

compare these two:

❌ " be helpful and professional "

✅ " always structure analysis as: problem → mechanism → why it matters. cite sources with dates. flag when data is older than 30 days. compare against competitor protocols by default."

the first tells the model nothing. the second shapes every output. specificity is behaviour architecture. vagueness is abdication.

3/ overloading context.

more documents ≠ better output. if the model can't prioritise what matters, it averages everything. curate ruthlessly.

4/ ignoring tool access.

if you're still copying and pasting files into Claude, you're manually doing what MCP automates. tool access is a context layer that most people don't think about.

5/ skipping Discernment.

the 4D framework gets this right, output verification is a core competency, not an optional step. I've caught Claude misreading protocol mechanics in competitive briefs. every output gets fact-checked against primary sources before I use it.

6/ never updating loaded documents.

context goes stale. if your protocol evolves, your roadmap changes, your competitive landscape shifts, and your Claude Project still has the old docs loaded, you're reasoning against outdated information. maintenance is part of the system.

## ==Starter Templates - Steal These==

here are system prompt templates you can adapt for your own projects. these are simplified versions of what I actually use.

content production:

markdown

```markdown
you write in my voice. 
first person, direct, analytical. lead with specific data, not generalities. 

show process including failures. cite every claim with a source URL and date. 

never use: 'game-changing', 'revolutionary', 'leverage', 'synergy', 'at the end of the day'. 

match the tone and structure of the example articles in the knowledge base.
```

competitive intelligence:

markdown

```markdown
structure all analysis as comparative briefs. 

format: protocol name → mechanism overview → strengths → weaknesses → strategic implications for us. 

always include data sources. 

flag when data is from a single source or older than 30 days. 

default to comparing against [list your competitors].
```

partnership outreach:

markdown

```markdown
generate partnership briefs for each protocol I name. 

format: what they do → where the integration overlap is → what specific value our product brings to their users → suggested outreach angle. 

use the documentation in the knowledge base as the source of truth for our product mechanics. 

be specific - no generic 'synergy' language."
```

research synthesis:

markdown

```markdown
summarise each source I provide. 

then cross-reference across all sources to identify: 
consensus points, contradictions, gaps in coverage, and novel insights. 

output as a structured brief, not a wall of text. 

flag where a claim appears in only one source.
```

code review / technical docs:

markdown

```markdown
you are a senior developer reviewing code for clarity, correctness, and maintainability. 

flag potential bugs, suggest improvements, and explain your reasoning. 

when writing documentation, structure as: 
what it does → how it works → how to use it → known limitations.
```

the knowledge base files matter just as much as the instructions. load your past work, your style guides, your reference docs. the system prompt tells Claude how to think. the knowledge base tells it what to think about.

## ==Conclusion==

Anthropic's courses teach you the pieces. the prompt engineering tutorial gives you Description, how to ask. the 4D framework gives you Delegation, Discernment, and Diligence, how to decide, evaluate, and take responsibility. both are worth your time. both are free.

but the biggest unlock is in assembling the pieces into a persistent context layer that makes every interaction better than the last. system prompts that define behaviour. documents that provide knowledge. tools that expand access. history that compounds.

that's context engineering. and the gap between someone who writes good prompts and someone who builds good context is the gap between using AI casually and getting real work done with it.

start with one project. pick your most common workflow. load the documents you find yourself re-sharing constantly. write custom instructions that define exactly how you want the model to operate.

20 minutes of setup. permanent compound returns.

the courses give you the foundation. context engineering is what you build on top of it.

Join my channel for more miscellaneous tools and researches on AI and DeFi:

[https://t.me/witcheergrimoire](https://t.me/witcheergrimoire)

sources:

[Anthropic's context engineering guide](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

·

[Anthropic Skilljar course catalog](https://anthropic.skilljar.com/)

·

[prompt engineering interactive tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)

·

[4D AI Fluency Framework](https://aifluencyframework.org/)

(Dakan & Feller) ·

[Anthropic prompt engineering documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

Kendi Makaleni yayınlamak mı istiyorsun?

[Premium kademesine yükselt](https://x.com/i/premium_sign_up)

- 	[witcheer ☯︎](https://x.com/witcheer)
		[@witcheer](https://x.com/witcheer)
	Head of Growth
	[@YariFinance](https://x.com/YariFinance)
	| Founder
	[@Broad\_Land](https://x.com/Broad_Land)
	| Daily AI × DeFi insights → [t.me/witcheergrimoi](https://t.co/IjETldXGaT)