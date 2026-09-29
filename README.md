# Del ADN a la proteína

## Bioinformática

Práctica centrada en el estudio del flujo de la información genética desde el ADN hasta la proteína mediante procesos de **replicación, transcripción y traducción**, utilizando Python y la biblioteca **Biopython**.

El proyecto también aborda el splicing alternativo, la relación entre secuencia, estructura y función de las proteínas y el uso de bases de datos bioinformáticas públicas.

---

## Estructura del proyecto

```text
ADN-a-Proteina/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── ejercicio2.fasta
│   └── secuencia.fasta
│
└── src/
    ├── ejercicio1.py
    ├── ejercicio2.py
    ├── ejercicio3.py
    ├── ejercicio4.py
    ├── ejercicio5.py
    └── pipeline.py
```

La principal dependencia utilizada es:

```text
biopython
```

---

# Ejercicio 1. Replicación del ADN

La secuencia inicial proporcionada es:

```text
5' - ATG CCG TTA GCT - 3'
3' - TAC GGC AAT CGA - 5'
```

La replicación del ADN es **semiconservativa**, lo que significa que cada una de las moléculas resultantes conserva una hebra de la molécula original y contiene una hebra nueva.

Tras una ronda de replicación se obtienen:

### Molécula 1

```text
5' - ATG CCG TTA GCT - 3'   Hebra original
3' - TAC GGC AAT CGA - 5'   Hebra nueva
```

### Molécula 2

```text
3' - TAC GGC AAT CGA - 5'   Hebra original
5' - ATG CCG TTA GCT - 3'   Hebra nueva
```

## Enzimas implicadas

- **Helicasa:** separa las dos hebras del ADN rompiendo los puentes de hidrógeno entre las bases complementarias.
- **Primasa:** sintetiza pequeños cebadores de ARN que permiten comenzar la síntesis de ADN.
- **ADN polimerasa:** incorpora nucleótidos complementarios y sintetiza las nuevas hebras de ADN en dirección 5' → 3'.
- **Ligasa:** une los fragmentos de ADN, especialmente los fragmentos de Okazaki de la hebra retardada.

## Error de la ADN polimerasa

Si la ADN polimerasa incorporara una base incorrecta y el error no fuese corregido, este podría quedar fijado como una **mutación**.

Dependiendo de la posición y del tipo de mutación, podría modificarse posteriormente el ARNm y la secuencia de aminoácidos de una proteína. Sin embargo, no todas las mutaciones producen necesariamente un cambio funcional.

## Biopython

El programa correspondiente se encuentra en:

```text
src/ejercicio1.py
```

Se utiliza:

```python
Seq.complement()
```

para generar automáticamente la hebra complementaria. El resultado obtenido coincide con el calculado manualmente.

---

# Ejercicio 2. Transcripción del ADN a ARN

La secuencia inicial es:

```text
5' - ATG CCT GAA TGC - 3'
3' - TAC GGA CTT ACG - 5'
```

La **cadena molde** es:

```text
3' - TAC GGA CTT ACG - 5'
```

La ARN polimerasa lee esta hebra en dirección 3' → 5' y sintetiza el ARN en dirección 5' → 3'.

El ARNm obtenido es:

```text
5' - AUG CCU GAA UGC - 3'
```

En el ARN se utiliza **uracilo (U)** en lugar de timina (T).

## Región promotora

La región promotora es una región del ADN situada antes de la región que será transcrita. En ella se unen la ARN polimerasa y otros factores necesarios para iniciar la transcripción.

En la secuencia corta proporcionada en el ejercicio no se especifica una secuencia promotora concreta.

## Región codificante

La región codificante contiene la información genética que puede dar lugar, después de la transcripción y traducción, a una secuencia de aminoácidos.

## Lectura de FASTA con Biopython

El archivo:

```text
data/ejercicio2.fasta
```

contiene la secuencia:

```text
>Ejercicio2_ADN
ATGCCTGAATGC
```

El programa:

```text
src/ejercicio2.py
```

lee este archivo con:

```python
SeqIO.read()
```

y posteriormente obtiene el ARNm mediante:

```python
Seq.transcribe()
```

También se cambia la orientación de la secuencia mediante `reverse_complement()` para comprobar que una orientación diferente produce un ARN diferente.

---

# Ejercicio 3. Traducción del ARNm a proteína

El ARNm proporcionado es:

```text
5' - AUG UAU GCU UAA - 3'
```

Separándolo en codones:

```text
AUG | UAU | GCU | UAA
```

se obtiene:

| Codón | Significado |
|---|---|
| AUG | Metionina (Met) e inicio |
| UAU | Tirosina (Tyr) |
| GCU | Alanina (Ala) |
| UAA | STOP |

Por tanto, la cadena de aminoácidos es:

```text
Met - Tyr - Ala
```

## Mutación del codón de inicio

Si el codón de inicio cambiara de:

```text
AUG → GUG
```

podría reducirse o impedirse el inicio normal de la traducción en ese punto. El efecto concreto dependería del contexto de la secuencia y de la existencia de otros posibles sitios de inicio.

## Desaparición del codón de parada

Si desapareciera el codón de parada, el ribosoma podría continuar traduciendo el ARNm hasta encontrar otro codón de terminación.

Esto podría generar una proteína más larga de lo normal y alterar su estructura o función.

## Biopython

El programa:

```text
src/ejercicio3.py
```

utiliza:

```python
Seq.translate()
```

y obtiene:

```text
MYA*
```

donde:

```text
M = Metionina
Y = Tirosina
A = Alanina
* = STOP
```

El resultado coincide con la traducción realizada manualmente.

---

# Ejercicio 4. Splicing alternativo

Se considera inicialmente un gen formado por cinco exones:

```text
Exón 1 - Exón 2 - Exón 3 - Exón 4 - Exón 5
```

Se proponen dos posibles formas de splicing alternativo.

### Isoforma 1

```text
Exón 1 - Exón 2 - Exón 4 - Exón 5
```

En esta combinación se elimina el exón 3.

### Isoforma 2

```text
Exón 1 - Exón 3 - Exón 5
```

En este caso se eliminan los exones 2 y 4.

Estas combinaciones producen ARNm diferentes y, como consecuencia, pueden generar proteínas con diferentes secuencias de aminoácidos, longitudes, estructuras o funciones.

El **splicing alternativo** aumenta la diversidad proteica porque permite producir distintos transcritos a partir de un mismo gen, sin necesidad de aumentar el número de genes.

El ejemplo se implementa en:

```text
src/ejercicio4.py
```

## Ejemplo real: FGFR2

Como ejemplo real se consultó el gen humano **FGFR2 (fibroblast growth factor receptor 2)** en Ensembl.

FGFR2 presenta diferentes transcritos producidos mediante procesamiento alternativo del ARN. Entre ellos pueden encontrarse transcritos que generan proteínas de distinta longitud.

Por ejemplo, Ensembl recoge transcritos codificantes de FGFR2 que producen proteínas de aproximadamente:

```text
821 aminoácidos
707 aminoácidos
```

La existencia de transcritos diferentes implica que la combinación de exones utilizada no es siempre la misma. Estas diferencias pueden modificar la secuencia y las regiones presentes en la proteína y, como consecuencia, afectar a sus propiedades y función.

Fuente consultada: **Ensembl, gen FGFR2 (ENSG00000066468).**

---

# Ejercicio 5. Introducción a las proteínas

La secuencia de aminoácidos proporcionada es:

```text
Met - Ile - Ser - Gly - Val - Lys - His
```

El extremo inicial de la proteína es el **extremo N-terminal**, por lo que en esta secuencia corresponde a:

```text
Met
```

El extremo final es el **extremo C-terminal**, correspondiente a:

```text
His
```

Por tanto:

```text
N-terminal                               C-terminal
     ↓                                        ↓
    Met - Ile - Ser - Gly - Val - Lys - His
```

## Relación entre secuencia, estructura y función

El orden de los aminoácidos constituye la estructura primaria de la proteína y condiciona las interacciones que se producen entre sus diferentes regiones.

Estas interacciones permiten que la proteína adopte una determinada estructura tridimensional. Como la función de una proteína depende en gran medida de su estructura, cambios en su secuencia pueden afectar también a su función.

## Mutación de un aminoácido

Si un aminoácido hidrofóbico situado en una región interna de la proteína fuera sustituido por uno hidrofílico, podrían alterarse las interacciones que estabilizan su estructura.

Esto podría:

- modificar el plegamiento;
- reducir la estabilidad de la proteína;
- alterar su estructura tridimensional;
- afectar a su función.

El análisis básico se encuentra en:

```text
src/ejercicio5.py
```

## Ejemplo en Protein Data Bank

Se consultó la estructura **1UBQ**, correspondiente a ubiquitina humana, disponible en el Protein Data Bank.

La estructura fue determinada mediante difracción de rayos X con una resolución de 1,8 Å.

En ella pueden observarse diferentes elementos de estructura secundaria, incluyendo:

- una hélice alfa;
- una pequeña hélice 3₁₀;
- una lámina beta formada por cinco hebras;
- varios giros.

La proteína también presenta un núcleo hidrofóbico relacionado con la estabilización de su estructura tridimensional.

Una mutación puntual que modificara las propiedades de uno de los aminoácidos implicados en estas interacciones podría alterar la estabilidad o el plegamiento de la proteína.

Fuente consultada: **RCSB Protein Data Bank, estructura 1UBQ.**

---

# Ejercicio 6. Actividad integradora: del ADN a la proteína

El último ejercicio integra los procesos estudiados anteriormente:

```text
ADN
 ↓
Replicación
 ↓
Transcripción
 ↓
ARNm
 ↓
Traducción
 ↓
Proteína
```

El programa completo se encuentra en:

```text
src/pipeline.py
```

## Secuencia utilizada

Se utiliza una secuencia correspondiente al comienzo de la región codificante del gen humano **HBB**, que codifica la subunidad beta de la hemoglobina.

La referencia pública utilizada es:

```text
HBB - Homo sapiens
RefSeq: NM_000518.5
```

La secuencia utilizada en el ejercicio se almacena en:

```text
data/secuencia.fasta
```

con formato FASTA.

El fragmento utilizado comienza:

```text
ATGGTGCACCTGACTCCTGAGGAGAAGTCT...
```

La referencia NM_000518.5 se encuentra en la base de datos pública **NCBI**.

## Lectura de la secuencia

El pipeline comienza leyendo el archivo FASTA mediante:

```python
SeqIO.read()
```

La secuencia obtenida se almacena como una secuencia de ADN sobre la que se realizan los siguientes procesos.

---

## Paso 1. Replicación

El programa obtiene la hebra complementaria mediante:

```python
adn.complement()
```

A partir de:

```text
5' - ADN original - 3'
```

se obtiene:

```text
3' - ADN complementario - 5'
```

La replicación se considera semiconservativa, de manera que cada nueva molécula contiene una hebra original y otra de nueva síntesis.

---

## Paso 2. Transcripción

La hebra complementaria representa la hebra molde correspondiente al ADN codificante utilizado.

El programa transforma la secuencia codificante en ARNm mediante:

```python
adn.transcribe()
```

Durante este proceso, las timinas del ADN se sustituyen por uracilos en el ARN.

Por ejemplo:

```text
ADN:  ATG
ARNm: AUG
```

---

## Paso 3. Traducción

El ARNm se interpreta en grupos de tres nucleótidos llamados **codones**.

Antes de realizar la traducción, el programa comprueba si la longitud de la secuencia es múltiplo de tres.

Si el fragmento termina con uno o dos nucleótidos que no forman un codón completo, estos no se incluyen en la traducción.

La proteína se obtiene mediante:

```python
arnm_traducible.translate()
```

En la secuencia utilizada, el inicio de la proteína obtenida es:

```text
MVHLTPEEKSAVTALWGKVNVDEVGGEALG
```

---

## Reflexión sobre los errores

Los errores que modifican de forma estable la secuencia del ADN pueden afectar a las etapas posteriores del flujo de información genética.

Una mutación localizada en una región codificante puede:

```text
Modificar el ADN
        ↓
Modificar un codón del ARNm
        ↓
Cambiar un aminoácido
        ↓
Alterar potencialmente la estructura o función de la proteína
```

Sin embargo, el efecto depende del tipo y posición de la mutación. Algunas mutaciones pueden no modificar el aminoácido producido, mientras que otras pueden generar cambios importantes, como la sustitución de un aminoácido o la aparición de un codón de parada prematuro.

Por ello, los errores permanentes en el ADN son especialmente relevantes, ya que pueden propagarse a los productos generados posteriormente.

---

# Pipeline completo

El pipeline implementado realiza automáticamente:

```text
Archivo FASTA
      ↓
Lectura de ADN
      ↓
Replicación
      ↓
Hebra complementaria
      ↓
Transcripción
      ↓
ARNm
      ↓
Traducción
      ↓
Proteína
```

Durante su ejecución, el programa muestra información sobre cada uno de los procesos y las secuencias que se van generando.

Para ejecutarlo desde la carpeta principal del proyecto:

```bash
python3 src/pipeline.py
```

---

# Conclusiones

La práctica permite recorrer computacionalmente las principales etapas del flujo de información genética.

Biopython facilita operaciones habituales en bioinformática como:

```python
Seq.complement()
Seq.reverse_complement()
Seq.transcribe()
Seq.translate()
SeqIO.read()
```

Los resultados obtenidos mediante los programas coinciden con los procesos realizados manualmente y muestran cómo las herramientas bioinformáticas permiten automatizar el tratamiento y análisis de secuencias biológicas.

Además, la consulta de bases de datos como **NCBI, Ensembl y Protein Data Bank** permite relacionar los conceptos estudiados con secuencias, genes y estructuras biológicas reales.

---

## Recursos utilizados

- **Biopython** — tratamiento de secuencias biológicas en Python.
- **NCBI** — secuencia de referencia del gen humano HBB, NM_000518.5.
- **Ensembl** — consulta de transcritos e isoformas del gen FGFR2.
- **RCSB Protein Data Bank** — estructura tridimensional 1UBQ de ubiquitina humana.