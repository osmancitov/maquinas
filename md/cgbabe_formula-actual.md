# Fórmula actual

La primera receta de la Destilería leía un libro con instrumentos: una persona o un modelo de lenguaje recorría el texto y anotaba lo que veía. La receta 2.0 añade un paso anterior: medir el libro. Antes de opinar sobre un corpus, se le pone una regla encima, y la regla no sabe nada de literatura. Esta entrada cuenta qué es esa regla y qué se hace con lo que mide.

## Primer paso: partir el texto en frases

Un corpus es el conjunto de textos que se va a leer: una obra de teatro, un libro de cuentos. Se parte en frases, y cada frase conserva su sitio: de qué escena o de qué cuento viene. De un libro de trece cuentos salen unas dos mil frases, cada una con su etiqueta de origen.

## Segundo paso: convertir cada frase en un vector

Un vector es una lista de números. Un modelo de embeddings es un programa que lee una frase y devuelve una lista larga de números que la describe. Para esta receta cada frase se convierte en una lista de 2.048 números.

Conviene imaginarlo como una dirección. Una casa tiene una dirección de tres datos: calle, número, piso. Con tres datos basta para ubicarla en una ciudad. El significado de una frase es más rico que un lugar en un mapa, y por eso hacen falta 2.048 datos para ubicarla. Cada número es una coordenada, un eje. Nadie sabe ponerle nombre a cada eje, ni hace falta: son ejes que el modelo aprendió leyendo muchísimo texto, y ninguno significa por sí solo "tristeza" o "mar". El sentido está en el conjunto.

Lo que importa es esto: frases que significan cosas parecidas reciben listas parecidas. Dos frases sobre el mismo duelo caen cerca una de la otra, aunque no compartan ni una palabra. Una frase sobre un duelo y otra sobre un contrato caen lejos. El modelo no entiende como entiende una persona, pero ordena como si hubiera entendido algo.

El resultado es una nube de unos dos mil puntos en un espacio de 2.048 dimensiones. Un espacio así no se puede dibujar ni imaginar. Se puede medir: la distancia entre dos puntos dice cuánto se parecen dos frases.

## Tercer paso: aplanar

Para ver la nube hay que bajarla a dos dimensiones, como una hoja de papel. A eso lo llamamos aplanar. Es como dibujar el mapa de una esfera: siempre se pierde algo, así que se elige qué conservar. Aplanar se hace en tres pasadas, una detrás de otra. Cada una tiene su nombre y su oficio.

**PCA** (análisis de componentes principales). Busca los ejes en los que la nube más se estira y deja caer los demás. De 2.048 ejes se queda con unos cincuenta. Es parecido a mirar una nube de mosquitos y notar que casi todo el movimiento ocurre en dos o tres direcciones: se conservan esas y se descarta el temblor de las otras. Limpia el ruido y acorta el trabajo de lo que viene.

**UMAP**. Toma esos cincuenta ejes y baja la nube a dos. Su criterio es el vecindario: cada punto debe seguir al lado de sus vecinos más cercanos. No le importa tanto la distancia exacta entre grupos lejanos como que quienes eran vecinos sigan siéndolo. Al final entrega un mapa plano donde se ven islas.

**HDBSCAN**. Recorre el mapa y decide dónde hay un grupo. Los grupos son zonas densas, rodeadas de zonas vacías. No hay que decirle cuántos grupos buscar: lo que encuentra lo pone el dato. Los puntos sueltos, que no pertenecen a ninguna isla, se declaran sueltos y no se fuerzan dentro de un grupo.

Los tres métodos juntos son la receta de aplanado de la casa. Su valor está en la última pasada: la cuadrícula la pone el texto, no quien lo lee.

## Cuarto paso: preguntar al mapa

Con las islas dibujadas, cada frase aún lleva su etiqueta de origen. Ahora se puede mirar si las frases de una misma escena, o de un mismo cuento, caen juntas, o si se mezclan. Si los trece cuentos de un libro forman trece continentes, cada cuento es un mundo aparte. Si se mezclan, el autor escribía un solo mundo con trece puertas. El mapa no dicta cuál de las dos cosas es verdad. Enseña dónde mirar, y la lectura sigue siendo de quien lee. Como se dice en la casa: el método es su propia pregunta.

## Qué cambia respecto de la receta 1.0

Antes se partía de la lectura y se llegaba a un resumen. Ahora se parte de una medida y se llega a un mapa, y la lectura entra después, para explicar lo que el mapa muestra. La medida no sustituye a la lectura: le da a la lectura un terreno donde apoyarse.

## Límites

Un embedding refleja lo que su modelo aprendió, y otro modelo daría otro mapa parecido, no idéntico. El aplanado pierde información por definición. Una isla es una pista, no una prueba. La receta sirve para explorar un corpus, no para dictar sentencia sobre él.
