# SlashMobilityTest
 # Test de IA para SlashMobility, predicción de diabetes

 ## Introducción

 API de predicción simple montada con Flask y documentada con Swagger para SlashMobility. Esta aplicación trabaja sobre un dataset relacionado con pacientes indios cuyo objetivo es averiguar si mediante las features como la presión arterial, la edad, los pliegues de la piel, etc. se puede observar si dicho tiene diabetes

 ## Dependencias y ejecución de la aplicación

 Las dependencias de este proyecto se encuentran en el archivo requirements.txt generado gracias al paquete pipreqs\

 **1** - Al hacer pip install (nombre del paquete) para todos los paquetes del .txt, tanto si estamos en un entorno virtual como en el general, procedemos a ejecutar App.py (python -u ruta/al/archivo/App.py)\
 (podemos tanto correr la aplicación directamente como asignar la variable FLASK_APP y especificar qué programa queremos ejecutar al correr flask run, que en este caso siempre será App.py)\
 **2** - La aplicación está configurada para correr en esta dirección : http://localhost:5000/ , donde vemos todas las rutas disponibles mediante la interfaz de Swagger, aquí podemos ejecutar las pruebas que queramos

 ## Funcionalidades

 Esta API tiene dos funcionalidades:

**1**- mediante **getPrediction**, a partir de unas features que se pasan en el cuerpo del JSON, se retornan las posibles clases predecidas
con su correspondiente probabilidad asociada.\
**2**- A través de **validatePrediction** y las features + label de la predicción anterior se envía a reentrenar al modelo previamente guardado para no tener que reentrenarlo
cada vez y los nuevos datos se guardan.

## Explicación del método de resolución

Para solventar el problema que se nos presenta, se ha requerido del clasificador DecisionTree que implementa a lo que llamamos un modelo basado en árboles de decisión. Este modelo obtenido entrenado a partir de los datos de los pacientes tiene un Accuracy de apróximadamente un 70%, lo cual es bastante aceptable. De hiperparámetros se ha visto que los que vienen por defecto son los más acertados. En la instanciación del clasificador vemos que por defecto usamos un splitter óptimo.


