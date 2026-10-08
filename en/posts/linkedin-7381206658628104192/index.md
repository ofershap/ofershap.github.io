# A vulnerability that changes the picture: it turns out a regular image can make an artificial intelligence model carry out instructions that the user never saw!

A vulnerability that changes the picture: it turns out a regular image can make an artificial intelligence model carry out instructions that the user never saw!

Researchers at Trail of Bits showed exactly that. They managed to hide textual commands inside images that look innocent to the eye, but after an automatic initial processing, these commands are revealed and picked up by the model. 

They tried it on systems like Google Gemini on the web, in the API, on the phone, on Vertex AI Studio and more. In most cases, the attack worked.
  
How it works:

Almost every AI system that receives an image downscales it before sending it to the model, to save resources.

In this process, done with algorithms like bicubic or bilinear, a side effect arises: if you design the pixels in the large image precisely, they will not be visible to the human eye, but will become clear after the downscaling. This way you can hide text that will be visible only in the version the model receives, not in the version the user sees.

This is basically a prompt injection attack disguised through an image!
  
But there are limitations - 
The attack requires precise control of the pixels.
You need to know in advance which algorithm the system uses.
And if the user sees a preview of what the model sees, they might discover the difference.
  
Still - it's a real attack that works against systems on the market, and it illustrates how differently models see the world from us.

For the full read:
https://lnkd.in/dUtyZpAE

Original: https://ofershap.github.io/posts/hidden-prompt-injection-through-image-downscaling/
Source: https://www.linkedin.com/posts/ofershap_%D7%A4%D7%99%D7%A8%D7%A6%D7%94-%D7%A9%D7%9E%D7%A9%D7%A0%D7%94-%D7%90%D7%AA-%D7%94%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%9E%D7%A1%D7%AA%D7%91%D7%A8-%D7%A9%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%A8%D7%92%D7%99%D7%9C%D7%94-activity-7381206658628104192-8tPE
Published: 2025-10-07T09:00:03.605000+03:00
