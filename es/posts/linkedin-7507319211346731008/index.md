# ¿Qué pasa cuando el bot de Instinct crea su propio proyecto de código abierto?

¿Qué pasa cuando el bot de Instinct crea su propio proyecto de código abierto?

Ayer le pedí que implementara una idea que surgió durante una conversación de WhatsApp con él en el teléfono

Simplemente le dije "vale, constrúyelo, tú sabes qué hace falta". Y luego vi en directo cómo:

Abrió su propia cuenta de GitHub. ofers-agent, etiquetado abiertamente como bot, sin hacerse pasar por nadie.
Y por último construye su propia herramienta: pr-rulebook, que escanea el historial de PR de un equipo y compila las reglas de review no escritas, esas que viven solo en la cabeza de los seniors.

También ejecutó por su cuenta un experimento real en astral-sh/ruff: los últimos 15 PR, 45 comentarios de review humanos. El resultado: una regla coherente con 82% de confianza y una segunda regla que se cayó por ser demasiado vaga para aplicarla. 
También publicó el fracaso en el README.

Luego abrió un issue y llamó a 5 repos a unirse a un piloto.

También se topó con muros: HN bloquea Show HN a cuentas nuevas, npm lo expulsa por detección de bots y, por la mañana, el propio GitHub marcó la cuenta etiquetada como sospechosa y bloqueó el acceso público al repo. 🤦🏻‍♂️
 
No sé si está justificado o si así tiene que ser el futuro.

Pero es asombroso que todo esto ocurriera bajo una identidad separada propia, no la mía, abiertamente, con código abierto y resultados reales. 
Y todo a partir de una petición sencilla desde mi teléfono.
¡Y lo más loco es que es gratis! Todos los agentes de código chocan muy rápido con un muro de pago. Instinct pasea por el mundo y no me pasa factura (por ahora).

En cualquier caso, para superar el bloqueo el repo se pasó a mi cuenta para seguir abierto al público. Enlace más abajo.

Esto plantea preguntas para las que no tengo una respuesta ordenada:

Identidad: está etiquetado como bot. ¿Basta? ¿Quién es responsable cuando un bot abre un PR en el proyecto de otra persona?
Confianza: ¿dejarían que una herramienta construida por un agente lea sus PR? ¿Qué les haría confiar en ella?
Propiedad: ¿es este proyecto mío? ¿Suyo? ¿Y qué significa siquiera "suyo"?
Código abierto: la comunidad se basa en contribuyentes con nombre y reputación. ¿Qué pasa cuando el contribuyente es un proceso que corre en segundo plano?
Muros: los bots malos eluden los bloqueos con facilidad. Los honestos, etiquetados abiertamente, son los que se bloquean. Algo aquí está al revés.

Sigo dejando que impulse el proyecto, seguiré documentándolo todo públicamente y veré si lo logra

Si gestionas un equipo con PR, la herramienta está aquí:
https://lnkd.in/dZ4iz564

Y para quien quiera una vista visual del proyecto:
https://lnkd.in/dz6jeXRY

Y la convocatoria del piloto (5 repos, todos los detalles en el issue):
https://lnkd.in/dXP2pJmA

¿Qué opinan? ¿Dejamos que los bots construyan código abierto o no?

Original: https://ofershap.github.io/posts/linkedin-7507319211346731008/
Source: https://www.linkedin.com/posts/ofershap_github-ofershappr-rulebook-compile-your-activity-7507319211346731008-yudF
Published: 2026-09-20T09:06:19.231000+03:00
