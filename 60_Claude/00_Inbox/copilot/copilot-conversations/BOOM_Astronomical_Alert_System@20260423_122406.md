---
epoch: 1776965046730
modelKey: "gpt-5.2|github-copilot"
topic: "BOOM Astronomical Alert System"



tags:
  - copilot-conversation
---

**user**: I get that BOOM ingests astronomical alert streams and moves them through several stages before exposing results to users and downstream systems. But i fail to understand what exactly is this alert system for, what are we alerting?
[Timestamp: 2026/04/23 12:24:06]

**ai**: In BOOM, an “alert” is the unit of data coming from time-domain sky surveys (e.g., ZTF, LSST) that flags that **something in the sky changed or looks like a new transient event**—i.e., a candidate “interesting object/event” worth follow-up. BOOM’s job is to act as an **alert broker**: it **consumes** those survey alert streams, **enriches** each alert with cross-matches and derived quantities, **filters** them using user-defined criteria, **stores** the resulting enriched/filtered alert data, and **exposes** it via an API so users or downstream systems can query and act on the candidates. [^1]

So “what are we alerting?”: we’re alerting on **survey-detected transient/variable candidates** (the incoming “astronomical alert streams”), then narrowing them down to the subset that matches what users care about (via enrichment + filtering) and making those results accessible for follow-up and analysis. [^1]

#### Sources
[^1]: [[BOOM]]
[Timestamp: 2026/04/23 12:24:18]