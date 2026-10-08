# Una vulnerabilidad que cambia el panorama: resulta que una imagen normal puede hacer que un modelo de inteligencia artificial ejecute instrucciones que el usuario nunca vio.

Una vulnerabilidad que cambia el panorama: resulta que una imagen normal puede hacer que un modelo de inteligencia artificial ejecute instrucciones que el usuario nunca vio.

Investigadores de Trail of Bits demostraron justamente eso. Lograron ocultar comandos de texto dentro de imágenes que parecen inocentes a simple vista, pero tras un procesamiento inicial automático, esos comandos se revelan y el modelo los capta. 

Lo probaron en sistemas como Google Gemini en la web, en la API, en el teléfono, en Vertex AI Studio y otros. En la mayoría de los casos, el ataque funcionó.
  
Cómo funciona:

Casi todo sistema de IA que recibe una imagen la reduce de tamaño (downscaling) antes de enviarla al modelo, para ahorrar recursos.

En este proceso, que se hace con algoritmos como bicúbico o bilineal, surge un efecto secundario: si se diseñan con precisión los píxeles de la imagen grande, no serán visibles para el ojo humano, pero se vuelven claros tras la reducción. Así se puede ocultar texto que solo se verá en la versión que recibe el modelo, no en la que ve el usuario.

¡Esto es básicamente un ataque de prompt injection camuflado a través de una imagen!
  
Pero hay limitaciones: 
el ataque requiere un control preciso de los píxeles.
Hay que saber de antemano qué algoritmo usa el sistema.
Y si el usuario ve una vista previa de lo que ve el modelo, puede descubrir la diferencia.
  
Aun así, es un ataque real que funciona contra sistemas que están en el mercado, e ilustra hasta qué punto los modelos ven el mundo de una manera totalmente distinta a la nuestra.

Para leer el artículo completo:
https://lnkd.in/dUtyZpAE

Original: https://ofershap.github.io/posts/hidden-prompt-injection-through-image-downscaling/
Source: https://www.linkedin.com/posts/ofershap_%D7%A4%D7%99%D7%A8%D7%A6%D7%94-%D7%A9%D7%9E%D7%A9%D7%A0%D7%94-%D7%90%D7%AA-%D7%94%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%9E%D7%A1%D7%AA%D7%91%D7%A8-%D7%A9%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%A8%D7%92%D7%99%D7%9C%D7%94-activity-7381206658628104192-8tPE
Published: 2025-10-07T09:00:03.605000+03:00
