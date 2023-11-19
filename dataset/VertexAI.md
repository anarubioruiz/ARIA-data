Herramientas de Google Cloud
- Generative AI Studio: prueba y personaliza grandes modelos de lenguaje y generativos de imágenes.
  "Prueba, ajusta e implementa modelos de lenguaje de IA generativa. Accede a la API de PaLM para Chat si quieres generar código o contenido, chatear, resumir contenido y mucho más."
  "Tune a model so it’s better equipped for your use case, then deploy to an endpoint to get predictions or test it in prompt design"

- Sube un conjunto de datos de ajuste a Cloud Storage (opcional)
  El ajuste requiere que tus datos se almacenen en Cloud Storage. Para subir tu conjunto de datos de ajuste de modelos a un bucket de Cloud Storage, realiza los siguientes pasos.

- Configuración del modelo
  1. Selecciona Archivo JSONL existente en Cloud Storage.
     GCS file path: Ingresa el URI del archivo de conjunto de datos que subiste a Cloud Storage. También puedes usar un conjunto de datos de muestra que pusimos a disposición para este instructivo.
  2. Configura los detalles del modelo
     - Nombre del modelo: Ingresa un nombre para el modelo ajustado.
     - Modelo base: Selecciona el modelo base que deseas ajustar.
     - Pasos de entrenamiento: Ingresa la cantidad de pasos que se ejecutarán para el ajuste del modelo. 1,000 pasos tardarás entre 2 y 3 horas en completar el ajuste.
     - Tasa de aprendizaje: Controla el tamaño del paso en el que un modelo actualiza sus pesos durante el entrenamiento. Predeterminado: 3.
     - Directorio de trabajo: ingresa el URI del bucket para almacenar el modelo ajustado. Si no tienes uno, puedes crear un bucket nuevo.

- Prueba el modelo
  Para verificar el estado de tu trabajo de ajuste de modelo, ve a la página Canalizaciones. El estado de tu canalización se puede encontrar en la sección Runs.

  Para ver tus modelos ajustados en la consola de Google Cloud, ve a la página Registro de modelos de Vertex AI.


## Parámetros para el ajuste
- Nombre del modelo: ARIA-text
- Tipo de ajuste: supervisado
- Modelo base: text-bison@001
- Pasos de entrenamiento: X (es complicado definir los pasos de entrenamiento sin conocer el batch size. Otros usuarios de la comunidad, tras hacer algunas pruebas, comentan que es probable que el tamaño de batch sea 64. En este sentido, cogiendo nuestro dataset y dividiéndolo por 64, podemos establecer qué paso de entrenamiento se necesitan para cada época (epoch, 3-5) ¿50?)
- Multiplicador de tasa de aprendizaje: 1. Normalmente se define entre 3 y 5. Esto es un multiplicador del ratio, pero no sabemos cuál es este ratio.
- Tipo de acelerador: TPU 64x cores de una TPU v3
