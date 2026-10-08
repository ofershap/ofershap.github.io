# ¿Cómo trabajamos todos hoy? Es gracioso (o triste), pero básicamente es: ask agent → hope (pregunta al agente → espera)

¿Cómo trabajamos todos hoy? Es gracioso (o triste), pero básicamente es: ask agent → hope (pregunta al agente → espera)
No tiene por qué ser así. Uno de los desarrolladores más apreciados (autor de Total TypeScript) convirtió los prompts aleatorios en un proceso de ingeniería repetible, con puntos de control que el agente debe superar.

¿Qué significa esto? En lugar de dar un solo prompt enorme, se ejecuta un workflow definido según la etapa en la que estés:

Si tienes una idea vaga o una funcionalidad que aún no está madura: `/grill-me` y luego `/to-spec`
El agente cuestiona tus supuestos y luego escribe una spec de verdad.

Si ya hay una spec, pero la tarea es demasiado grande para construirla: `/to-tickets` o `/wayfinder`
Obtienes tickets pequeños y enfocados o un mapa de decisiones que vive dentro de GitHub o Linear.

Si ya estás listo para construir: `/implement` junto con `/tdd`
Avanzas una pieza cada vez, red → green → refactor, en lugar de reescribir media aplicación de golpe.

Si construiste pero algo se rompió: `/diagnosing-bugs`
Reproduces el problema → lo acotas → formulas una hipótesis → añades medición → lo corriges.

Antes del merge: `/code-review`
La revisión se hace en dos ejes en paralelo: cumplimiento de los estándares frente a ajuste a la spec.

De esta forma aprovechas la IA para que te preste mucha más atención, con comandos que conocen las limitaciones de los modelos y de los agentes, y además te mantiene dentro de los límites a lo largo del tiempo, sin saltarse pasos, sin olvidar ni cansarse.

Hace que el agente se comporte más como un desarrollador sénior que trabaja contigo y exige primero aclarar, desglosar, probar y hacer review, en lugar de como un desarrollador júnior que empieza a escribir código de inmediato.

Es decir, no te saltas las "partes aburridas" de alinear expectativas, definir el scope, probar y hacer review, que normalmente se pierden cuando se hace vibe coding.

Lo importante es recordar que no es magia... es un proceso empaquetado dentro de skills.
La parte más importante del proceso eres tú. Recordar los comandos, memorizarlos y usarlos en el momento adecuado.
Eso no lo puede hacer por ti ningún modelo ni ningún skill.

Si te saltas la configuración inicial con `/setup-matt-pocock-skills`, o simplemente no usas en la práctica los slash commands, es solo otra carpeta con archivos Markdown.

Por cierto, si ya tienes tus propios skills y comandos, vale la pena pedirle al chat que repase sus comandos y vea qué tienes ya y qué merece la pena adoptar.

Enlace al proyecto: https://lnkd.in/dqzMnXpN

Original: https://ofershap.github.io/posts/linkedin-7498244426281148416/
Source: https://www.linkedin.com/posts/ofershap_%D7%90%D7%99%D7%9A-%D7%9B%D7%95%D7%9C%D7%A0%D7%95-%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D-%D7%94%D7%99%D7%95%D7%9D-%D7%96%D7%94-%D7%9E%D7%A6%D7%97%D7%99%D7%A7-%D7%90%D7%95-%D7%A2%D7%A6%D7%95%D7%91-activity-7498244426281148416-XmRj
Published: 2026-08-26T08:06:21.870000+03:00
