Title: How do you check that a multi-agent process is worth its cost?

**Short answer:** Build a small sample with known answers, run a single agent and a multi-agent process on it, and compare three metrics: how many of the right answers were found, how many errors were added, and what the cost was. Decide by the metrics, not by an impression from a demo.

### Build a sample with known answers

Pick 10 to 30 items from the real material. For some items the right answer is known in advance: for example a document that contains a specific commitment, or a clean document with no finding at all. Write the answers down before any run.

Example: when testing 200 documents against a new policy, pick 20 documents, manually mark which commitments appear in them, and keep the list as an answer key.

### Run two setups on the same sample

One run with a single agent handling all items. A second run with a multi-agent process, for example reader agents, checker agents, and a report-joining step. Same items, same instruction, same model version.

### Measure three numbers

Accuracy: how many of the findings from the key were found in each run. Noise: how many wrong findings were added. Cost: tokens, run time, and how many repeat passes were needed.

In the Anthropic demo on Latent Space, a stock-list scan with a review stage cost much more than a single agent and also found more details in the example. That's the illustration of the tradeoff between cost and coverage. Your sample is what tells you whether the tradeoff pays off on your task.

### Decide by the result

If the multi-agent process found more correct findings at a cost you're willing to pay, expand gradually. If a single agent reached the same result, stay with it. For a small set of independent parts, even a simple script can be the answer.

### What to keep from the test

Keep the answer key, both reports, and the comparison table. When someone later asks why you chose one architecture over another, you have numbers from your task, not a quote from somebody else's demo.