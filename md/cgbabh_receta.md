17 de octubre de 2026

# La receta

![Sala de máquinas](../img/maquinas.jpg)

La receta completa de la Destilería, de principio a fin: de un libro a su página destilada. Queda fijada el 17 de octubre de 2026 («la misma receta, 1, con glosa nivel 3 escuela. Esa receta va fija de ahora en adelante hasta que consigamos una mejor»). Vive en este archivo y en ningún otro; lo que la cambie, la cambia aquí.

## 1. Fuente: del epub al markdown

El libro llega como epub a la bóveda (una carpeta por obra, «Autor Obra»). Se convierte a un solo `.md`, que queda suelto en la carpeta, junto al epub:

- Se leen los archivos del lomo en orden de lectura. La portada (imagen) y la tabla de contenido automática se omiten.
- Los rótulos de capítulo y sección quedan como encabezados `## `; el título del libro, como `# `.
- Las marcas de nota al pie se quitan del texto corrido; las notas se conservan numeradas al final, bajo `## Footnotes`.
- La letra capital suelta que abre un capítulo se reintegra a su palabra («T HE» → «THE»).
- Los pies de foto se conservan como texto; las imágenes no entran al `.md`.
- El texto se guarda llano, sin marcas de cursiva ni negrita.

## 2. Molde: la segmentación canónica

El `.md` se parte en frases y cada frase recibe su identidad. El molde es `embeds/segmentacion-canonica.json`, con la especificación completa en `boveda/README.md`:

- IDs de dos letras y un contador corrido por obra: `BD` (cuerpo), `SD` (didascalia), `EP` (epígrafe), `PT` (paratexto), `DS` (descarte).
- Cada segmento guarda sus offsets exactos en la fuente (`char_start`, `char_end`), su texto normalizado y su texto literal, su tipo y su localización (escena o capítulo).
- El paratexto preliminar se localiza en `Preliminares`; las notas, índices, créditos, dedicatorias, firmas y pies de foto son `PT` con su subtipo.
- El molde pasa cinco pruebas mecánicas: fidelidad, cobertura, catálogo, IDs y localización. No se admite sin las cinco.
- Solo las frases `BD` se vectorizan: se vectoriza lo que se estudia.

## 3. Vectores: medir una sola vez

Un motor basta. El motor es gratuito y el gasto es cero. Los vectores se guardan en `embeds/<nombre exacto del motor>/`, en un solo `.json.gz` cuantizado a int8 (cada coordenada ×128, redondeada y recortada a [-128, 127]), como diccionario `{ID: [enteros]}`. Con molde y vectores guardados, todo lo demás se regenera local, sin volver a llamar a la máquina.

Motores usados hasta ahora: `voyage-4-large` (Voyage) y `gemini-embedding-001` y `gemini-embedding-2` (Google, llave gratuita, lotes de cien textos, un lote por minuto, tope de mil textos al día por modelo).

## 4. Reserva: el ranking al centroide

Cómputo local sobre los vectores guardados:

- Se promedian los vectores `BD` de la obra: ese promedio es el centroide, el centro de gravedad del libro.
- Cada frase se ordena por su cercanía al centroide (coseno).
- De cada unidad —la escena en teatro, el capítulo o la sección en prosa— entra a la reserva el 10% superior de su ranking.

La reserva es el material del que se escogen las citas. Las unidades cortas pueden quedar con reserva pobre; se sirven con lo que haya y el resto va a los puentes.

## 5. Selección: los tres criterios

De la reserva se eligen las citas una a una, con tres criterios:

1. **Movimiento:** la frase hace avanzar algo —la acción, la idea, el corazón.
2. **Se entiende sola:** se sostiene fuera de su contexto.
3. **Voz propia:** suena a su autor y a nadie más.

## 6. Glosa nivel tres

Cada cita lleva su glosa en castellano llano, de nivel escolar: explica lo que la cita supone —quién habla, qué pasó antes, la palabra rara— sin vocabulario de crítica. La glosa acompaña la decisión: la frase que necesita tres líneas de rescate para sostenerse confiesa que no entra.

## 7. Traducción y puentes

Cada cita va en su idioma original, con la traducción al castellano debajo. Entre cita y cita, los puentes en cursiva cuentan lo que ocurre, abren la pieza y la orientan. Una prohibición: nunca se parafrasea lo que el texto ya dice; si la frase existe, se cita.

## 8. Texto de presentación (fijo)

Toda página destilada abre con una sola pieza: un párrafo que presenta la obra como tal —qué es, quién la escribió, de qué trata—. Ninguna cifra en la intro: ni las páginas del destilado, ni las de la fuente, ni la proporción entre ambos, ni cuántas frases tenía el original, ni cuántas citas quedaron, ni ninguna frase que explique el oficio de la página (cómo van las citas, las traducciones, las glosas o los puentes), porque se ve a simple vista.

## 9. Página: la entrega

- La página vive en la Destilería como gemelos `html/cgbabX_nombre.md` y `html/cgbabX_nombre.html`, y entra al tope de la lista en `destileria.html` y en el `README.md`: lo más nuevo primero.
- Lleva fecha arriba, título, su dibujo (1280×640, `html/img/cgbabX_nombre_og.jpg`, declarado en el `og:image`), el autor, el texto de presentación y el cuerpo por unidad, con un `## ` por escena o capítulo.
- Cada escena o capítulo puede llevar además su propio dibujo, cuando él lo pida para esa obra; se genera igualmente con Gemini Web y se coloca justo bajo el encabezado `## ` de la unidad. (El Yogi llevará dibujo por capítulo; se generan cuando la sesión de Gemini Web quede libre, porque solo cabe una sesión a la vez.)
- Las citas van en bloque, la traducción debajo, el hablante cuando lo hay, los puentes en cursiva.
- Cierra con la firma: «Osmancito, con la asistencia de Instinct».
- Después de la firma, un solo enlace de regreso a su sala: «volver».

## 10. Verificación

Con la obra abierta, nunca de memoria. Cada cita se busca literal en la fuente —el molde da sus offsets—. La página se ve en el navegador antes de publicarse.

## Reglas transversales

- Gasto cero sin permiso expreso.
- Los dibujos de las páginas se generan con Gemini Web (su sesión de Google), nunca con la herramienta de imágenes de Instinct; la cuota propia de Instinct es solo para la Capilla.
- La frase es la referencia y la moneda de la casa.
- El idioma es el castellano.
- Sin URLs en las páginas.
- Los archivos viejos que una versión nueva reemplaza se borran, con su confirmo.

## Historia

Esta receta sustituye al cuaderno del Taller «El procedimiento de la Destilería» (14 de octubre de 2026) y a todo lo que ese absorbió: la Receta 2.0, los criterios de corpus, la medida de significado, el mapa del corpus y el demi-glace. Los Protocolos antiguos quedan como están: son la primera etapa, ya declarada historia.

Cambios después de fijada:

- 17 de octubre de 2026, 19:31: el texto de presentación se simplifica —presenta la obra, no el destilado, y el único número que lleva son las páginas del destilado. Antes llevaba también las páginas de la fuente y la proporción («de cada cien palabras…»), y en una primera lectura quedaron fuera también los conteos de frases y citas.
- 18 de octubre de 2026, 06:48: la regla transversal del idioma queda escrita en positivo: «El idioma es el castellano».
- 17 de octubre de 2026, 22:23: regla del enlace «volver» tras la firma (toda página de entrada termina con un solo enlace de regreso a su sala); anotada en la sección 9 y aplicada a la página del Yogi.
- 17 de octubre de 2026, 21:59: él decide que el Yogi lleve un dibujo por capítulo además del de portada; queda anotado en la sección 9. Los dibujos se generan después, cuando Macbeth libere la sesión de Gemini Web.
- 17 de octubre de 2026, 19:53: se quita de la intro la línea con el dato de páginas; la introducción queda solo con el párrafo que presenta la obra. «Definitivamente no fue buena idea meter el dato de las páginas. El resto de la introducción está excelente.»
- 17 de octubre de 2026, 19:47: el cierre de la intro queda en una sola línea —«La obra completa, destilada en N páginas.»—; reemplaza las dos líneas anteriores («destilada escena por escena…» + «se lee en unas N páginas»). «Qué cuesta decir lo que hay que decir y ya.»
- 17 de octubre de 2026, 19:39: el texto de presentación queda en dos piezas solas —el párrafo de la obra y la línea de las páginas—; se borra de todas las intros la frase que explicaba el formato de citas, glosas y puentes («se ve a simple vista», dijo).
- 17 de octubre de 2026, 19:37: regla de dibujos anotada en transversales: Gemini Web con su sesión, nunca la herramienta de imágenes de Instinct (regla suya ya vigente).
