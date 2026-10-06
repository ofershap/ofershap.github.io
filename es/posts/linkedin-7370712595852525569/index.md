# ¿Usas Cursor? Aquí tienes un consejo de oro:

Traducción automática del post original, sin revisión de un traductor humano. Las afirmaciones históricas pueden haber cambiado.

¿Usas Cursor? Aquí tienes un consejo de oro:
Cuando ejecutamos comandos a través de la CLI, ocurren errores. A veces se lanzan en pantalla, a veces se esconden dentro de largas líneas de logs. 

Pero ¿qué pasa cuando trabajamos con Cursor u otros agentes inteligentes que ejecutan el código por nosotros?

Aquí se crea una brecha. El agente no "ve" lo que vemos nosotros. No puede escuchar los logs en tiempo real, ni seguir un tail, ni reacciona automáticamente al Watch Mode.

No es un bug: simplemente no forma parte de su forma de trabajar. Si hiciera una llamada así, se "quedaría atascado" esperando a que terminara.

Entonces, ¿cómo se asegura uno de que una ejecución automática no rompa algo?
Y no, la respuesta no es un MCP para la CLI 😄 

La solución que encontré es sencilla:
Configuré mi comando de npm para que escriba sus logs en un archivo (en mi caso dentro de una carpeta logs/ porque tengo más de un entorno en el proyecto) y la carpeta, por supuesto, está en gitignore. 
Usé el comando Tee (parecido al más conocido Tail) para escribir los logs.

Además, añadí una Cursor Rule que le pide revisar esos archivos al terminar de escribir código o al investigar fallos.

Así, al final de la ejecución se hace una comprobación proactiva de esos archivos para detectar anomalías, advertencias o errores que pasaron bajo el radar.

Sin complicaciones de MCP, sin herramientas externas, solo documentación en un archivo.
A veces, lo que un agente inteligente no ve, un solo archivo de log sabe contarlo.

Original: https://ofershap.github.io/posts/make-cursor-read-the-logs-it-cannot-watch/
Source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%A9%D7%AA%D7%9E%D7%A9%D7%99%D7%9D-%D7%91-cursor-%D7%94%D7%A0%D7%94-%D7%98%D7%99%D7%A4-%D7%96%D7%94%D7%91-%D7%A2%D7%91%D7%95%D7%A8%D7%9B%D7%9D-%D7%9B%D7%A9%D7%90%D7%A0%D7%97%D7%A0%D7%95-activity-7370712595852525569-wFyr
Published: 2025-09-08T10:00:24.069000+03:00
