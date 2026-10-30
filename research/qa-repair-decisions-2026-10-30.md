# Bounded build gate repair

Reader/author demand unchanged prose; maintainer wants deterministic builds; QA rejects deleting assertions; privacy reviewer rejects adding tracking; SEO reviewer rejects fabricated freshness; cost reviewer keeps tools free; skeptic requires original failing examples.

Debate: normalizing all generated pages would create hundreds of diffs and fake dates. Ignoring test failures would hide real omissions. Changing only counts would hide broken widgets. Chosen: preserve existing module placement; stable dates; whitespace-stable identity update; derive inventory from source but retain per-page assertions; recognize the existing semantically equivalent script. Beacon import must not mutate pages merely by importing a builder. Builders may add their own beacon while generating a page, not globally at import.

Decision tree: broad rebuild / bypass gate / bounded deterministic code -> bounded. Existing widget: move it / preserve location -> preserve. Lastmod: clock / source or prior date -> source/prior. Tests:constant count / source-derived expected set plus per-pagechecks -> latter. Script assertion:duplicate script / weaken feature check / semantic attribute check -> semantic check. Generated HTML:commit all / restore unrelated drift -> restore. Ship:unreviewedCSS / Mainpixelreview -> Mainreview.

1. We preserve source/prose/title hashes because gate repair is not content authorship.
2. We keep existing engagement placement because regeneration must not move media.
3. We remove global import-time beacon sweeps because tests must not silently add analytics sitewide.
4. We retain source-derived dates instead of today's date on unchanged pages because rebuild is not an update.
5. We fix whitespace accumulation in identity builder because identical input should have identical bytes.
6. We replace stale inventory1165 with expected paths derived from source files and verify every actual page because new archives legitimately increase counts.
7. We recognize the existing serialized WebMCP script semantically because the byte-literal assertion was a false alarm. No script or post HTML is added or changed.
8. We isolate rebuild tests in temporary copies where necessary and require repeated builds stable, preserving live-file assertions because tests must not rewrite the working site.

Correction from source inspection:the archive script was present as `<script defer="" src="/webmcp.js">`; this was a byte-literal false alarm, not a missing feature. The guard now recognizes semantic attributes in either order. No script or post HTML changed.
All12existing suites pass in disposable copied repository after bounded code/test fixes. Test snapshots isolate normalizer first-pass differences; a second build must be byte-stable. Original authored body hashes, per-page schema/WebMCP/metadata/source checks, source-derived archive inventory and engagement privacy assertions stay enforced. No production content or sitemap normalization included in patch. Shared contrast candidate remains awaiting Main pixel review.
