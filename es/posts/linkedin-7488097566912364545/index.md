# ¿Cómo se combate esta situación en la que de repente hay tanto código que hay que revisar y hacerle Review?

¿Cómo se combate esta situación en la que de repente hay tanto código que hay que revisar y hacerle Review?
El cuello de botella ha pasado de escribir el código a revisarlo, y gran parte del trabajo del equipo de desarrollo consiste en juzgar lo que se desarrolló y cómo se desarrolló.

Una de las formas que encontré que nos facilita las cosas a mí y al equipo es añadir instrucciones al agente que escribe la PR Description (ya sea un command en Cursor o a través de GitStream de LinearB) siguiendo una metodología de 4 pasos:

1. Qué problema veníamos a resolver 
2. Qué cambió y dónde (qué archivos)
3. Cómo funciona en la práctica (el flujo)
4. Cuáles son los riesgos

Una vez que se detalla el PR de forma tan granular ya en la etapa de Description, el camino para entender el código se vuelve mucho más corto y fácil: ya sé qué espero ver en el propio código, y a veces incluso detecto aspectos de arquitectura o riesgos que el propio agente planteó antes de que yo mirara una sola línea de código

Esto nos funcionó tan bien que, cuando se lo compartí a los demás líderes de equipo, decidieron adoptarlo en todo R&D para cada PR que se abre 😇

Original: https://ofershap.github.io/posts/a-four-step-pr-description-for-faster-code-reviews/
Source: https://www.linkedin.com/posts/ofershap_%D7%90%D7%99%D7%9A-%D7%A0%D7%9C%D7%97%D7%9E%D7%99%D7%9D-%D7%91%D7%9E%D7%A6%D7%91-%D7%94%D7%96%D7%94-%D7%A9%D7%99%D7%A9-%D7%A4%D7%AA%D7%90%D7%95%D7%9D-%D7%9B%D7%9C-%D7%9B%D7%9A-%D7%94%D7%A8%D7%91%D7%94-activity-7488097566912364545-K7N5
Published: 2026-07-29T08:06:22.077000+03:00
