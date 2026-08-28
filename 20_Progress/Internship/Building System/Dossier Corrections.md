
# Dossier Corrections — audit from the 2026-08-28 deadline sweep

Report-only. No dossiers were moved, merged, or edited in this pass — every finding below is cited to a specific filename and a specific piece of evidence (a quote, a URL match, or a direct observation from reading the dossier body), per this repo's own "cite the real data" convention. Findings are scoped to what I personally read in full this session; I did not re-derive findings for dossiers I only saw as a filename in a listing.

## 1. Likely duplicate dossiers (same underlying posting, filed twice)

Confirmed via explicit "duplicate" / "same URL" annotations recorded during the sweep's no-deadline check:

- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Network Automation Engineer Intern - Global Physical Network Infrastructure - ByteDance]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Network Automation Engineer Intern, Global Physical Network Infra - ByteDance]] — near-identical titles (comma vs. dash variant), sweep noted "rolling basis, no fixed deadline (duplicate of above)".
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Applied Machine Learning Production Engineer Intern - AML Production Engineer - ByteDance]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Applied Machine Learning Production Engineer Intern - ByteDance]] — flagged "(duplicate)".
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Data Lake Infrastructure & Data Analytics Research Engineer Intern - Applied Machine Learning Ark - ByteDance]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Data Lake Infrastructure and Data Analytics Research Engineer Intern - Applied Machine Learning Ark - ByteDance]] — titles differ only by "&" vs. "and"; flagged "(duplicate)".
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/GPUAI Application System Software Engineer Intern - ByteDance]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/GPUAI Application System Software Engineer Intern - System Technologies and Engineering - ByteDance]] — flagged "(duplicate)".
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate) - AbbVie]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Business Technology Solutions Intern - Data & Software Engineering - Undergraduate - AbbVie]] — flagged "same posting/URL as above" — confirmed same URL in frontmatter comparison.
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Technology Intern - Humana]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer Intern, CenterWell and Humana Military - Humana]] — flagged "same posting/URL as above".
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Cybersecurity Intern - American Express (2)]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Cybersecurity Intern - American Express]] — identical title except a "(2)" suffix; near-certain duplicate ingestion of the same posting via two source feeds.
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Intern - Montenson]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Artificial Intelligence Intern - Montenson]] — flagged "duplicate of AI Intern - Montenson".
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Data Science Intern - College to Corporate IT - Vanguard]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Data Science Intern - Information Technology - Vanguard]] — both individually flagged "Workday, duplicate posting" in the sweep notes.

**Needs a human look, not yet resolved — the sweep's own note contradicted itself:**
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Machine Learning Engineer Intern - AML-Engine-Orchestration - ByteDance]] ↔ [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Machine Learning Engineer Intern - ByteDance]] — the sweep called the second one "duplicate role, different req" in the same phrase, which is internally inconsistent. Someone should actually diff the two `url` frontmatter fields directly.

**Suspicious by title pattern only — I did not verify URLs, flagging for a future check rather than asserting duplicate status:**
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer Intern - Global Payment Infra and SRE - ByteDance]] (AI & ML) vs. [[10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Software Engineer Intern - Global Payment - ByteDance]] (Fullstack) — same company, overlapping "Global Payment" theme, filed in two different priority buckets. Could be genuinely different reqs (one SRE-specific) or the same role double-classified.
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Machine Learning InternCo-op - Machine Learning - Artificial Intelligence - AMD]] vs. [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Machine Learning InternCo-op - Multiple Teams - AMD]] — both dossier bodies read "This posting is for an existing vacancy," a generic template AMD appears to reuse across many team-specific listings on its career site. The captured text alone can't distinguish two real reqs from the same generic page ingested twice.

## 2. Priority-bucket misclassification

**Systemic pattern, not a single dossier** — quant-trading-firm software/hardware roles are split inconsistently between `1 - AI & ML` and `3 - CyS & Finance` (the bucket whose own folder name is specifically for quant/trading firms). Directly observed:
- Optiver: [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer Intern - Optiver]] and [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Quantitative Intern (Summer 2027) - Optiver]] sit in AI & ML, while [[10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Software Engineer Intern (Summer 2027 - Austin) - Optiver]] and [[10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/FPGA Engineer Intern (Summer 2027 - Austin) - Optiver]] sit in CyS & Finance.
- IMC: [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer Intern - IMC]] (AI & ML) vs. [[10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Hardware Engineer Intern - IMC]] (CyS & Finance).
- Chicago Trading Company: [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineer Intern - Chicago Trading Company]] (AI & ML) vs. [[10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Quant Trading Intern - Chicago Trading Company]] (CyS & Finance).

Same company, same class of role, filed in two different buckets depending on which keyword tripped first during ingestion (an "AI/ML/Data" match vs. a "quant/trading" match on the same posting family). This is the same failure class the 2026-08-23 audit already partially addressed. Worth a rule change so any posting from a recognized quant-trading-firm allowlist lands in one consistent bucket regardless of which keyword matched.

**Single-dossier finding:**
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Business Systems Analyst Intern - W.W. Grainger]] — a Business Systems Analyst internship with no AI/ML or software-engineering content in the body; likely matched into this bucket on a loose keyword rather than real content fit.

## 3. Postings a human would waste time screening (beyond the Rippling dead link already logged in the prior sweep report)

None of these are confirmed 404s/redirects — they're dossiers with effectively no usable content or an already-lapsed deadline, which a human would only discover after opening them:

**Empty or non-content captures:**
- [[10_Areas/Career/Internships/List/Dossiers/Other/Software Engineering Intern, Summer 2027 - Google]] — source is a bare Telegram post link (`t.me/getjobss/7795`); body literally reads "No posting content fetched."
- [[10_Areas/Career/Internships/List/Dossiers/Other/Engineer Intern - Spring 2027 - TMEIC Corporation Americas]] — captured body is a raw job-application form scaffold (country-code phone dropdown, boilerplate legal-consent text); no actual job description was ever captured.
- [[10_Areas/Career/Internships/List/Dossiers/Other/Software Engineer Intern - Summer 2027 - Belvedere Trading]] — captured body is ~700 bytes: just a title/location/department breadcrumb, no real description.
- [[10_Areas/Career/Internships/List/Dossiers/Other/Software Systems Validation Intern (Spring 2027) - Zipline]] — body reads "No posting content fetched."
- Six further Zipline dossiers only ever captured Zipline's generic `/open-roles` directory listing (dozens of unrelated job titles) instead of the specific posting — the `gh_jid` URL parameter that should filter to one job isn't honored by a non-JS fetch: [[10_Areas/Career/Internships/List/Dossiers/Other/Enterprise Systems Software Engineer Intern (Summer 2027) - Zipline]], [[10_Areas/Career/Internships/List/Dossiers/Other/Enterprise Systems Software Engineer Intern - Spring 2027 - Zipline]], [[10_Areas/Career/Internships/List/Dossiers/Other/Long Range Platform Embedded Firmware Intern (Summer 2027) - Zipline]], [[10_Areas/Career/Internships/List/Dossiers/Other/Software Systems Validation Intern (Summer 2027) - Zipline]], [[10_Areas/Career/Internships/List/Dossiers/Other/System Test Automation Intern (Spring 2027) - Zipline]], [[10_Areas/Career/Internships/List/Dossiers/Other/System Test Automation Intern (Summer 2027) - Zipline]].

**Deadline already lapsed as of 2026-08-28** (now correctly bucketed under "Already Over" in `Tracker/Deadline Tracker.md`, but flagged here too since the dossier itself carries no visible staleness marker):
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Quantic – Quantitative Developer Intern (Summer 2027) - Walleye Capital Internships]] — "The deadline to apply for this opportunity is Friday, July 31."
- [[10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Investment Data Science Intern - Walleye Capital]] and [[10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Risk Technology Analyst Intern - Walleye Capital]] — same July 31 deadline text.
- [[10_Areas/Career/Internships/List/Dossiers/Other/Intern, Software Engineering - Moog]] — "End Date: July 29, 2026."
- [[10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Software Engineering Intern - Google]] and [[10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Software Engineering Intern, MS, Summer 2027 - Google]] — Google's own boilerplate: application window closed July 24, 2026.
- [[10_Areas/Career/Internships/List/Dossiers/Other/Software Engineering Intern (Summer 2027) - RTX]] — "End Date: August 21, 2026" (7 days ago).

None of these were re-fetched live this pass to confirm whether the posting itself has actually been pulled down vs. still silently accepting late applications — worth a human live-check to tell the two apart before writing them off entirely.

## 4. PhD-only / clearance-track roles worth a self-check

I don't have the human's exact citizenship/degree-level profile loaded in this session, so these are flagged for a human eligibility check rather than asserted as definite mismatches:

- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Quantic - PhD Quantitative Researcher Intern (Summer 2027) - Walleye Capital Internships]] — body: "Are pursuing a PhD degree in computer science, engineering, statistics, operations research, mathematics, or a related field."
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Quantitative Research Intern, PhD (Summer 2027) - Optiver]] — PhD requirement is in the title itself.
- [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software DeveloperData Scientist Intern - Summer 2027 - CACI]] — "Interns will be required to obtain TS/SCI clearance as a condition of continued employment" — a multi-year background-investigation process that typically requires US citizenship; worth flagging for anyone not planning to pursue a clearance-track career.


## 5. Possible company-name data-quality issue (surfaced during Task 1's landing-page re-check)

- The 5 "Montenson" dossiers ([[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Intern - Montenson]], [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Artificial Intelligence Intern - Montenson]], [[10_Areas/Career/Internships/List/Dossiers/Other/Data Analytics Intern - Insights - Montenson]], [[10_Areas/Career/Internships/List/Dossiers/Other/Sustainability Engineer Intern - Montenson]], [[10_Areas/Career/Internships/List/Dossiers/Other/System Administrator Intern - Montenson]]) — a company-landing-page search for "Montenson" found no such company; the only plausible real match is **Mortenson**, a real construction company with an actual careers/college page (`mortenson.com/careers/college`). Worth a human check on whether `company: Montenson` in these 5 dossiers' frontmatter is a typo of Mortenson, or whether Montenson is a real, smaller company that just doesn't show up in a search — I did not verify which against the dossiers' own stored `url` fields in this pass.


## 6. Follow-ups on items 5 and "Acds" (2026-08-29 re-check)

**Montenson — CONFIRMED, not just suspected.** Read [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Intern - Montenson]] directly: the posting body itself reads "At Mortenson, we're grounded in..." and "Mortenson's i4 department seeks an AI intern..." and the page-load footer literally says "Page AI Intern - Mortenson External Career Site Careers loaded." The `company:` frontmatter field ("Montenson") is a one-letter-dropped typo of the real employer, **Mortenson** (the construction/EPC company already identified in Task 1's landing-page check). This affects all 5 Montenson-labeled dossiers: the two above plus [[10_Areas/Career/Internships/List/Dossiers/Other/Data Analytics Intern - Insights - Montenson]], [[10_Areas/Career/Internships/List/Dossiers/Other/Sustainability Engineer Intern - Montenson]], [[10_Areas/Career/Internships/List/Dossiers/Other/System Administrator Intern - Montenson]]. Not fixed in this pass (report-only), but no longer just a guess — it's a confirmed `company` field typo.

**"Acds" — NOT a data-quality bug, confirmed via direct read.** [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Operations Intern - Naukr AI - Acds]] and [[10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Operations Intern-Caddell Reynolds - Acds]] both read: "The Arkansas Center for Data Sciences dba Apprenticely will not discriminate against apprenticeship applicants..." — ACDS = **Arkansas Center for Data Sciences**, doing business as **Apprenticely**, a real Arkansas work-based-learning placement organization. It places candidates with host employers — Naukr.AI and Caddell Reynolds respectively — which are correctly named in each dossier's *title* even though the `company:` frontmatter field names the placement intermediary rather than the host employer. Worth a convention decision (should `company` be the actual host employer instead of the staffing intermediary?), but this is not a bug in the sense Montenson is.

**New finding while checking Acds's own site:** `https://www.acds.co/careers` (linked from inside both Acds dossier bodies) currently fails to load over HTTPS with a "certificate has expired" error. Not the same as a dead/redirected posting, but a real access problem for anyone who clicks that link from the dossier — the parent org page `apprenticely.org` loads fine and states no deadline.
