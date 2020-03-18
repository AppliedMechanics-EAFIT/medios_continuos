# Mecánica de los medios continuos

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AppliedMechanics-EAFIT/medios_continuos/master)

## Introducción
Este repositorio contiene recursos de aprendizaje para el curso **Mecánica de los Medios Continuos** dictado a estudiantes de segundo año (4to semestre) del programa de Ingeniería Civil de la Universidad EAFIT. El curso cubre la teoría de los medios deformables partiendo del planteamiento del problema de muchas particulas hasta introducir los conceptos de tensor de tensiones, tensor de deformaciones unitarias y discutir las ecuaciones de equilibrio para un sólido elástico.

Los archivos almacenados en este repositorio se pueden descargar directamente o clonar el repo como se describe mas adelante. El repo contiene algunos ejemplos descritos en térmnos de Notebooks de [Jupyter](http://jupyter.org/).

## Contenido

- Notas de clase, con los archivos fuente y el documento en
  [pdf](https://github.com/AppliedMechanics-EAFIT/Notas-MMC/raw/master/notas_de_clase/notas_medios.pdf).

- Notebooks de [Jupyter](http://jupyter.org/) con ejercicios.

- Actividad

## Actividad usando computación (2020-01)

* [Determinación de la respuesta de una presa de concreto](https://nbviewer.jupyter.org/github/AppliedMechanics-EAFIT/medios_continuos/blob/master/actividades/presa/01_solidspy_dam_design.ipynb)



## Descarga del material

Se puede clonar el repositorio usando:

    git clone https://github.com/nicoguaro/medios.git

o directamente usar la opción de descarga desde GitHub.

## Instrucciones de instalación

Para correr los notebooks de Jupyter, es necesario [Python](https://www.python.org/)
y algunos paquetes:

- [IPython](http://ipython.org/), un shell interactivo que añade funcionalidades
 extra al modo interactivo incluido con Python, como resaltado de líneas y
errores mediante colores, una sintaxis adicional para el shell, autocompletado
mediante tabulador de variables, módulos y atributos; entre otras funcionalidades.
- [NumPy](http://www.numpy.org/), una extensión de Python, que le agrega mayor
soporte para vectores y matrices, constituyendo una biblioteca de funciones
matemáticas de alto nivel para operar con esos vectores o matrices.
- [SciPy](http://www.scipy.org/), una biblioteca de herramientas y algoritmos
matemáticos para Python
- [matplotlib](http://matplotlib.org/),  una biblioteca para la generación de
gráficos a partir de datos contenidos en listas o arrays en el lenguaje de
programación Python y su extensión matemática NumPy.

y el [Sistema de Álgebra por computadora (CAS)](https://en.wikipedia.org/wiki/Computer_algebra_system) [Sympy](http://www.sympy.org/).

El método sugerido es usar una distribución de Python, preferiblemente
 [Anaconda](https://www.continuum.io/downloads). Esta incluye todos los paquetes
mencionados arriba.

## Licencia

El contenido de este repositorio está licenciado bajo una licencia
[Creative Commons Attribution 4.0](http://choosealicense.com/licenses/cc-by-4.0/),
y el código fuente que le acompaña bajo una
[licencia MIT](https://opensource.org/licenses/mit-license.php).

## Citación

Para citar estas notas de clase use

> Juan Gómez, César Augusto Sierra, Juan Carlos Vergara,
  Mario Sáenz, y Nicolás Guarín-Zapata (2018).
  Notas de clase: Mecánica del medio continuo. Universidad EAFIT,
  Disponible en: https://github.com/AppliedMechanics-EAFIT/Notas-MMC.

Una entrada de BibTeX para los usuarios de LaTeX es

    @misc{notas_medios,
     title = {Notas de clase: Mecánica del medio continuo},
     author = {Gómez, Juan and Sierra, César Augusto and
               Vergara, Juan Carlos and Mario Sáez and
               Guarín-Zapata, Nicolás},
     year = {2018},
     keywords = {Mecánica del medio continuo, Elasticidad, Python,
                Mecánica computacional},
     publisher = {Universidad EAFIT},
     url = {https://github.com/AppliedMechanics-EAFIT/Notas-MMC}
    }
