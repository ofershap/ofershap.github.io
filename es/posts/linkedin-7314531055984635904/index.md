# El MCP del que tanto se oye hablar últimamente: ¿qué significa siquiera?

El MCP del que tanto se oye hablar últimamente: ¿qué significa siquiera?
Para explicarlo como es debido, piensa en cómo empezó internet:
Hubo que inventar un lenguaje común para que un ordenador pudiera hablar con un servidor remoto. Esa fue la invención del HTTP. Hoy nos resulta transparente: usamos un navegador, visitamos sitios y olvidamos que se basan en una infraestructura mundial acordada, un protocolo, para transferir comunicación e información que permite que esos sitios aparezcan en nuestro ordenador.

Lo mismo está pasando ahora con la IA.
Solo que ahora quien necesita saber "hablar" no eres tú, es la inteligencia artificial.
Y no es sencillo: GPT no sabe qué es "enviar un correo" o "reservar una cita", necesita que alguien le explique qué se puede hacer, en qué lenguaje, en qué formato y qué pasará cuando pulse.

Y eso es lo que hace MCP (y, ampliado, model context protocol): 
es un protocolo acordado que poco a poco están adoptando todas las empresas y que se convierte en la forma en que enseñamos a la IA a hablar con sistemas, servicios, botones, menús y todo.

¿Y cómo se hace? Pues no es nada sencillo: requiere traducir nuestra API a un lenguaje que una máquina entienda. Todo servicio de la red que quiera ser accesible a la inteligencia artificial necesita añadirle ese acceso (un servidor mcp).

Pasamos de una situación en la que la gente de producto escribe documentación para desarrolladores a una situación en la que hoy los desarrolladores escriben documentación para la inteligencia artificial.

Parece surrealista, pero es la etapa en la que estamos ahora. Se está mapeando para la IA todos los servicios que puede usar y las formas en que puede acceder a los distintos sistemas, para permitirle hacer acciones por nosotros "con un solo comando".

Así como necesitamos protocolos para navegar por internet y ver sitios, y así surgieron conceptos como HTTP que hoy nos parecen transparentes, ahora, por increíble que parezca, hubo que inventar un protocolo nuevo que permita a la inteligencia artificial dirigirse por sí misma a los servicios digitales.

Alguien tiene que sentarse de verdad a mapear la comunicación tecnológica (la "manual", la que los desarrolladores saben leer) que hemos usado hasta hoy, como APIs, botones, formularios, etc., y convertirla en un lenguaje que la inteligencia artificial sepa usar.

Es un arte de convertir comandos técnicos en lenguaje de comandos de máquina, y requiere:
- Explicar qué se puede hacer siquiera con el sistema
- Qué acciones están expuestas en la API o en la UI
- Cómo acceder a ellas (¡y cómo hacerlo de forma segura!)
Y redactar en inglés claro qué debe hacer la IA para usarlas

Por ejemplo: 
si hay un botón que envía un correo, hay que escribirle a la inteligencia artificial:
"Para enviar un correo, usa la acción send_email. Indica destinatario, asunto y contenido. El formato debe ser JSON de tal y tal manera."

No es exactamente programación, y no es documentación normal: es un lenguaje nuevo que media entre el ordenador que piensa y el ordenador que ejecuta.
Y eso es MCP.

Esta es la etapa en la que estamos ahora, y quien no lo entienda a tiempo se quedará fuera del juego.

Original: https://ofershap.github.io/posts/mcp-is-how-ai-talks-to-software/
Source: https://www.linkedin.com/posts/ofershap_%D7%94-mcp-%D7%A9%D7%A9%D7%95%D7%9E%D7%A2%D7%99%D7%9D-%D7%A2%D7%9C%D7%99%D7%95-%D7%94%D7%A8%D7%91%D7%94-%D7%9C%D7%90%D7%97%D7%A8%D7%95%D7%A0%D7%94-%D7%9E%D7%94-%D7%96%D7%94-%D7%91%D7%9B%D7%9C%D7%9C-activity-7314531055984635904-OwyK
Published: 2025-04-06T09:15:01.162000+03:00
