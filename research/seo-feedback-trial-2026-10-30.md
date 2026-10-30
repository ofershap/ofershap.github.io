# Evidence-led SEO/GEO trial, 30 October–5 November 2026

Review date:6November. Owner:Ofer Shapira. Existing blog remains on GitHub Pages. This extends the existing routine; it is not a new content calendar or a promise of rankings.

## Source and scope
Ofer shared Tim Scheuer's LinkedIn post on30October and asked to try incorporating a similar process into the blog routine.
Source: https://www.linkedin.com/posts/tim-scheuer-91b005237_we-put-our-seogeo-fully-on-autopilot-9-days-share-7520945462573584384-o_bY/
The post describes a daily evidence loop, one change, a change log, comparison content and indexing. Its17LLM signups,31+Google signups and911clicks/8271impressions are the author's self-report.30/28day windows overlap the nine-day automation experiment, so they do not prove its effect.

## Decision debate
Eight viewpoints: reader, author, SEO analyst, accessibility reviewer, copy editor, cost controller, experiment skeptic and maintenance reviewer.
1. SEO analyst wants daily content; author rejects generic filler and title changes. Reader wants existing answers improved first. Choose existing-page improvements, not an automatic article quota.
2. Analyst wants paid competitor data; cost controller vetoes new paid tools. Skeptic says public SERPs cannot replace exact keyword volume. Choose available Search Console query/page data and free public sources, explicitly mark missing metrics.
3. Analyst wants every indexing button pressed; maintenance reviewer cites unresolved sitemap fetch failures. Choose diagnose first, no blind repeat submissions. IndexNow only for actual eligible changes.
4. Reader wants useful comparisons; editor rejects invented product use, numbers or hands-on screenshots. Choose dated primary sources and documented experience; draft only when evidence is missing.
5. Analyst wants four daily changes; skeptic says attribution becomes impossible. Choose one coherent change/day, other slots measure or prepare. A blocked day can ship nothing.
6. Accessibility reviewer prioritizes confirmed contrast defect; SEO analyst says it will not itself establish topic visibility. Choose that low-risk first fix with an accessibility endpoint, do not call it ranking growth. Search/AI endpoints remain separate.

## Decision tree and consequences
- Input:current query/page data / scanner recommendations / vendor promises. Choose current evidence; scanners can nominate candidates only. If unavailable, record missing evidence instead of inventing it.
- Candidate:existing content / technical correction / new landing page. Choose within existing permissions; new pages excluded. If titles would change, reject; use in-page answer sections when justified.
- Prioritization:effort-only / promised traffic / evidence×reader value×confidence divided by effort+risk. Choose last. A hard restriction overrides score.
- Shipping:several unrelated changes / one coherent correction / no change. Choose one correction; no change if no verified defect.
- Measurement:immediate rankings / technical endpoint now plus7/28day search windows / scanner score. Choose technical now and search later. Search Console delay and sparse traffic limit causal inference.
- Content:one article/day / sourced existing-page improvement / speculative competitor comparison. Choose sourced improvements. Content pipeline is separate and does not inherit new publishing authority.
- Indexing:daily retries / request only relevant supported changes / unsupported bulk automation. Choose supported routes and preserve the open sitemap diagnosis.
- Attribution:claim success on any positive mention / fixed prompt plus source and denominator / omit measurement. Choose fixed prompts and record model/search mode/date/sources; repeated exposure and third-party citations are confounders.
- End:expand automatically / review6Nov / abandon after one day. Choose review; continue only what adds useful evidence.
- Failure:hide sparse data / disclose no measurement / fabricate a lift. Choose disclose; a reversible accessibility fix can stand even without ranking change.

## Plain decisions
1. We use one evidence-ranked existing-page change per day because four simultaneous changes obscure what helped. Why: other existing slots gather evidence, verify or prepare.
2. We do not add daily articles or buyer landing pages because the trial is an extension of an existing blog, not a content factory. Why: title/new-page restrictions remain.
3. We use free evidence because paid competitor tooling is not approved. Why: missing keyword volumes stay unknown.
4. We check factual claims and dated sources because comparison content can become stale. Why: no invented product experience, pricing or screenshots.
5. We record hypothesis, baseline, change, verification, rollback and next check because activity counts are not outcome evidence.
6. We separate technical readiness, indexing, query impressions/clicks, AI name/topic presence and referrals because they measure different things.
7. We preserve sitemap diagnosis because valid live XML does not prove Google processed it. Why: repeated submissions have not resolved the recorded failure.
8. We review on6November because seven days can validate execution and early signals, not prove sustainable rankings.

## Operating card
At the first useful existing daily slot, inspect the last card and current evidence. Rank up to three candidates by evidence strength, reader value and confidence (each0–3), subtract risk and effort (each0–3). Record rationale, not just sum. Select at most one coherent change/day. An absence of a safe grounded change is a valid outcome. Later slots validate the deployed result and gather outcomes; do not manufacture changes to fill the quota.
Each card records: date, exact page/source, baseline timestamp, hypothesis, alternatives and score, effect sought, permission/restriction check, changed files/commit, technical test and visual verification where needed, rollback, outcome status,7/28day followup. Existing content/distribution/LinkedIn rules are unchanged.

## Day1:confirmed contrast defect
- Source:29OctGreadme finding, independently reproduced30Oct07:06IST on live homepage. Computed muted nav/post metadata color rgb(118,118,118), body rgb(253,253,251). WCAG contrast approximately4.45:1, below4.5 for small text.
- Candidates:contrast correction score9(evidence3+reader3+confidence3−risk0−effort0); speculative new comparison rejected by scope; repeated sitemap submission rejected by prior failed attempts.
- Hypothesis:darkening shared muted text to #707070 makes small metadata/navigation meet4.5:1 without changing layout, titles, content or new URLs.
- Endpoint:computed contrast+live CSS+actual pixels, not a ranking claim.
- Prepared change, NOT shipped:shared style.css muted #767676→#707070 only (4.862:1). Existing darker ordinary text unaffected. Full-suite gate failed on pre-existing archive WebMCP omission, engagement count1168vs1165, and generated-output idempotence. Test-generated drift restored; do not deploy the CSS until the gate is resolved.
- Rollback:revert this isolated stylesheet replacement. No content migration.
- Search baseline:latest historical29Oct read:Google28day1click/99impressions/4AIimpressions; sitemap still fetch-failed/blank last read/0discovered despite live valid1236URLs. Bing224indexed,13AIcitations over3months/1last7days. One web-enabled unseeded recommendation cited Ofer throughDEV, not stable ranking. These remain dated historical baseline, not a fresh30Oct dashboard read or causally attributable result.
- Next:existing30Oct09:30–10GSC diagnosis; daily technical followups in existing slots. Review6Nov; use comparable7/28day windows when available. Do not claim ranking lift from this contrast correction.
