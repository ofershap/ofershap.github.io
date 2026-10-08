# Un amigo me escribió y me dijo que había pasado Cursor a una suscripción Pro y después de un día ya había usado el 13 % de su suscripción. Así que me senté a escribir, para él y para ustedes, la siguiente guía:

Un amigo me escribió y me dijo que había pasado Cursor a una suscripción Pro y después de un día ya había usado el 13 % de su suscripción. Así que me senté a escribir, para él y para ustedes, la siguiente guía:

* Cómo ahorrar costes de desarrollo con IA (y ahorrar tokens) *

Aquí van algunos consejos que pueden ayudarles, desde mi experiencia, tanto para Cursor como para Claude Code:

Ya sea que lo paguen de su bolsillo o trabajen en una organización, la conciencia de los costes es lo primero que preocupa justo después de adoptar la tecnología.

Si usan Cursor, hace mucho del trabajo por sí mismo, pero aun así hay algunas cosas que pueden hacer ustedes: 
 
- Procuren abrir una conversación nueva al comienzo de cada tema nuevo. Si el contenido de la conversación existente es importante pero quieren reducir el tamaño del context (que afecta al coste de tokens), después de abrir una conversación nueva pueden pedirle que lea el historial de la conversación con @past y eligiendo la conversación.

- Los modelos caros son mejores pero, naturalmente, más caros. 
Una de las formas que uso para ahorrar costes es pedirle al modelo que ejecute agentes secundarios en un modelo más barato y los supervise. (Incluso tengo una rule así).
Spawn subagents and use composer-2 for the work it can do, and supervise it
A veces añado (en tareas grandes): then critic it and run subagent to fix
Y así obtengo alta velocidad (porque puede ejecutar en paralelo) y también una gestión económica y correcta de las tareas e incluso una corrección del código antes de que yo lo haya mirado siquiera

- Elegir modelos para la tarea es un músculo que hay que trabajar. Hay dos atajos de teclado que me gustan mucho y están uno junto al otro. Junto a la tecla shift derecha de su teclado están el signo de interrogación y la "ץ" final (tsadi final, una letra hebrea), así que en inglés cada una de ellas junto con cmd cambia una de las dos cosas: o el modelo, o el modo (plan, agent, ask)
Adopté para mí tres modelos y cambio entre ellos todo el tiempo: composer-2, sonnet 4.6, opus 4.6. Para muchas tareas uso Composer mientras no sean complicadas. Para tareas que requieren un razonamiento más complejo, o para Debug, paso a los más inteligentes. 
No uso Auto, no sé qué pasa ahí y me importa controlar el modelo que ejecuta mis tareas.

Algo que quizá valga la pena conocer: si trabajan en una organización y están en una cuenta enterprise donde hay "una sola manta" de la que todos tiran y hay que supervisar los costes, publiqué un proyecto de código abierto que permite seguir, monitorizar y recibir alertas sobre los gastos de la empresa: https://lnkd.in/djZRK5ZP

¿Y Claude Code? 
Lo primero, recomiendo instalar claude code statusline para que les muestre cuánto contexto se está usando ahora, y cuando vean que se infla pueden abrir una conversación nueva o llamar a /compact, al que también pueden añadir en una frase qué es importante conservar y qué se puede descartar (o simplemente dejar que decida él)

Además, también hay skills y librerías que pueden ayudar mucho:

Artik (en hebreo: ארטיק): https://lnkd.in/eXKPNNvV
Un proxy que ahorra tokens, funciona sobre todo con Claude Code (los de Cursor ya lo gestionan por su cuenta)

"El hombre prehistórico" (en hebreo: האדם הקדמות): https://lnkd.in/eqrJanMQ 
Reduce la longitud de las respuestas y del contenido a un lenguaje básico de "hombre de las cavernas" y ahorra la cantidad de texto (= tokens) que se acumula a lo largo de las conversaciones. A costa de las respuestas y las explicaciones.


En resumen,
hemos pasado la etapa de adopción de la tecnología y hemos subido de curso al trabajo óptimo y al intento de ahorrar costes. El nuevo campo de juego nos obliga a ser conscientes de los costes porque cada acción que hacemos cuesta dinero, y igual que al conducir un coche no se puede pisar a fondo el acelerador todo el día y quemar todo el depósito, aquí hay que gestionar una "economía de munición" y optimizar nuestro uso

¿Conocen otros métodos? ¡Me encantará saberlo!

Original: https://ofershap.github.io/posts/cutting-token-costs-in-cursor-and-claude-code/
Source: https://www.linkedin.com/posts/ofershap_%D7%97%D7%91%D7%A8-%D7%A4%D7%A0%D7%94-%D7%90%D7%9C%D7%99-%D7%95%D7%90%D7%9E%D7%A8-%D7%A9%D7%94%D7%95%D7%90-%D7%A9%D7%93%D7%A8%D7%92-%D7%90%D7%AA-%D7%A7%D7%A8%D7%A1%D7%95%D7%A8-%D7%9C%D7%9E%D7%A0%D7%95%D7%99-activity-7451525433248002048-KmoP
Published: 2026-04-19T10:01:45.934000+03:00
