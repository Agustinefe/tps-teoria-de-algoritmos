# Trabajo Práctico 1: Técnicas de Diseño

## Primera Parte: Problema de K-merge por División y Conquista

### Como ejecutar los scripts

#### Simulación

```$ python3 simulator.py```

La configuración de la simulación se encuentra en el archivo *simconfig.json*. Los archivos con los resultados se guardan en la carpeta *results*.

Los nombres de los resultados corresponden a la hora en la que finalizó su simulación.

#### Plotting

```python3 complexity-check.py [results\example.json]```

Los gráficos se guardan en la carpeta *plots*, en una carpeta con el mismo nombre del example.json. Hay un archivo *plot* y uno *diff*. Este *README lee imágenes de la carpeta *plot*.

### Introducción

El problema de K-merge es el siguiente: se tienen K arreglos ordenados, y se quiere quiere obtener un único arreglo, también
ordenado, con todos los elementos de los arreglos originales (inclusive si hay repetidos). Por simplicidad para los diferentes
análisis se puede suponer que todos los arreglos tienen exactamente h elementos (por ende, la cantidad total de elementos es
n = K ∗ h).
Para resolver este problema, es posible que hayan visto en Algoritmos y Programación II un algoritmo que resuelve este
problema utilizando un Heap. Nos referiremos a este como el algoritmo que utiliza Heaps.
La idea en este caso será plantear otra solución y analizarla. Se propone el siguiente algoritmo por división y conquista, con
semejanzas a mergesort.
1. Caso base: cuando quede un único arreglo, simplemente devolver dicho arreglo.
2. En el caso general, dividir la cantidad de arreglos entre la primera mitad, y la segunda mitad, y luego invocar
recursivamente para cada mitad de arreglos. Es decir, si tenemos cuatro arreglos, invocamos para los primeros 2, y
luego para los segundos 2. Al terminar los llamados recursivos, tenemos dos arreglos ordenados. Estos deberán ser
intercalados ordenadamente, tal cual se realiza en mergesort.

### Consigna

1. Determinar, utilizando el Teorema Maestro, cuál sería la complejidad del algoritmo propuesto.

    El Teorema Maestro nos provee una forma sencilla de estimar la complejidad temporal de un algoritmo. Para su aplicacion debemos determinar los siguientes aspectos de nuestroa algoritmo:
    - La cantidad de llamados recursivos que realiza el algoritmo.
    - La proporcion del problema original que se pasa al llamado recursivo.
    - La costo algoritmico de partir en subproblemas y juntar las subsoluciones. 
    
    El algoritmo propuesto describe que la lista de K arreglos original debe ser dividida en dos mitades, para posteriormente realizar llamados recursivos sobre ella. Esto nos permite inducir que se realizan dos llamados recursivos, donde la proporcion del problema evaluada en el llamado es de la mitad del problema.
    
    Por otra parte, partir el problema puede implementarse a traves de la actualizacion de indices que indiquen el inicio y final del subproblema, sin necesidad de realizar un slice sobre el problema original; esto puede realizarse en tiempo constante.
    
    Por ultimo, el problema indica que la junta de los subproblemas debe realizar mediante un algoritmo de intercalamiento, como el utilizado en mergesort. Esta junta (en mergesort) es O(n), y en este caso seria de manera similar. Sabiendo que n = K * h, el costo de juntar las subsoluciones tambien sera de O(n).
    
    Con esto en mente, nuestra ecuacion de recurrencia quedaria de la siguiente manera: T(n) = 2 * T(K/2) + O(n), y, por el Teorema Maestro, podemos afirmar que la complejidad del algoritmo propuesto es de O(n * log2(K))


---


2. Describir el algoritmo que utiliza heaps, y determinar su complejidad.

    A continuación, se enuncia el algoritmo y en simultáneo se va detallando la complejidad de cada operación. El K-merge con heaps trabaja tomando al comienzo el primer elemento de cada uno de los K arreglos ordenados e insertándolos (encolándolos) en un heap de mínimos (en O(K), justamente por ser un heap), que servirá posteriormente para ir siempre sabiendo cuál es el elemento de valor más chico y así ir construyendo el arreglo final.

    ¿Cómo logramos esto? Para empezar, no se guarda simplemente el valor del arreglo, sino que también se guarda el número del arreglo al que pertenece y el índice dentro de ese arreglo (en este caso, se puede realizar con un struct o una sencilla clase con tan solo los 3 atributos mencionados). La importancia de esto es que se utilizará para en un loop ir desencolando del heap el elemento más pequeño, agregándolo al arreglo final y encolando el siguiente elemento (si lo hubiera) del arreglo al que pertenecía el elemento que se desencoló. Esto sucederá hasta que el heap no tenga más elementos, que a su vez solo sucederá una vez que cada uno de los h elementos de cada uno de los K arreglos hayan pasado por el heap (es decir, se hayan encolado, agregado al arreglo final y luego desencolado).

    Debido a que las operaciones de encolar y desencolar dentro del loop se realizan en O(log(K)) (estrictamente sería O(log(K)) + O(log(K)) porque son dos operaciones por cada iteración) y esto se realizará por la cantidad total de elementos, como indica la consigna, n = K * h), las operaciones del loop se realizan en O(n * log(K)).

    Como O(n * log(K)) es mayor que O(K) ya que n = K * h, entonces la complejidad del algoritmo es O(n * log(K)).
    
---

3. Implementar ambos algoritmos, y hacer mediciones (y gráficos) que permitan entender si las complejidades obtenidas para cada uno se condicen con la realidad.

    Hemos observado que tanto el algoritmo propuesto con merge como el algoritmo de heaps tienen una complejidad temporal de O(n * log(K)), siendo n = K * h.
    
    ## K-merge con D&C
    
    Dado que el problema de k-merge presenta dos variables en su contexto (K: cantidad de arreglos ordenados, h: tamaño de esos arreglos), mostrar su desempeño mediante gráficos nos obligaria a que estos gráficos sean tridimensionales. Sin embargo, la **regla del producto** nos permite asegurarnos que **O(K * h * log(K)) = O(h) * O(K * log(K))**. De poder identificar que partes de cada algoritmo son las que añaden cada una de las complejidades (O(h) y O(K * log(K)), solo necesitaríamos un gráfico por cada complejidad temporal, para poder probar la complejidad temporal total de cada algoritmo. ¡Y podemos identificarlas! 
    
    **O(K * log(K))** es la complejidad temporal de ordenar K arreglos ordenados de un solo elemento, lo que tambión podria significar ordenar un arreglo de K elementos con merge. Esto explica por qué esta parte tiene la misma complejidad que el algoritmo Mergesort.
    
    **O(h)**, por otra parte, es la complejidad temporal de mergear dos arreglos ordenados, dado que inevitablemente se deberan recorrer ambos arreglos de inicio a fin para realizar el intercalado. El costo temporal de este merge crece linealmente respecto de h.
    
    *"Pero alumnos, este es un solo algoritmo. No podemos correr la parte de O(h) por un lado y la parte de O(K * log(K))" por otro lado"*. Es cierto que no podemos particionar el algoritmo y evaluarlos por separados. Lo que **sí** podemos hacer, es setear una variable con una constante, y evaluar el desempeño del algoritmo cuando la otra variable *varía*. Así, si el tamaño de todos los arreglos fuese de uno (h = 1), sería lo mismo que tener números individuales, lo que desembocaría en un Mergesort (O(K * log(K))). Si en cambio siempre tuviésemos 2 arreglos de h elementos (K = 2), entonces el algoritmo solo se encargaría de separarlos del arreglo de arreglos (lo cual es O(1)), y luego debería mergearlos (lo cual, como ya vimos, es O(h)). *¿Por qué h es 2, y no 1?*, si hubiese solo un arreglo ordenado, entonces el algoritmo solo debería devolver el arreglo, sin hacer merge, pudiendo hacerlo en O(1).
    
        
    ### Análisis de la parte *mergesort* del algoritmo

    Como se mencionó previamente, si h = 1, entonces el algoritmo debería comportarse de manera semejante a Mergesort. Al realizar mediciones y graficar los costos temporales de correr el algoritmo con determinada muestra (lineal), esperaremos encontrarnos con un gráfico semejante a un n * log2(n).

    El siguiente gráfico muestra los resultados de evaluar el algoritmo en una secuencia de 1 a 20.000.000, en intervalos de 2.000.000, donde cada muestra ha sido evaluada 10 veces, y calculado la mediana de los resultados de cada muestra.

    ![D&C var-K plot (1)](/plots/2023-04-22_15-55-58/plot.png "2023-04-22_15-55-58/plot.png")
    
    Si bien podría pertenecer a un intervalo de alguna función del estilo f(n) = n * log2(n), también podría ser un intervalo de una función lineal g(n) = n. Esto quiere decir que para generar una muestra mucho mas exacta, debemos realizar simulaciones mucho mas refinadas, implicando esto una secuencia de cantidades mucho mas grandes, mayor repetición de pruebas para cada cantidad, y, en consecuencia, mucho mas tiempo de ejecución (simular para obtener estas mediciones ha llevado cerca de una hora).

    Sin embargo, podemos aprovechar las propiedades matemáticas de las funciones, y calcular una "derivada" de la muestra. Si la muestra siguiese una proporción lineal, entonces la diferencia entre los tiempos debería ser (casi) constante, dado que la derivada de una funcion linear es una función constante. Pero si la muestra siguiese efectivamente una proporción de n * log2(n), entonces la diferencia entre tiempos deberia seguir una proporción logarítmica, dado que la derivada de n * log2(n) es log2(n) + 1/ln(2) (y podemos ignorar la constante 1/ln(2)).

    ![D&C var-K diff (1)](/plots/2023-04-22_15-55-58/diff.png "2023-04-22_15-55-58/diff.png")

    Podemos observar que, con algunos altibajos, las diferencias entre tiempos siguen una proporción logarítmica, lo cual nos permite confirmar que esta parte del algoritmo es O(K * log(K))

    ### Análisis de la parte de *merge* del algoritmo

    Cuando K = 2, podemos medir como funciona la parte del ordenamiento por merge del algoritmo. Como se menciono previamente, se estima que esta parte tiene una complejidad temporal de O(h).

    El siguiente gráfico muestra los resultados de evaluar el algoritmo en una secuencia de 1 a 10.000.001, en intervalos de 1.000.000, donde cada muestra ha sido evaluada 10 veces, y calculado la mediana de los resultados de cada muestra.

    ![D&C var-h plot (1)](/plots/2023-04-22_20-01-22/plot.png "2023-04-22_20-01-22/plot.png")

    Podemos observar que las mediciones siguen una proporción lineal, pero para descartar la posibilidad de un posible n * log(n), graficaremos también las diferencias entre tiempos.
    
    ![D&C var-h diff (1)](/plots/2023-04-22_20-01-22/diff.png "2023-04-22_20-01-22/diff.png")

    A diferencia de los diffs obtenidos al medir la parte de O(K * log(K)), que mostraban una proporción logarítmica, en estos diffs se puede observar un comportamiento que a simple vista parece errático, pero que al notar que el intervalo donde oscila la muestra es de solo 0,0175 segundos, y no pareciera haber signos de una monotonía creciente o decreciente (sino un comportamiento oscilante), podemos afirmar que esta parte del algoritmo es O(h).
    
    ## K-merge con Heaps

    En esta sección volveremos a hacer uso de las propiedades que nos permitieron analizar el K-merge con D&C a partir de evaluar por separado los componentes de la complejidad del algoritmo. Recordemos, como se explicó detalladamente en el punto 2), la complejidad del K-merge con heaps es de O(h * k * log(K)). Para ello, primero deduzcamos qué sucede al fijar el valor de cada variable para este caso.
    
    Si la cantidad de elementos por arreglo (h) fuera uno (1), la complejidad del algoritmo sería O(K * log(K)), es decir, ya podríamos graficar en dos dimensiones. También podríamos animarnos a hacer un paralelismo (no tan literal como en el caso del K-merge con D&C, pero posible) con Heapsort, siendo éste un algoritmo que también utiliza un heap, del cual va desencolando para ir ordenando el arreglo inicial, lo que lo hace tener una complejidad de O(n * log(n)) donde n es la longitud del arreglo inicial. Sin embargo, esta comparación puede ser innecesaria, debido a que el input de Heapsort es un único arreglo, que es ordenado a partir de desencolar el heap e ir realizando swaps, mientras que K-merge con Heaps se encarga de a partir de múltiples arreglos mergearlos y devolver uno único, y si se tratara del caso en que h es igual a 1, entonces obtendríamos una complejidad de O(K * log(K)), lo cual es muy tentador para vincular ambos algoritmos incluso aunque tengan objetivos diferentes. A pesar de esto, y con fines de simplemente identificar el componente con complejidad O(K * log(K)), lo denominaremos "parte *pseudo heapsort*" del algoritmo.
    
    ### Análisis de la parte de *heapsort* del algoritmo
    
    Una vez más, considerando el caso de h = 1, realizaremos ejecuciones con las mismas características o parámetros que se utilizaron previamente para el análisis de la parte *merge* del K-merge con D&C (secuencia de 1 a 20.000.000, intervalos de 2.000.000, 10 evaluaciones, uso de mediana, etc.) y esperaremos obtener resultados similares a un K * log2(K).
    
      ![D&C var-K plot (1)](/plots/2023-04-23_23-33-06/plot.png "2023-04-23_23-33-06/plot.png")
      
      Una vez más, el gráfico no nos permite afirmar que los resultados volcados en el gráfico se correspondan de alguna manera con una proporción lineal o logarítmica, es por eso que recurriremos nuevamente al gráfico de pendientes.

---

4. En caso que la complejidad obtenida en el punto 1 no se condiga con la realidad, indicar por qué (qué condición falla). En dicho caso, se requiere llegar a la complejidad correcta (no solamente enunciarla, sino demostrar cuál es).
5. Indicar cualquier conclusión adicional que les parezca relevante en base a lo analizado.
