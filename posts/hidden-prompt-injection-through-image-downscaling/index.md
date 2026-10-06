# Hidden prompt injection through image downscaling

October 7, 2025 · 1 min read

Originally posted on LinkedIn , October 7, 2025.

An ordinary image can make an AI model follow instructions the user never saw. Trail of Bits hid text commands inside images that looked harmless, but the commands became visible to the model after automatic image processing.

They tested the attack against systems including Google Gemini on the web, through the API, on mobile, and in Vertex AI Studio. It worked in most cases.

Almost every AI system that accepts images performs downscaling before sending them to the model to reduce resource use. Algorithms such as bicubic and bilinear can create a side effect: if the pixels in the original image are designed precisely, they remain invisible to the human eye but become clear after downscaling. The hidden text appears only in the version the model receives, not the version the user sees.

This is prompt injection disguised inside an image.

The attack has limits:

- It requires precise control over the pixels.

- The attacker needs to know which downscaling algorithm the system uses.

- If the user can preview what the model sees, they may notice the difference.

Even with those limits, this is a real attack that works against products already on the market. It shows how differently models can see the same image we do.

Read Trail of Bits’ full write-up .

Original source: https://www.linkedin.com/posts/ofershap_%D7%A4%D7%99%D7%A8%D7%A6%D7%94-%D7%A9%D7%9E%D7%A9%D7%A0%D7%94-%D7%90%D7%AA-%D7%94%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%9E%D7%A1%D7%AA%D7%91%D7%A8-%D7%A9%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%A8%D7%92%D7%99%D7%9C%D7%94-activity-7381206658628104192-8tPE
