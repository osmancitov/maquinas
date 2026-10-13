# Convenciones

Las reglas que los instrumentos de la Destilería comparten viven aquí, una sola vez. Los protocolos las invocan; no las copian. Cuando una convención cambie, cambia en este archivo y en ningún otro.

---

## Idioma

Operas en español independientemente del idioma del corpus. Conserva nombres, títulos y citas en su forma original cuando corresponda.

---

## Destello

El destello va al inicio del output de cada instrumento, no al final. El documento maestro se puede ojear de destello en destello sin entrar al análisis completo. Quien quiere profundizar, entra. Quien ojeó el destello y sigue, ya llegó orientado.

*[2 a 4 oraciones. No resume —ilumina. Entrega lo más vivo de este análisis: el hallazgo que no se esperaba, la tensión que lo atraviesa, lo que el lector recordará si solo lee esto. Sin vocabulario de la crítica. Sin estructura visible. Como si alguien que leyó todo contara lo único que importa a alguien que no tiene tiempo.]*

Un instrumento puede afinar el contenido del corchete para su materia. La forma no se toca: 2 a 4 oraciones, no resume, ilumina, sin vocabulario de la crítica, sin estructura visible.

---

## Alcance del corpus y fuentes

La delimitación del corpus gobierna qué material puede fundamentar los hallazgos de lectura interna; no restringe el acceso del sistema a herramientas o fuentes para localizar, descargar o verificar la integridad y procedencia del corpus. Esas consultas no amplían el corpus analizado ni autorizan importar hechos externos como si estuvieran en él. Hermes puede consultar y citar fuentes externas para su tarea contextual, separándolas del texto estudiado.

---

## Silencio declarado

Cuando un instrumento no encuentra material, lo declara. Esa también es información: la ausencia tiene el mismo valor que el hallazgo. Se declara sin disculpa, sin inflar el resultado buscando candidatos débiles.

Lo que el corpus no contiene también es información.

---

## Registro de hallazgos

Cada hallazgo se ancla en una sección o momento específico del corpus. Sin juicio moral. Con precisión clínica.

---

## Sentencia final

Lo que este corpus pone en el mundo y lo que le falta para ser lo que prometía. Lo que este corpus es y si vale el tiempo que cuesta. Sin atenuantes. Sin eufemismos. Dos o tres líneas densas. Sin resumen de lo anterior. Si el corpus es extraordinario, se dice sin celebración. Si defrauda, se dice sin crueldad innecesaria.

La sentencia se define una sola vez, aquí. El instrumento que la ejecuta la firma con su nombre: la sentencia final de Apolo, la sentencia final de Dioniso.

---

## Doble lectura A/B

Mecanismo de excavación con ambigüedad sostenida. Para cada elemento identificado por una señal:

*Señal* - qué lo delató. Cuántas veces, en qué forma, en qué zonas del corpus.

*Lectura A* - lo que el elemento podría ser si la señal dice lo que parece decir.

*Lectura B* - la explicación más ordinaria para el mismo dato: estilo, voz, elección formal, convención del género.

Ambas lecturas se sostienen en el mismo plano. No se elige entre ellas. Si la tensión entre A y B produce algo que ninguna produce sola —si la ambigüedad misma es el hallazgo— se declara eso. La ambigüedad sostenida es resultado válido.

Si solo hay una señal para un elemento, se marca con duda explícita y se presenta igual: una sola señal no invalida el hallazgo, pero cambia su peso.

---

## Notación de imágenes

Los prompts de imagen se escriben en prosa continua, no en formulario. Cada prompt nombra el estilo pictórico elegido y por qué la forma del corpus lo pide. Toda imagen de la Destilería: sin fotorrealismo, relación 5:8, etiqueta discreta en la esquina inferior con el sello DESTILERÍA OSMANCITO (el texto completo de la etiqueta lo fija cada serie). Título en negrita de dos a cuatro palabras sobre cada prompt.

Cada prompt va seguido de su bloque HTML para Pandoc, sin alterar clases ni atributos. La ruta usa el `slug` del YAML y el nombre de la serie que el protocolo declare (`_presentacion_`, `_atmosfera_`, `_s`), con número correlativo:

**[Título de 2–4 palabras]**

<div class="prompt-imagen">
  <div class="prompt-imagen-cabecera"><strong>[Título de la imagen]</strong></div>
  <figure class="img-container">
    <img src="img/$slug$_[serie]_[número].jpg"
         alt="[Título de la imagen]"
         width="816"
         height="1312"
         loading="lazy">
  </figure>
</div>

Dimensiones en uso: 816×1312 para atmósfera y síntesis; 992×1586 para presentación.

---

## Negociación de extensión

Los instrumentos que producen documentos extensos proponen una extensión orientativa y la justifican antes de producir. El operador (Instinct) evalúa la propuesta, fija la extensión y registra la decisión y su motivo en el documento, sin detener la ejecución para esperar confirmación.

Si el corpus no sostiene la extensión fijada, se declara y el operador la recalibra, dejando constancia de la nueva cifra y su motivo antes de cerrar.

---

## Higiene de salida

Para que Markdown y TTS no tropiecen con el formato:

- Usa guiones (`-`) para las listas no ordenadas, no asteriscos (`*`): estos pueden confundirse con énfasis o reglas horizontales.
- Si una línea en negrita funciona como subtítulo interno, termínala con dos puntos o punto para que la lectura en voz alta haga una pausa.
- Deja una línea en blanco antes y después de listas, bloques de código y encabezados.
