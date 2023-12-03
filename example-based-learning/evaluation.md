Zeroshot (GPT)
    ASP
    - A.1.1: ACCEPTABLE. razonamiento válido, aplicando bien la lógica. Pero describe reglas ASP que no tienen forma de automatización.
    - A.1.2: FAIL. El resultado no es algo directamente ejecutable, y tampoco aplica bien la lógica. Tiene dos reglas para encender la luz con diferentes condiciones, una que considera solo la ocupación y otra que considera ocupación y nivel de luz (quedando anulada por la primera). Además, incluye una restricción que no tiene sentido: que no es posible que suceda al mismo tiempo que la lámpara esté encendida, que haya ocupación y que el nivel de luz sea alto.
    - A.1.3: FAIL. El resultado no es algo directamente ejecutable, y tampoco aplica bien la lógica de la propuesta, ya que las reglas de encendido y apagado de la luz no tienen en cuenta la luz natural que puede estar pasando a través de la ventana (a pesar de incluir reglas que levantan la persiana cuando se hace de día).

    HA
    - A.1.1: OK. Razonamiento válido, aplicando bien la lógica. La automatización generada es correcta: si se detecta ocupación, se enciende la luz, y esta permanece encendida durante 5 minutos; si a los cinco minutos no se detecta ocupación, se apaga. No es la automatización más eficiente, pero es correcta. (VALIDACIÓN: ESTADOS INVENTADOS: occupied)
    - A.1.2: ACCEPTABLE. La automatización de encender la luz solamente tiene la ocupación como trigger y el nivel de luz bajo como condición. Esto hace que si hay alguien en una habitación y se hace de noche, no se encienda la luz. Esto es aceptable, pero hay alternativas mejores.
    - A.1.3: FAIL. Las reglas de encendido y apagado de la luz solo consideran la ocupación, y las cortinas se abren cuando el espacio está ocupado y es de día, y se cierran cuando es de noche. Además añade una regña para encender la luz a las seis de la tarde.

    - B.1: ACCEPTABLE. Genera reglas que permiten encender la luz de un espacio para iluminar otro en base a un estado 'fail' de la luz principal que había disponible en este. El resultado es correcto en este caso. En cambio, para apagar la luz solamente tiene en cuenta la ocupación del espacio que se desea iluminar, sin tener en cuenta si hay alguien o no en el espacio que tiene la fuente de luz. Si alguien sale del espacio objetivo y había alguien en el espacio de la fuente de luz, este último se quedará a oscuras. Se considera aceptable por las explicaciones que acompañan la respuesta, de sentido común, aunque se queden cortas. Además, provee las reglas de iluminación normal.
    - B.2: FAIL. Considera que hya que buscar luz alternativa si la lámpara está apagada (no en un estado como roto, o fuera de servicio). Basarse en eso no tiene sentido, ya que la lámpara puede estar apagada porque no hay nadie en el espacio, o porque no es necesario iluminar el espacio.
    - B.3: FAIL. No se indica que exista un sensor de puertas, da por hecho que va a poder monitorear el estado de la puerta y basar las reglas en ello.

Few-shot (GPT)
    ASP
    - A.1.1: ?. Asume que puede emplear el sensor de luz de la cocina en la decisión de encender la luz. No es correcto porque la cocina y el salón son espacios separados.
    - A.1.2: OK
    - A.1.3: FAIL. Genera reglas sin mucho sentido. COnsidera como trigger/condición para encender la luz que la cortinas estén abiertas, independientemente de la hora del día. Además, basa la apertura de la cortina en que esta esté abierta.

    HA
    - A.1.1: ?. Asume que puede emplear el sensor de luz de la cocina en la decisión de encender la luz. No es correcto porque la cocina y el salón son espacios separados.
    - A.1.2: ACCEPTABLE. Define bien las reglas de encendido y de apagado de la luz, pero añade una tercera regla para encender la luz con los mismos criterios que la primera regla pero, además, que sea de noche. Esta regla es inútil (TODO: VALIDACIÓN, comprobación de acciones redundantes).
    - A.1.3: FAIL. Si hay ocupación enciende la luz, y si no, la apaga. Abre la persiana si hay ocupación y es de día, y la cierra si no hay ocupación y es de noche. Esto puede tener sentido en algún caso por preferencias de usuario, pero no es generalizable y, desde luego, no aprovecha la luz natural que pueda entrar por la ventana.

    - B.1: OK
    - B.2: OK
    - B.3:

Few-shot-exp
    GPT
        TEXT
            ASP
            - A.1.1: OK
            - A.1.2: OK
            - A.1.3: OK

            HA
            - A.1.1: OK
            - A.1.2: OK
            - A.1.3: FAIL. Si hay ocupación enciende la luz, y si no, la apaga. Abre la persiana si hay ocupación y es de día, y la cierra si no hay ocupación y es de noche. Esto puede tener sentido en algún caso por preferencias de usuario, pero no es generalizable y, desde luego, no aprovecha la luz natural que pueda entrar por la ventana.

            - B.1: OK
            - B.2: OK
            - B.3:

        STRUCTURED
            ASP
            - A.1.1: OK
            - A.1.2: ACCEPTABLE. Define las reglas esperadas, pero añade una regla redundante que enciende la luz si hay ocupación, hay poca luz y la puerta está abierta. El resultado es el esperado, pero sobran reglas (TODO: VALIDACIÓN, comprobación de acciones redundantes)
      ------- A.1.3: OK. Genera las reglas esperadas y una adicional que enciende la luz, aunque sea de día, las cortinas estén abiertas y haya ocupación, si el nivel de luz de la cocina es bajo. Asumen que tomar el nivel de luz de la cocina, donde hay una ventana, es válido porque son habitaciones que están en el mismo edificio.

            HA
            - A.1.1: OK
            - A.1.2: FAIL. Define las reglas esperadas, pero añade una regla que apaga la luz si el nivel de luz es suficiente, lo que puede dar lugar a un bucle de encendido y apagado de la luz (TODO: VALIDACIÓN, comprobación de estados incompatibles)

            - B.1: OK
            - B.2: OK
            - B.3:
    PaLM
        TEXT
            ASP
            - A.1.1: FAIL. Basa el encendido de la luz en el momento del día, encendiendo la luz solamente si hay presencia y es de noche (esto podría tener sentido si hubiese ventanas, pero no es el caso).
            - A.1.2: OK
            - A.1.3: ACCEPTABLE. Define las reglas casi de la forma esperada. Mientras que las reglas generadas por GPT4 permiten que, si hay una persona en una habitación y se hace de día, se pueda apagar la luz y abrir la persiana aunque el nivel de luz en ese momento fuese adecuado, las reglas generadas por PaLM no permiten que se apague la luz y se abra la persiana si el nivel de luz es suficiente. La solución de GPT4 es más completa.

            HA
            - A.1.1: OK
            - A.1.2: OK
            - A.1.3: FAIL. Asume que puede medir el nivel de luz en la estancia con un sensor que no existe.

            - B.1: OK
            - B.2: OK
            - B.3:

        STRUCTURED
            ASP
            - A.1.1: FAIL. Solamente enciende la luz si hay presencia de noche. Tendría sentido si hubiese ventanas, pero no es el caso.
            - A.1.2: OK
            - A.1.3: FAIL. Si hay ocupación y es de noche, enciende la luz, y si no hay nadie (independientemente del momento del día), la apaga. Abre la persiana si hay ocupación y es de día, y la cierra si no hay ocupación y es de noche. Esto tiene cierto nivel de validez, ya que solamente se enciende la luz de noche, y se levanta la persiana de día. ¿pero qué pasa si ya hay alguien en la habitación cuando se hace de día?

            HA
            - A.1.1: ACCEPTABLE. Utiliza como condición el trigger, cosa que no tiene sentido ya que si la condición se evalúa es porque el trigger sucede.

            - B.1: OK
            - B.2: OK
            - B.3:
