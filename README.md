# Trabajo Práctico 1: Técnicas de Diseño

## Primera Parte: Problema de K-merge por División y Conquista

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
2. Describir el algoritmo que utiliza heaps, y determinar su complejidad.

    A continuación se enuncia el algoritmo y en simultáneo se va detallando la complejidad de cada operación. El K-merge con heaps trabaja tomando primero el primer elemento de cada uno de los K arreglos ordenados e insertándolos en un heap de mínimos (O(K)), que servirá posteriormente para ir siempre sabiendo cuál es el elemento de valor más chico y así ir construyendo el arreglo final.

    ¿Cómo logramos esto? Para empezar, no se guarda simplemente el valor del arreglo, sino que también se guarda el número del arreglo al que pertenece y el índice dentro de ese arreglo (en este caso, se realizó implementando una sencilla clase que solo tuviera estos 3 atributos). La importancia de esto es que se utilizará para en un loop ir desencolando del heap el elemento más pequeño, agregándolo al arreglo final y encolando el siguiente elemento (si lo hubiera) del arreglo al que pertenecía el elemento que se desencoló. Esto sucederá hasta que el heap no tenga más elementos, que a su vez solo sucederá una vez que cada uno de los h elementos de cada uno de los K arreglos hayan pasado por el heap (es decir, se hayan encolado, agregado al arreglo final y luego desencolado).

    Debido a que las operaciones de encolar y desencolar dentro del loop se realizan en O(log(K)) (estrictamente sería O(log(K)) + O(log(K)) porque son dos operaciones por cada iteración) y esto se realizará por la cantidad total de elementos, como indica la consigna, n = K * h), las operaciones del loop se realizan en O(n * log(K)).

    Como O(n * log(K)) es mayor que O(K) ya que n = K * h, entonces la complejidad del algoritmo es O(n * log(K)).

3. Implementar ambos algoritmos, y hacer mediciones (y gráficos) que permitan entender si las complejidades obtenidas
para cada uno se condicen con la realidad.
4. En caso que la complejidad obtenida en el punto 1 no se condiga con la realidad, indicar por qué (qué condición falla).
En dicho caso, se requiere llegar a la complejidad correcta (no solamente enunciarla, sino demostrar cuál es).
5. Indicar cualquier conclusión adicional que les parezca relevante en base a lo analizado.
