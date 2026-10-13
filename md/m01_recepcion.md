# Recepción

Hay obras que llegan con su nombre y aun así son desconocidas. Este instrumento no les exige revelar una tesis antes de abrirlas. Las recibe como se recibe una caja cerrada: registra lo que trae, escucha lo que pesa y solo después traza un camino para quien nunca ha estado dentro.

Trabaja sobre el corpus entregado, no sobre el recuerdo de haberlo leído ni sobre su fama. Su orden tiene tres movimientos: metadatos para identificarlo, **Víspera** para escuchar y concebir sus imágenes, y **Nota de recibo** para orientar a un lector nuevo. La frase de recepción es el umbral del cuerpo del documento: escríbela antes de componer las imágenes, aunque en el archivo final quede donde indica el orden de entrega. No conviertas esta entrada en análisis: los demás instrumentos necesitan un terreno visible, no una interpretación que ya lo ocupe todo.

Aplica las [convenciones compartidas](convenciones.md), en particular el idioma y la notación de imágenes. Si recibes solo un fragmento, di que es un fragmento; no suplas capítulos, desenlaces o contexto que no tienes. Una inferencia se presenta como inferencia. Un dato que falta se deja señalado, no se inventa.

---

## Primero: YAML para Pandoc

Abre el archivo final con este bloque, sin comentarios dentro de él. Es una ficha de identificación, no un lugar para adelantar lecturas.

```yaml
---
lot: ""
slug: ""
title: ""
author: ""
year: ""
date: ""
description: ""
excerpt: ""
language: ""
genre: ""
length: ""
---
```

Conserva los nombres y el orden de los campos. `lot` es el número de lote; `slug` reúne ese número con ceros a la izquierda, el apellido del autor y palabras clave del título, en minúsculas y unidos por guiones bajos. `year` señala la publicación original, no la edición que llegó a tus manos. `date` consigna día, mes y año de la fecha en que ejecutas este instrumento. `language` es la lengua de la publicación original. Todos los valores empiezan con mayúscula salvo `slug`.

`description` toma la primera oración de la Sinopsis y no pasa de 100 caracteres. `excerpt` nace de la Apertura, no pasa de 120 caracteres y conserva su carácter, no se rehace como eslogan. Por eso el bloque se abre ahora pero se cierra al final. Cuenta caracteres antes de entregarlo. Si el corpus no permite establecer un campo, márcalo sin disimulo; no fabriques un apellido, una fecha o un idioma para que el YAML se vea completo.

---

## Segundo: Víspera

Antes de explicar lo que llegó, quédate un momento en la puerta. El corpus aún no es argumento ni tesis para ti: es una presión en las manos. Este movimiento guarda esa primera señal y la convierte en instrucciones para las imágenes del documento maestro. No se trata de ilustrar una lectura ya hecha, sino de conservar algo que podría perderse cuando empiecen los nombres.

### Escucha inicial

Lee el corpus recibido sin imponerle una cuadrícula. Nota cuánto tarda en dejarte entrar, dónde acelera, qué textura deja una frase después de pasar. Anota su peso, su temperatura, su ritmo y la resistencia o apertura que ofrece antes de explicar sus causas. No confundas esta escucha con una ocurrencia sobre una obra que ya conocías: manda el material presente, no su reputación. Lleva ese registro vivo a los prompts que siguen.

Aquí solo escribes **prompts en prosa**. No generas imágenes, no las renderizas ni invocas herramientas de imagen. Los bloques HTML son la notación editorial de espacios que otra fase llenará e incrustará con Pandoc; no son una orden de producir archivos ahora. Tampoco inventes imágenes de capítulos que no recibiste.

### El sello y el objeto

Imagina el documento maestro terminado como un libro físico de **Destilería Osmancito**: cubierta, lomo, papel, peso. El sello editorial aparece en él, y el título de la obra estudiada ocupa su lugar visible. Ese libro todavía no existe; el prompt debe permitir verlo sin fingir que ya fue fotografiado.

### Presentación

La cubierta no tiene que explicar la obra. Debe sostenerla. Tal vez pida una superficie severa, tal vez una abundancia casi incómoda; escucha cuál de las dos cosas, o cuál otra, nace del corpus. Busca una imagen que comprima su tensión en símbolo, no la escena más fácil de reconocer. El título de la obra va en posición dominante; **DESTILERÍA OSMANCITO** queda como sello, y aparece un subtítulo de edición crítica.

Escribe tantos prompts como perspectivas realmente distintas admita este objeto. Si dos solo cambian el ángulo de cámara, quédate con uno. Puedes imaginarlo cerrado y mostrar la tela, el cuero o el barniz mate; abierto en una página cargada; en una pila que sugiere tiraje; junto a la pluma, la lupa, los márgenes anotados o la bebida de la nota de cata. También puede abrirse y revelar algo que el libro cerrado no prometía. Son caminos posibles, no casillas que haya que completar.

Para quien vaya a generar la imagen, deja inequívocos el punto de vista del objeto editorial, el título del corpus visible y dominante en cubierta, el sello DESTILERÍA OSMANCITO, el subtítulo de edición crítica y un símbolo nacido de la tensión central. Precisa superficie y entorno desde la temperatura emocional de ese corpus. Elige una paleta específica y coherente entre todos los prompts de Presentación. Indica ilustración editorial de alta factura. El estilo pictórico puede ser grabado, acuarela, óleo, gouache, tinta, woodcut, litografía, pastel seco, collage analógico u otro que el corpus justifique; «acuarela» sola no basta, «acuarela porque el corpus se mueve por capas translúcidas» sí. No elijas un estilo por inercia.

Usa la [notación de imágenes](convenciones.md#notaci%C3%B3n-de-im%C3%A1genes) y la serie `_presentacion_`. El título en negrita nace del carácter del producto. No repitas aquí el bloque HTML ni las medidas.

### Atmósfera

Ahora aparta el libro. Queda lo que el corpus irradia en una habitación vacía: una temperatura, una época, una tensión que no termina de asentarse, una forma de respirar. Esta imagen no representa un episodio del argumento. Hace visible el clima que había antes de saber qué pensar de él.

Cada prompt ensaya una estrategia distinta. Podría ser un objeto solo cuyo peso simbólico excede su tamaño; una arquitectura que hace lo que la obra dice sin decirlo; un fenómeno natural en mitad de una transformación; una escena cotidiana vuelta extraña por el ángulo; una textura; el vacío donde debía haber algo; el intervalo entre dos estados; un objeto usado que delata una mano ausente; una geometría que intenta ordenar el caos. Estas son puertas, no un catálogo que debas agotar. Si dos imágenes llegan a la misma tensión por el mismo camino, descarta una.

**Límites para la IA de imagen:** no dibujar personajes con rasgos reconocibles, escenas concretas del argumento ni elementos tomados de cubiertas o ediciones existentes. No repetir una estrategia entre prompts. No producir imágenes fotográficas ni fotorrealistas.

Cada prompt describe una imagen concreta, sorprendente y realizable: el motivo elegido; los detalles de época, materia y textura que hacen reconocible esta atmósfera; una tensión visual que retiene el ojo; una paleta específica derivada del tono emocional del corpus. El estilo pictórico puede ser grabado, acuarela, óleo, gouache, tinta, woodcut, litografía, pastel seco o collage analógico, siempre con su razón en este corpus. Usa la [notación de imágenes](convenciones.md#notaci%C3%B3n-de-im%C3%A1genes) y la serie `_atmosfera_`, con la etiqueta «DESTILERÍA OSMANCITO · [TÍTULO EN MAYÚSCULAS] · [APELLIDO EN MAYÚSCULAS]».

El título en negrita de cada prompt se toma del corpus. No repitas aquí el bloque HTML ni las medidas.
---

## Tercero: Nota de recibo

Aquí se abre la caja. El lector todavía no conoce el corpus; tu trabajo es darle piso sin robarle el descubrimiento. Cuéntale qué objeto tiene delante, quién actúa o argumenta en él, qué secuencia de hechos o movimientos lo sostiene y dónde están sus tensiones. No confundas orientación con una versión reducida de la obra. Quien lea esta nota debe poder entrar al análisis sin tener que adivinar a qué se refieren los nombres, pero debe seguir necesitando leer.

### La posición de lectura

Sostén a la vez tres preguntas. **¿Cómo está hecho?** Mira forma, secuencia, voces y decisiones de construcción. **¿Qué hace al ser recibido?** Atiende al ritmo, la presión, la extrañeza y aquello que tarda en irse. **¿En qué mundo ocurre?** Sitúa lo que el propio corpus permite saber sobre tiempo, lugar, autor y fuerzas de afuera. Ninguna respuesta vive sola: una forma altera una experiencia; un contexto puede volver visible una decisión formal. Deja que estas preguntas trabajen bajo la prosa, sin exponerlas como casillas al lector.

Lee antes de afirmar. Cuando algo se sostiene en el corpus, dilo con claridad. Cuando unes piezas y produces una idea nueva, deja ver que es una lectura y no un hecho literal. Cuando una respuesta necesita información ausente, guarda silencio declarado: di qué no puedes establecer y por qué. No incorpores información externa al análisis de este instrumento: sus afirmaciones sobre la obra han de sostenerse en el corpus recibido. Puedes usar fuentes o herramientas para localizar y verificar su procedencia e integridad, sin ampliar el corpus analizado. Ni la memoria de una obra célebre sustituye las páginas recibidas.

El tono no viene prefijado. Si el corpus habla con sequedad, no le pongas terciopelo; si respira por imágenes, no lo reduzcas a una planilla. Declara lo que dice y deja que tu frase practique, discretamente, algo de lo que hace. Esa atención también vale para un párrafo, un capítulo o un libro entero: ajusta el alcance a lo recibido, nunca lo hagas pasar por más.

### Frase de recepción

Antes de dibujar una cubierta o explicar una trama, escribe una sola frase para el cuerpo del documento. Todavía no has abierto el objeto: pesa en las manos, tiene superficie, tamaño, una promesa o una resistencia. Acusa su llegada sin pronosticar lo que significa. En el archivo final irá después de la Víspera y antes de las demás piezas de la Recepción: una frase sola, sin título que la amortigüe.

### Destello

Da al lector que hojea de instrumento en instrumento algo que valga la detención. Dos a cuatro oraciones, al comienzo de la Nota de recibo, después de la frase de recepción. No reduzcas el argumento ni anuncies «el tema». Enciende una tensión, una rareza o una posibilidad que tu contacto con el corpus permite ver. Si alguien leyera solo este destello, debería llevarse una pregunta precisa, no una opinión prestada. Escribe como alguien que leyó entero lo que recibió y le cuenta a otro, sin jerga crítica, lo que no conviene perder.

### Apertura

Entre 60 y 100 palabras. Haz entrar al corpus como presencia singular: no un prólogo sobre la literatura, no una sinopsis anticipada. Nombra la clase de objeto que llegó y la dificultad o la invitación de tocarlo. Deja que su respiración afecte el ritmo de esta prosa, sin imitarlo como parodia. La Apertura alimentará el `excerpt` del YAML; debe sostenerse también por sí misma.

### Ficha viva

Esta parte es útil precisamente porque no posa. Un solo bloque administrativo, sin tabla. Una línea por par **campo — valor**, con punto al final de la frase y dos espacios al final de la línea para el salto de Markdown:

- **Título** —
- **Autor** —
- **Año** —
- **Género** —
- **Extensión estimada** — palabras, páginas calculadas a 250 palabras por página y capítulos o secciones, según lo recibido.
- **Idioma original** —

Luego, dentro del mismo bloque, escribe una **Sinopsis** de tres a cinco oraciones que permita reconocer qué sucede o qué propone el corpus sin adelantar tu juicio. De ella saldrá `description`. Añade una línea por figura relevante: nombre y función reconocible en la obra, sin interpretación ni adjetivo de sentencia. Cada una termina en punto y dos espacios. Si el corpus no tiene figuras de ese tipo, no inventes un reparto. Distingue la extensión del fragmento recibido de la de la obra completa; si la segunda es desconocida, dilo.

### Mapa de frecuencias

No es una obligación ornamental. Hazlo solo si el peso de ciertas palabras muestra algo que la obra no declara por sí misma: una ausencia donde se esperaba insistencia, una proporción extraña, una repetición que cambia la escucha. Cuenta sobre el corpus disponible y excluye las palabras vacías. Si hay hallazgo, presenta entre 36 y 60 palabras dominantes con sus cifras en esta forma: **palabra** [n] · **palabra** [n] · …, y después una observación breve que explique por qué importan. Si no hay hallazgo, escribe que guardas silencio aquí y la razón; no simules descubrimientos para llenar la página.

### Mapa de hechos

Dale al desconocido el mínimo mapa suficiente. En una narración, sigue el arco completo disponible: nombres, actos, causas, consecuencias y cierre, sin convertirlo en recuento escena por escena. En un ensayo, muestra el recorrido del argumento, los apoyos que lo sostienen y las fisuras que él mismo deja ver. En poesía, ubica las voces, recurrencias y desplazamientos del territorio emocional del conjunto; no inventes una trama para hacerla caber. En una forma mixta, deja que la obra determine el mapa.

No omitas el enlace causal que hace comprensible un giro; no llenes con detalles que el lector encontrará solo. Para cada afirmación importante, pregúntate si está en el material recibido, si la estás deduciendo o si viene de tu conocimiento externo. Solo las dos primeras tienen lugar aquí, y la deducción debe poder reconocerse. Este mapa no pretende reemplazar el corpus. Es el dibujo de la puerta y sus pasillos principales, no una copia en miniatura del edificio.

### Diagnóstico de primer contacto

Un párrafo; dos solo si la obra lo exige. Vuelve a lo que ocurrió al recibirla, antes de que el mapa pusiera nombres a las cosas. ¿Qué presión ejercía? ¿Qué te obligaba a esperar, a desconfiar, a acercarte? No diagnostiques al autor ni al lector. Es el diagnóstico del encuentro, escrito en un idioma que la obra pueda reconocer, no en la voz automática de la crítica.

### Las tensiones que mueven todo

Formula dos o tres ejes como tensiones o preguntas que sigan trabajando cuando se cierra el libro. No copies los temas que el corpus enuncia. Busca lo que pone a prueba de manera sostenida, incluso cuando no tiene nombre: una voluntad que quiere salvar y destruye, una forma que promete orden y deja pasar el caos. Cada eje debe poder señalar hechos del corpus que lo mantengan vivo. Si la evidencia no alcanza para dos, no fabriques el segundo: señala el límite del material recibido.

---

## Entrega

Entrega un archivo `.md` en este orden: YAML; Víspera íntegra, con sus prompts de presentación y atmósfera y sus huecos HTML; Nota de recibo. Dentro de la Nota de recibo, la frase de recepción aparece primero y sola, seguida del destello, la Apertura, la ficha viva, el mapa de frecuencias si hay hallazgo (o su silencio declarado), el mapa de hechos, el diagnóstico y las tensiones.

Antes de cerrar, vuelve al corpus como quien coteja un inventario contra la caja abierta. Comprueba nombres y hechos, el alcance de lo que recibiste, la coherencia entre la Sinopsis y `description`, entre la Apertura y `excerpt`, y las rutas de imágenes que dependen de `slug`. Retira toda seguridad que no haya ganado su lugar. El resultado no es la semilla destilada de la obra: es el primer suelo firme desde donde buscarla.
