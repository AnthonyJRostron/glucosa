# README — Diario de Diabetes

---

> ## ⚠️ AVISO IMPORTANTE — LEE ESTO ANTES DE USAR LA APP
>
> **Esta aplicación NO diagnostica, NO prescribe y NO recomienda tratamientos de insulina ni de ningún otro fármaco.**
>
> La app es únicamente una **herramienta de registro y visualización** de los datos que tú introduces. **Solo un profesional sanitario cualificado** (endocrino, educador en diabetes, enfermería especializada o médico de familia) puede diagnosticar, ajustar dosis, cambiar pautas o recomendar tratamientos.
>
> **Esta app debe haberte sido facilitada por una clínica o unidad de diabetes acreditada.** Esa clínica tiene acceso a herramientas adicionales para **revisar y corregir tus datos** (por ejemplo, si olvidaste registrar un medicamento, si una dosis quedó mal anotada o si un ajuste de pauta no se reflejó correctamente). No dudes en ponerte en contacto con ella para cualquier corrección.
>
> **Nunca modifiques tu tratamiento por tu cuenta basándote únicamente en lo que veas en la app.** Si tienes dudas sobre tus glucemias, tus dosis o tus patrones, contacta con tu equipo de diabetes.
>
> **Se recomienda volver a la consulta con la periodicidad que te indique tu equipo sanitario.** Como orientación general, la mayoría de guías clínicas recomiendan **revisión cada 3 meses** para personas con diabetes tipo 1 o tipo 2 insulinizadas, y **cada 6–12 meses** para personas con diabetes tipo 2 no insulinizadas o bien controladas. **La frecuencia exacta la decide tu profesional sanitario.** Lleva siempre el informe PDF o el archivo JSON de la app a cada revisión.

---

## Índice

1. [Descripción general](#1-descripción-general)
2. [Inicio rápido para pacientes](#2-inicio-rápido-para-pacientes)
3. [Requisitos técnicos](#3-requisitos-técnicos)
4. [Primera configuración: qué debe introducir el paciente](#4-primera-configuración-qué-debe-introducir-el-paciente)
5. [Panel de configuración colapsable](#5-panel-de-configuración-colapsable)
6. [Cómo añadir, editar y eliminar registros](#6-cómo-añadir-editar-y-eliminar-registros)
7. [Sistemas que garantizan la correcta introducción de datos](#7-sistemas-que-garantizan-la-correcta-introducción-de-datos)
8. [Explicación detallada de cada sección](#8-explicación-detallada-de-cada-sección)
9. [Para profesionales sanitarios: datos de ejemplo](#9-para-profesionales-sanitarios-datos-de-ejemplo-diabetesjson)
10. [Videollamada con el profesional sanitario](#10-videollamada-con-el-profesional-sanitario)
11. [Alta de médicos y ajustes de la clínica](#11-alta-de-médicos-y-ajustes-de-la-clínica)
12. [Privacidad, seguridad y cumplimiento](#12-privacidad-seguridad-y-cumplimiento)
13. [Preguntas frecuentes (FAQ)](#13-preguntas-frecuentes-faq)
14. [Solución de problemas](#14-solución-de-problemas)
15. [Glosario](#15-glosario)
16. [Anexo A: esquema del archivo JSON](#16-anexo-a-esquema-del-archivo-json)
17. [Anexo B: valores admitidos en campos cerrados](#17-anexo-b-valores-admitidos-en-campos-cerrados)

---

## 1. Descripción general

**Diario de Diabetes** es una aplicación autocontenida en un único archivo, sin instalación y sin servidor. Todos los datos que introduces se guardan **localmente en tu propio navegador** y puedes exportarlos o importarlos como un archivo `.json`. Los datos solo salen de tu dispositivo si **tú** decides enviarlos (por email o por videollamada).

La app permite a una persona con diabetes:

- **Registrar cada día** sus glucemias (antes y después de las comidas y por la noche).
- **Registrar la insulina** u otros medicamentos que se inyecta o toma, con dosis, unidad, hora, si la ha omitido y una nota.
- **Anotar el ejercicio** realizado (tipo y duración), el **estado de ánimo** y el **contexto dietético** de cada jornada.
- **Recibir automáticamente** los datos meteorológicos de su localidad (temperatura, humedad, precipitación, presión y viento), que se guardan junto al registro porque influyen en el control glucémico.
- **Consultar resúmenes y estadísticas** de los últimos días, semanas o meses.
- **Generar informes PDF** totalmente configurables para llevar a la consulta.
- **Registrar la presión arterial** (opcional, se activa en el perfil clínico): sistólica, diastólica, pulso y notas.
- **Enviar por email** a la clínica el archivo JSON con sus datos, antes de la consulta.
- **Hacer una videollamada** con su profesional sanitario, con chat y pantalla compartida, y **compartirle sus datos de forma cifrada** durante la llamada. El médico solo puede *verlos* mientras dura la llamada; para que pueda *guardarlos* hace falta un segundo permiso expreso del paciente (ver [sección 10](#10-videollamada-con-el-profesional-sanitario)).

La app también está pensada para que **profesionales sanitarios** (endocrinólogos, educadores en diabetes, enfermería, médicos de familia) puedan revisar informes de sus pacientes, comparar tendencias, atender por videollamada y demostrar el funcionamiento de la herramienta con **datos de ejemplo ficticios** incluidos en el archivo `diabetes.json`.

> Recuerda el aviso del principio: **la app no diagnostica ni recomienda tratamientos**. Solo un profesional sanitario puede hacerlo, y solo la clínica que te proporcionó la app puede corregir tus datos si detectas errores.

---

## 2. Inicio rápido para pacientes

Al abrir la app por primera vez en un navegador sin datos aparece la pantalla **«Antes de empezar»**, que pregunta cómo quieres continuar:

- **Soy paciente** → crea directamente tu propio perfil de paciente (ruta A). **No** se te ofrecen los datos de ejemplo: son solo para uso clínico y formativo.
- **Soy profesional de la salud** → eliges entre **«+ Añadir nuevo paciente»** o **«Ver datos de ejemplo»** (ruta B).

### 2.1 Ruta A — Soy paciente y quiero crear mi diario

1. Pulsa **«Soy paciente»**.
2. Rellena tus **datos personales y clínicos** (nombre, fecha de nacimiento, tipo de diabetes…) y pulsa **«Guardar datos»**. *Sin nombre guardado no podrás compartir tus datos por videollamada.*
3. Añade tus **medicamentos** con la **dosis habitual** y la **hora habitual**.
4. Indica tu **localidad** para que la app descargue la meteorología (o usa **«Usar mi ubicación»**).
5. Empieza a registrar mediciones. Si tu clínica te lo indica, activa **«Monitorizar presión arterial»** en el perfil clínico.

### 2.2 Ruta B — Soy profesional sanitario y quiero explorar con datos de ejemplo

1. Pulsa **«Soy profesional de la salud»** → **«Ver datos de ejemplo»**.
2. Lee la descripción de los **5 pacientes ficticios** y pulsa **«Sí, cargar los 5 pacientes de ejemplo»**. La app carga `diabetes.json` **automáticamente** (debe estar en la misma carpeta que la app); no hay que buscarlo ni seleccionarlo.
3. Las fechas se **desplazan automáticamente** para que el último día del historial coincida con **hoy**.
4. Cuando termines, borra los datos de ejemplo con **«Borrar todo - empezar de nuevo»** antes de usar la app con un paciente real.

### 2.3 ¿Y si ya tengo datos?

Si en este navegador ya existen pacientes, la pantalla «Antes de empezar» **no aparece** y tus datos **nunca se sustituyen** al abrir la app. Si borras todos los pacientes, la pantalla vuelve a aparecer.

### 2.4 Cómo llevar los datos a la consulta (lo más importante)

Tienes **cuatro formas** de entregar tus datos al profesional sanitario:

1. **Videollamada con compartición de datos.** Si tu médico te atiende por vídeo, puedes enviarle tus datos **cifrados** durante la llamada (ver [sección 10](#10-videollamada-con-el-profesional-sanitario)). Es la opción más cómoda para una consulta telemática: no hay que enviar ni adjuntar nada.
2. **Enviar por email antes de la consulta.** Pulsa **«✉️ Enviar por email»** (cabecera). La app genera el archivo JSON con tus datos y usa una de estas dos vías, e **informa siempre de cuál ha usado**:
   - **Compartir con archivo adjunto** (si tu dispositivo lo permite, p. ej. móviles): se abre el panel nativo para compartir el archivo directamente con tu app de correo.
   - **Descarga + correo**: el JSON se guarda en la carpeta de descargas y se abre tu cliente de correo con destinatario, asunto y texto ya rellenados. **Por seguridad, los navegadores no permiten adjuntar archivos automáticamente: tendrás que adjuntar el JSON descargado a mano antes de enviar.**
3. **Informe PDF.** Con **«Imprimir PDF»** puedes generar la *versión para el paciente* (resumen corto, sin DNI ni nº de Seguridad Social) o el *informe clínico* completo (ver [§8.11](#811-panel-de-informes-y-pdf)).
4. **Llevar el JSON en un pendrive o en el propio dispositivo.** Contiene **todos** los datos y la clínica puede cargarlo en sus herramientas.

> **¿Dónde se guardan los archivos exportados?** Los archivos que la app descarga (el JSON del email, **Copia de seguridad**, **Exportar Pacientes**, **Exportar Excel**) van al **directorio de descargas por defecto** del dispositivo (normalmente la carpeta **Descargas**). El PDF se genera en el navegador y solo se guarda si lo indicas en el diálogo de impresión/guardado.

> **Consejo:** si vas a enviar el email, hazlo **al menos 24–48 horas antes** de la consulta.

### 2.5 ¿Con qué frecuencia debo exportar mis datos?

**Exporta tus datos al menos una vez a la semana.** La app guarda los datos en el navegador, y un borrado accidental, un cambio de dispositivo o una limpieza del navegador pueden hacerte perderlo todo. Exportar semanalmente es una red de seguridad sencilla. **Utiliza el botón «Copia de seguridad» de la ficha del paciente.**

> **Importante:** exportar no es lo mismo que enviar los datos a la clínica. Exportar es una **copia de seguridad personal**; el email o la videollamada sirven para **compartir con el profesional sanitario**. Además, **las fichas temporales recibidas por videollamada no se pueden exportar** (ver [sección 10](#10-videollamada-con-el-profesional-sanitario)).

---

## 3. Requisitos técnicos

### 3.1 Requisitos del dispositivo

| Elemento | Mínimo recomendado |
|---|---|
| Navegador | Chrome / Edge 100+, Firefox 100+, Safari 15+ |
| Sistema operativo | Windows 10+, macOS 12+, Linux, Android 9+, iOS 15+ |
| Memoria RAM | 2 GB |
| Almacenamiento libre | ≥ 50 MB |
| **Conexión a internet** | **Necesaria para las librerías de terceros que dibujan las gráficas y que exportan el PDF** |
| JavaScript | Activado (imprescindible) |
| **Videollamada** | Cámara y micrófono, permisos del navegador concedidos y página servida por **HTTPS** (necesario también para el cifrado) |

### 3.2 Requisitos funcionales

- **No requiere instalación**.
- **Requiere conexión a internet** para:
  - Cargar las **librerías de terceros** que dibujan las **gráficas**.
  - Cargar las **librerías de terceros** que generan la **exportación a PDF**.
  - Descargar la **meteorología** (si tienes ubicación configurada).
  - Usar la **videollamada** (ver §10): carga la librería de conexión y usa servidores de terceros para establecer la llamada.
- **No requiere registro ni contraseña.**
- **Compatible con exportación**: puedes descargar todo el diario como archivo `.json`.
- **Generación de PDF en cliente**: el PDF se crea en tu navegador; los datos no se envían a ningún servidor salvo que tú decidas enviarlos por email o por videollamada desde la app.

### 3.3 Limitaciones conocidas

- **Sin internet, las gráficas y el PDF no funcionan.** El registro de glucemias e insulina sí funciona sin conexión, pero no podrás visualizar gráficas ni generar PDF hasta que recuperes la conexión.
- El **almacenamiento local** está vinculado al navegador y al dispositivo. Si borras los datos del navegador, pierdes el diario. **Exporta semanalmente.**
- **Capacidad limitada.** El navegador reserva unos **5 MB** para la app, y todos los datos comparten ese espacio. Como orientación (estimación, varía según las notas y el uso):
  - Un **paciente con una lectura al día** ocupa unos **0,35 MB al año** → caben unos **10 pacientes con un año de datos**.
  - Con **3 o 4 lecturas al día** ocupa **0,9–1,4 MB al año** → caben **3–4 pacientes-año**.
  - Un paciente que usa la app a diario durante varios años puede llenar el espacio (unos **4 años** con 3 lecturas al día): **exporta y archiva** los años antiguos.
  - Cuanto más se llena, más lenta puede notarse la app, sobre todo en móviles.
  - Si aparece **«almacenamiento lleno»**, exporta una copia de seguridad y borra registros antiguos.
  - **Un médico que guarda fichas** de pacientes recibidas por videollamada comparte este mismo límite: es adecuado para unos pocos pacientes, no como archivo de toda una clínica.
- El **modo incógnito** no conserva los datos al cerrar la ventana.
- La **meteorología** requiere conexión en el momento de consultar; si no hay conexión, el registro se guarda con los campos meteorológicos vacíos.
- Los **PDF** se generan con el motor de impresión del navegador. Si el PDF sale con saltos raros, revisa los márgenes de impresión.

---

## 4. Primera configuración: qué debe introducir el paciente

La primera vez que se abre la app, el diario está vacío. Antes de registrar nada conviene rellenar los datos de configuración. Todos estos campos se usan luego para validar los registros, calcular la severidad y construir los informes.

### 4.1 Datos personales y clínicos

| Campo | Obligatorio | Descripción | Ejemplo |
|---|---|---|---|
| **Nombre completo** | Sí | Nombre y apellidos del paciente. Aparece en los informes. | `Javier Manuel Ortega Díaz` |
| **DNI / Identificador** | Recomendado | Documento de identidad o número de historia clínica. | `12345678Z` |
| **Número de la Seguridad Social (NUSS)** | Opcional | Número de afiliación a la Seguridad Social. Formato habitual en España: **12 dígitos** (2 de provincia + 8 del número + 2 de control), a menudo escrito con barras y guiones: `28/12345678-90`. | `28/12345678-90` |
| **Sexo** | Sí | `Hombre`, `Mujer` o `Sin especificar`. Condiciona las opciones de embarazo. | `male` |
| **Fecha de nacimiento** | Sí | Determina si el paciente es niño/adolescente o adulto, y permite calcular la edad. | `1985-04-10` |
| **Tipo de diabetes** | Sí | `Tipo 1`, `Tipo 2` o `Gestacional`. | `type1` |
| **Grupo de paciente** | Sí | `Adulto`, `Niño/adolescente` o `Embarazo`. | `adult` |
| **Monitorizar presión arterial** | Opcional | Casilla del perfil clínico. Si se activa, aparecen la sección de presión arterial y su análisis. | — |
| **Estado de embarazo** | Solo mujeres | `No embarazada`, `Embarazada`, `Lactancia` o `Postparto`. | `not_pregnant` |

> **Nota sobre la categoría de embarazo:** la **categoría de embarazo** (primer, segundo o tercer trimestre) **no se registra en la app**. Si tu profesional sanitario necesita esa información, la manejará en la clínica con sus propias herramientas.

> **Nota sobre el objetivo personalizado:** el campo **Objetivo personalizado** (rango de glucemia objetivo distinto del estándar) **no lo rellena el paciente**. Lo establece el **profesional sanitario** de la clínica que le proporcionó la app. Si tu endocrino te ha dado un objetivo distinto del estándar, será él quien lo introduzca en la app o en sus herramientas clínicas.

### 4.2 Unidades de glucosa y objetivos

- **Unidad de glucosa**: elige `mg/dL` (habitual en España, Estados Unidos y Latinoamérica) o `mmol/L` (habitual en Reino Unido y algunos países europeos). Todos los valores introducidos a partir de ese momento se interpretarán y mostrarán en esa unidad. Si cambias de unidad más adelante, la app convierte automáticamente los valores ya guardados.
- **Objetivos por defecto**:
  - Adulto no embarazado: **70–180 mg/dL** (3,9–10,0 mmol/L).
  - Embarazo: **63–140 mg/dL** (3,5–7,8 mmol/L).
  - Niños/adolescentes: **70–180 mg/dL** con ajustes según edad.
- Si tu profesional sanitario te ha dado un objetivo distinto, **será él quien lo introduzca** en la app o en sus herramientas clínicas. El paciente no debe modificar este campo por su cuenta.

### 4.3 Medicamentos e insulina

En la sección de **Medicamentos** se añaden los fármacos que el paciente usa habitualmente. Cada medicamento tiene estos campos:

| Campo | Descripción | Ejemplo |
|---|---|---|
| **Nombre comercial** | Denominación tal como aparece en el envase. | `ABASAGLAR 100 UNIDADES/ML KWIKPEN SOLUCION INYECTABLE EN PLUMA PRECARGADA` |
| **Principio activo** | Fármaco real. | `Insulina glargina` |
| **Laboratorio** | Titular del medicamento. | `Eli Lilly Nederland B.V.` |
| **Clase** | Clasificación ATC. | `Insulinas y analogos de accion prolongada (A10AE04)` |
| **Vía de administración** | Subcutánea, oral, etc. | `Subcutanea` |
| **Unidad** | Unidad de medida (UI, mg, mcg…). | `UI` |
| **Riesgo de hipoglucemia** | Marca si el fármaco puede provocar hipoglucemias. | `false` para análogos basales, `true` para insulina rápida |
| **Fuente** | Origen del dato (CIMA, manual…). | `cima` |
| **Dosis predeterminada** | Dosis que la app propondrá por defecto al registrar. | `16` |
| **Unidad predeterminada** | Unidad que se mostrará por defecto. | `ui` |
| **Posibles dosis** | Lista de presentaciones disponibles. | `[{ valor: "100", unidad: "U" }]` |

### 4.4 Dosis habitual y hora habitual

En cada medicamento debes indicar **dos cosas clave**:

1. **Dosis habitual**: la dosis que el paciente suele administrarse. La app la usará como valor por defecto al registrar la toma en una medición y como referencia para avisar si un registro se aleja mucho de lo habitual.
2. **Hora habitual**: la hora a la que suele administrarse. La app la usará para:
   - Ordenar los registros y agruparlos por "toma de mañana / mediodía / tarde / noche".
   - Avisar si una dosis no se ha registrado en las horas siguientes a la hora habitual.
   - Dibujar correctamente las gráficas de "insulina a lo largo del día".

> **Ejemplo**: una persona que se pone 16 UI de insulina glargina a las 21:00 tendría `dosisPredeterminada: "16"` y hora habitual `21:00`.

### 4.5 Ubicación para la meteorología

Indica la **ciudad y el país** donde vives habitualmente (por ejemplo, `Vigo, Pontevedra` o `Barcelona, España`). La app usará esa ubicación para:

- Descargar automáticamente la **temperatura, humedad, precipitación, presión atmosférica y viento** del día de cada registro.
- Guardar el nombre de la localidad junto al registro (útil si viajas: los registros de viaje conservarán la localidad de destino).
- Permitir análisis posteriores (por ejemplo, ¿empeora el control cuando llueve o hace mucho calor?).

> **Consejo**: si te vas de viaje, puedes cambiar temporalmente la ubicación. La app guardará los registros nuevos con la nueva localidad y conservará los antiguos con la suya.

---

## 5. Panel de configuración colapsable

Una vez completada la primera configuración, el panel deja de ser necesario en el día a día. Por eso la aplicación lo **colapsa automáticamente**:

- En la parte superior de la pantalla principal verás un **resumen compacto** con tu nombre, edad, tipo de diabetes y número de medicamentos activos.
- Para **desplegar** la configuración completa, **pulsa directamente sobre la barra del resumen**. Es decir, la barra entera es el botón: no hay que buscar ningún icono concreto.
- Para **volver a colapsarla**, vuelve a **pulsar sobre la barra**.

Esto evita que la pantalla se llene de campos que solo se rellenan una vez y deja más espacio para el registro diario, que es lo que realmente se usa cada día.

> **Importante**: los datos de configuración **no se pierden** al colapsar el panel. Solo se ocultan visualmente. Si necesitas cambiar algo, pulsa sobre la barra, edita, y vuelve a pulsar sobre la barra para colapsar.

---

## 6. Cómo añadir, editar y eliminar registros

La aplicación distingue **dos grandes tipos de registro**:

1. **Registros de glucemia** (`records`): recogen las glucemias del día y el contexto (comida, ejercicio, ánimo, meteorología…).
2. **Registros de medicación** (`medicationLog`): recogen cada dosis de insulina u otro fármaco administrada (u omitida).

### 6.1 Registro de una medición (glucemia y contexto)

1. En la sección **«Registrar medición»** completa el formulario:
   - **Fecha** (por defecto, hoy) y **Hora / momento**: `Desayuno`, `Almuerzo / Comida`, `Cena` o `Nocturna (antes de dormir)`.
   - **Glucosa antes**, **Glucosa después** (postprandial, opcional) y **Glucosa nocturna** (opcional), con su rango orientativo bajo cada campo.
   - **Medicamentos de esta medición**: marca la toma realizada o indica que se ha **omitido**. Puedes cambiar la dosis antes de guardar y usar **«Añadir medicamento»**.
   - **Ejercicio**: tipo (Sin ejercicio, Caminata, Caminata rápida, Trotar/Correr, Natación, Gimnasio, Pilates, Ciclismo, Yoga, Baile, Tenis), duración en minutos y pasos (opcional).
   - **Estado de ánimo / síntomas físicos**: selección múltiple (emocionales y físicos).
   - **Contexto de la comida** (opcional): plan recomendado, comida familiar, comida de trabajo, restaurante, comida rápida, alcohol, evento especial, exceso de cantidad, salté una comida…
   - **Comentarios / notas**.
   - **Meteorología**: se obtiene automáticamente de Open-Meteo para la fecha del registro (ver §4.5). Si falla la conexión, puedes introducirla a mano en **«Entrada manual de clima»**.
2. Pulsa **«Guardar medición»**. Si ya existe una medición de hoy para ese momento, usa **«Editar medición de hoy»**.
3. La **severidad** se calcula automáticamente (ver §7.4).

> **Recordatorio de días sin registrar:** poco después de abrir la app, si hay días recientes sin datos, aparece el aviso **«Tienes días sin registrar»** con botones para preseleccionar cada fecha.

### 6.2 Registro de medicación

La toma de insulina u otros fármacos se registra **dentro de la propia medición** («Medicamentos de esta medición»): marca la toma o márcala como **omitida**, ajusta la dosis si hace falta y guarda. Distinguir *omitida* de *no registrada* es importante: en los informes son eventos distintos. El registro histórico se guarda en `medicationLog`.

### 6.2 bis Registro de presión arterial (opcional)

Solo aparece si activas **«Monitorizar presión arterial»** en el perfil clínico. Introduce **fecha, hora, sistólica, diastólica, pulso y notas** y pulsa **«Agregar»** (o **«Cancelar»** al editar). El **historial de presión** se muestra debajo y el **análisis de presión arterial** (estadísticas, categorías ESC/ESH y comentario automático) está en el análisis clínico y en el informe PDF.

### 6.3 Edición y borrado

- **Editar**: pulsa sobre cualquier registro del historial. Usa **«Mostrar todas las mediciones»** para ver el historial completo. Se abrirá el formulario con los datos cargados.
- **Eliminar**: dentro del formulario de edición, pulsa **"Eliminar"**. La app pedirá confirmación antes de borrar.
- **Deshacer**: si acabas de borrar un registro, aparece un aviso con **"Deshacer"** durante unos segundos.

> **Recuerda:** si detectas que te falta un medicamento, que una dosis está mal anotada o que un ajuste de pauta no se reflejó, contacta con tu clínica. Ellos tienen herramientas para corregir tus datos de forma segura.

---

## 7. Sistemas que garantizan la correcta introducción de datos

### 7.1 Validación en el momento de la entrada

La app aplica validaciones **mientras escribes**, no solo al guardar:

| Campo | Validación |
|---|---|
| Fecha | Debe ser una fecha válida y no puede ser futura (salvo confirmación expresa). |
| Glucemia | Debe ser un número. En mg/dL se aceptan valores de 10 a 800; en mmol/L, de 0,5 a 45. Fuera de ese rango la app avisa y pide confirmación. |
| Dosis | Debe ser un número positivo. Si se aleja más de un 50 % de la dosis habitual, la app avisa. |
| Hora | Formato de 24 horas. |
| Unidad | Selector cerrado. |
| Tipo de ejercicio | Selector cerrado. |
| Estado de ánimo | Lista cerrada con selección múltiple. |
| Contexto dietético | Lista cerrada con selección múltiple. |
| Comentarios | Texto libre, longitud máxima 500 caracteres. |

### 7.2 Gestión de valores ausentes

- **Glucemia después** y **glucemia nocturna** son opcionales. Se guardan como `null` y **no cuentan como cero** en las estadísticas.
- **Ejercicio** puede quedar vacío.
- **Meteorología**: si no hay conexión o no hay ubicación configurada, los campos quedan vacíos, pero el registro se guarda.
- **Estado de ánimo**, **contexto dietético**: listas vacías si no se selecciona nada.
- **Comentarios**: cadena vacía si no se escriben.

Reglas estadísticas:

- Los **valores `null` se excluyen** de medias, medianas, percentiles y desviaciones estándar.
- En los gráficos, los huecos se representan como **ausencia de punto**, no como cero.
- En los informes PDF se indica el **número de valores disponibles** sobre el total de días del período.

### 7.3 Detección de duplicados y coherencia temporal

- La app **avisa** si intentas guardar dos registros con la misma fecha, misma comida y misma glucemia antes.
- Si detecta dos **dosis del mismo medicamento** en menos de 4 horas, muestra un aviso.
- Si la **fecha del registro** es anterior a la fecha de nacimiento o posterior a hoy, se bloquea.
- Si un registro tiene **glucemia después** pero no **glucemia antes**, la app permite guardarlo pero lo marca como **incompleto** en los informes.

### 7.4 Cálculo automático de severidad

| Severidad | Criterio orientativo |
|---|---|
| `null` | Glucemia dentro de objetivos y sin síntomas. |
| `mild` | Glucemia ligeramente fuera de rango (180–250 mg/dL en ayunas, o 55–70 mg/dL). |
| `moderate` | Glucemia claramente fuera de rango (> 250 mg/dL o 40–54 mg/dL). |
| `urgent` | Glucemia muy fuera de rango (> 300 mg/dL o < 40 mg/dL). |
| `emergency` | Glucemia extrema con riesgo vital (< 30 mg/dL, > 400 mg/dL o pérdida de conciencia). |
| `severe` | Episodio grave documentado (convulsiones, ingreso, glucagón). |

Este cálculo **no sustituye el juicio clínico**; es solo una ayuda para clasificar y priorizar la revisión de los registros.

### 7.5 Exportar Pacientes e Importar Pacientes

- **Exportar Pacientes**: descarga un archivo `.json` con **todos** los pacientes, medicamentos, registros de glucemia, presión arterial y registro de medicación.
- **Exportar Excel (Paciente actual)**: descarga una hoja de cálculo del paciente activo.
- **Copia de seguridad**: descarga el JSON del paciente actual.
- **Importar Pacientes** (o **Importar paciente**, en la ficha): carga un archivo `.json` previamente exportado. La app **valida el esquema** antes de cargarlo.
- Las **fichas temporales** recibidas por videollamada **no se incluyen** en ninguna exportación.

**Recomendación de frecuencia:** exporta **al menos una vez a la semana**.

**¿Dónde se guarda el archivo exportado?** En el **directorio de descargas por defecto** del dispositivo, que habitualmente es la carpeta **Descargas**.

---

## 8. Explicación detallada de cada sección

### 8.1 Cabecera y selector de paciente

La cabecera muestra el nombre y los datos de contacto de la clínica y los botones **📹 Videollamada**, **✉️ Enviar por email**, el **selector de tema** (claro/oscuro) y **Ayuda**. En la ficha del paciente están **+ Nuevo paciente**, **Importar paciente**, **Copia de seguridad**, **Cambiar paciente**, **Eliminar paciente** y **Guardar datos**. Cuando se ve una ficha recibida por videollamada, aparece un **aviso amarillo «Ficha temporal»**.

### 8.2 Panel de pacientes

Corresponde al array `patients`. Incluye `id`, `name`, `dni`, `socialSecurity`, `gender`, `dateOfBirth`, `diabetesType`, `patientGroup`, `pregnancyStatus`, `pregnancyCategory`, `glucoseUnit`, `customTarget`, `medicines`, `medicationLog`.

### 8.3 Panel de medicamentos

Corresponde al array `medicines`. Es importante que la **dosis predeterminada** y la **hora habitual** estén bien configuradas.

### 8.4 Registro de glucemias (records)

Cada registro tiene `id`, `patientId`, `profile`, `date`, `meal`, `glucoseBefore`, `glucoseAfter`, `glucoseNight`, `exercise`, `comments`, `mood`, `moods`, `weather`, `example`, `severity`, `createdAt`, `dietContext`.

### 8.5 Registro de medicación (medicationLog)

Cada entrada tiene `id`, `medId`, `nombre`, `dosis`, `unidad`, `fecha`, `omitida`, `nota`.

### 8.6 Meteorología

Campos: `temp`, `humidity`, `precipitation`, `pressure`, `wind`, `date`, `location`.

### 8.7 Ejercicio

Campos: `type` (walking, cycling, swimming, running, other), `duration` (minutos), `steps` (opcional).

### 8.8 Estado de ánimo

Valores: `normal`, `estresado`, `ansioso`, `cansado`, `fatiga`.

### 8.9 Contexto dietético

Valores: `plan_recomendado`, `comida_familiar`, `exceso_cantidad`, `alcohol`, `salte_comida`, `comida_rapida`, `restaurante`, `evento_especial`, `comida_trabajo`, `otro_imprevisto`.

### 8.10 Severidad

Se muestra como etiqueta de color: gris, verde, amarillo, naranja, rojo, rojo oscuro.

### 8.11 Panel de informes y PDF

El botón **«Imprimir PDF»** (dentro de **«Ver/Imprimir análisis clínico»**) ofrece dos documentos:

- **Versión para el paciente**: resumen corto en lenguaje sencillo (tiempo en rango, barra de colores y unos pocos consejos). **No incluye DNI ni nº de Seguridad Social.**
- **Informe clínico**: elige las secciones con **«Marcar todas» / «Quitar todas»**. La portada con la advertencia, el aviso médico final y la firma se incluyen **siempre**.

El **análisis clínico avanzado** incluye informe y problemas detectados, adherencia al plan y contexto dietético, influencia del clima y del estado de ánimo, **comparación antes/después** de un cambio de pauta, análisis de correlaciones (descriptivo, no causal) y **presión arterial**. Puedes exportar las estadísticas en JSON.

> Recuerda: **las gráficas y la exportación a PDF necesitan conexión a internet**.

### 8.12 Exportar Pacientes / Importar Pacientes

- **Exportar Pacientes**: descarga un `.json` con todos los pacientes y registros.
- **Importar Pacientes**: carga un `.json`. Puedes elegir entre **fusionar** o **reemplazar**.
- **Exportar Excel (Paciente actual)**: hoja de cálculo del paciente activo.
- **Validación**: la app comprueba el esquema antes de cargar.

---

## 9. Para profesionales sanitarios: datos de ejemplo (diabetes.json)

El archivo `diabetes.json` contiene **cinco pacientes ficticios** con **365 días de registros** cada uno (glucosa, ánimo, ejercicio, contexto dietético, medicación y, en dos casos, presión arterial). **Ninguno es real.** Las fechas se desplazan al cargarlos para que el último día coincida con **hoy**.

### 9.1 Cómo cargar los datos de ejemplo

En la pantalla inicial pulsa **«Soy profesional de la salud» → «Ver datos de ejemplo» → «Sí, cargar los 5 pacientes de ejemplo»**. El archivo `diabetes.json` se carga automáticamente (debe estar junto a la app). Las fechas se ajustan a hoy y los datos se pueden borrar con **«Borrar todo - empezar de nuevo»**.

### 9.2 Descripción de los cinco pacientes de ejemplo

#### 9.2.1 `pt_es_sample_t1_01` — Javier Manuel Ortega Díaz (Vigo)

- **Perfil**: varón, 41 años (nacido el 10/04/1985), diabetes tipo 1, adulto, no embarazado.
- **Medicamento**: Abasaglar (insulina glargina) 100 U/mL, vía subcutánea.
- **Pauta**: 12 UI a las 21:00.
  - **10/12/2025**: ajuste a **14 UI** tras revisión.
  - **24/12/2025**: ajuste a **16 UI**.
- **Utilidad**: caso **estable con ajuste progresivo de basal**.

#### 9.2.2 `pt_es_dawn_phenomenon_02` — Ana Maria Torres Gil (Barcelona)

- **Perfil**: mujer, 37 años (nacida el 03/11/1988), diabetes tipo 1, adulto, no embarazada.
- **Pauta**: 14 UI **a las 08:00**.
  - **24/12/2025**: cambio a **17 UI a las 20:30** (fenómeno del alba).
- **Utilidad**: caso de **fenómeno del alba**.

#### 9.2.3 `pt_es_poor_adherence_02` — Carlos Alberto Fernandez Lopez (Madrid)

- **Perfil**: varón, 44 años (nacido el 15/03/1982), diabetes tipo 1, adulto, no embarazado.
- **Pauta**: 16 UI a las 20:00.
  - **21/01/2026**: ajuste a **15 UI** (tras educación diabetológica).
- **Utilidad**: caso de **mala adherencia**.

#### 9.2.4 `pt_es_hypo_dose_reduce_02` — Laura Isabel Mendez Ruiz (Santiago de Compostela)

- **Perfil**: mujer, 35 años (nacida el 22/07/1990), diabetes tipo 1, adulto, no embarazada.
- **Pauta**: 18 UI a las 20:00.
  - **10/12/2025**: reducción a **14 UI** por hipoglucemias frecuentes.
- **Utilidad**: caso de **reducción de dosis por hipoglucemias**.

#### 9.2.5 `pt_es_exercise_variability_02` — Pablo Andres Molina Vega (Valencia)

- **Perfil**: varón, 33 años (nacido el 28/05/1993), diabetes tipo 1, adulto, no embarazado, sexo sin especificar.
- **Pauta**: 16 UI a las 20:00, con **ajustes puntuales a 14 UI los días de ejercicio intenso**.
- **Utilidad**: caso de **variabilidad por ejercicio**.

#### Medicación y presión arterial de los casos de ejemplo

- **Carlos** (caso principal para empezar): adherencia muy baja (~33 % de dosis olvidadas); además de insulina toma enalapril, amlodipino y atorvastatina por **hipertensión**, que se mantiene mal controlada. Tiene registros de **presión arterial**.
- **Ana**: además de insulina toma Eutirox; tras varios meses con presión normal-alta se diagnostica hipertensión y empieza Losartán con buena respuesta. Tiene registros de **presión arterial**.
- **Javier**: atorvastatina; presión normal. **Laura**: anticonceptivo oral combinado; presión normal. **Pablo**: ibuprofeno ocasional; presión normal con pulso bajo en reposo.

### 9.3 Opciones que conviene probar en los informes PDF

1. **Informe de 7 días** (`pt_es_sample_t1_01`, resumen ejecutivo).
2. **Informe de 30 días** (cualquiera, informe estándar).
3. **Informe de 90 días** (`pt_es_dawn_phenomenon_02`, informe completo).
4. **Informe de 365 días** (`pt_es_hypo_dose_reduce_02`, informe completo).
5. **Informe centrado en hipoglucemias** (`pt_es_hypo_dose_reduce_02`, 180 días).
6. **Informe centrado en adherencia** (`pt_es_poor_adherence_02`, 365 días).
7. **Informe centrado en ejercicio** (`pt_es_exercise_variability_02`, 90 días).
8. **Informe comparativo** (varios pacientes, 30 días, resumen).
9. **Informe con orientación horizontal** (cualquiera, 30 días, completo).
10. **Informe con rango personalizado** (`pt_es_dawn_phenomenon_02`, 10/12/2025–10/01/2026).

### 9.4 Guion de demostración sugerido

1. **Minuto 0–1**: abrir la app y mostrar la pantalla «Antes de empezar».
2. **Minuto 1–2**: elegir **«Soy profesional de la salud» → «Ver datos de ejemplo»** y cargar los 5 pacientes.
3. **Minuto 2–3**: mostrar el paciente activo y sus registros.
4. **Minuto 3–4**: generar un **informe de 30 días**.
5. **Minuto 4–5**: generar un **informe de 90 días** de `pt_es_dawn_phenomenon_02`.
6. **Minuto 5–6**: generar un **informe de 365 días** de `pt_es_hypo_dose_reduce_02`.
7. **Minuto 6–7**: usar **"Enviar por email"** y, si hay otro equipo, probar una **videollamada** (§10).
8. **Minuto 7–8**: mostrar **Exportar Pacientes** e **Importar Pacientes**.
9. **Minuto 8–9**: generar un **informe comparativo**.
10. **Minuto 9–10**: cerrar con la idea de flexibilidad y recordar el aviso legal.

---

## 10. Videollamada con el profesional sanitario

La app incluye una **videoconsulta entre médico y paciente** con vídeo, audio, **chat** y **pantalla compartida**. Además, el paciente puede **compartir sus datos** con el médico durante la llamada, de forma cifrada y solo con su consentimiento. Se abre con el botón **📹 Videollamada** de la cabecera (junto a **✉️ Enviar por email**).

> **Resumen en cuatro ideas**
> 1. **Nada se comparte sin tu permiso.** Puedes estar en la llamada sin compartir ningún dato.
> 2. **Permiso 1 — VER:** si aceptas compartir, el médico ve tus datos como una **ficha temporal** mientras dure la llamada. Se elimina al salir.
> 3. **Permiso 2 — GUARDAR:** solo si tú lo autorizas después, con un consentimiento informado y una doble confirmación, el médico podrá **guardar una copia** en sus registros.
> 4. **Los datos viajan cifrados.** El tratamiento posterior depende del profesional o de la clínica (§10.4).

### 10.1 Qué necesitas antes de empezar

- **Nombre de la sala**: te lo da tu médico o tu clínica (mayúsculas y números; hasta 12 caracteres). Pídelo por un **canal fiable** y **no lo compartas** con nadie más: además de identificar la llamada, es la **clave que cifra tus datos** (§10.3).
- **Tu nombre guardado en la ficha del paciente** (pulsa **«Guardar datos»**). Sin nombre, la app no te dejará compartir datos.
- **Conexión a internet**, **cámara y micrófono** con permisos concedidos, y la app abierta por **HTTPS**.
- Un navegador actual (Chrome, Edge, Firefox o Safari, como en §3).

### 10.2 Cómo usarla como paciente (paso a paso)

1. Pulsa **📹 Videollamada**. Se abre la pantalla de la videoconsulta. Deja seleccionado el rol de **paciente** (es el rol por defecto).
2. Pulsa **«Activar cámara y micrófono»** y **permite** el acceso cuando el navegador te lo pida. Puedes elegir cámara y micrófono en los selectores.
3. Escribe el **nombre de la sala** que te dio tu médico y pulsa **«Entrar»**. Si el médico **aún no ha abierto la sala**, verás una pantalla de espera y la llamada **se conectará sola** cuando la abra.
4. **Al conectarte** aparece el aviso **«Compartir mis datos con el médico»**, con tu nombre. Léelo y elige:
   - **«Acepto y comparto mis datos»** → se envían cifrados (**Permiso 1: ver**).
   - **«No compartir (seguir en la llamada)»** → la llamada continúa sin enviar nada. Puedes cambiar de idea más tarde con el botón **«Compartir mis datos»** de la barra superior.
   - Casilla opcional: **«Incluir también mi DNI y mi nº de Seguridad Social»**. **Por defecto no se envían.** Márcala solo si tu médico lo necesita.
5. Qué se envía: **perfil clínico, registros de glucosa, medicación y, si la usas, presión arterial.** La barra superior confirmará: *«✓ Datos enviados cifrados al médico. El médico solo puede verlos durante la llamada.»*
6. Durante la llamada puedes usar el **chat**, **silenciar** el micrófono, **cambiar de cámara** y **compartir pantalla**.
7. **(Opcional) Permitir que el médico guarde tus datos.** Cuando el médico ya ha recibido tus datos aparece el botón **«Permitir que el médico guarde mis datos»** (ver §10.4). No es obligatorio y puedes ignorarlo.
8. Para terminar pulsa **«✕ Cerrar»** (o **«Salir»** dentro de la llamada).

### 10.3 Cómo se mantienen seguros los datos

| Elemento | Protección |
|---|---|
| **Vídeo y audio** | Conexión directa entre los dos equipos (WebRTC), **cifrada por defecto**. Si un cortafuegos lo impide, la app prueba automáticamente servidores de relevo, que solo reenvían tráfico ya cifrado. |
| **Datos del paciente** | Se **cifran en tu equipo antes de enviarse** con **AES-256-GCM** (confidencialidad + detección de manipulación). La clave se deriva del **nombre de la sala** con PBKDF2-SHA256 (250.000 iteraciones, sal e IV aleatorios), y los datos se comprimen antes de cifrar. Solo se descifran en el equipo del médico. |
| **Quién puede ser médico** | Solo los médicos dados de alta por el administrador del sistema (§11), con usuario y contraseña. Tras 3 fallos hay un tiempo de espera. El rol de médico **no se recuerda**: se pide siempre la contraseña. |
| **Datos de identificación** | **DNI y nº de Seguridad Social no se envían** salvo que el paciente marque la casilla opcional. |
| **Lo que ve el médico** | Una **ficha temporal** (🩺, aviso amarillo): **no se guarda** en el equipo del médico, **no se puede exportar** como copia de seguridad ni incluir en exportaciones y **se elimina al salir** de la videollamada. |
| **Protección ante pérdidas** | Si el médico cierra o recarga la página con una ficha temporal abierta, el navegador pide confirmación. |
| **Integridad** | Si el nombre de sala no coincide o los datos se han alterado, **no se pueden descifrar** y la app lo indica. |
| **Guardado** | Nunca ocurre sin el **Permiso 2** del paciente (§10.4). |

**Límites que conviene conocer (sé consciente de ellos):**

- **La clave es el nombre de la sala.** Una sala fácil de adivinar (p. ej. `CONSULTA1`) protege menos. **Los médicos deben usar un código aleatorio** (la app lo genera si dejan el nombre en blanco), no reutilizarlo con otros pacientes y enviárselo al paciente por un canal fiable.
- **Comprueba que hablas con tu médico** antes de aceptar compartir. El cifrado protege el envío, no la identidad de quien está al otro lado.
- La conexión se establece con **servicios públicos de terceros** (servidor de señalización y servidores de ayuda a la conexión). Estos no reciben tus datos clínicos en claro, pero pueden ver datos técnicos de la conexión (como la dirección IP y el nombre técnico de la sala). La clínica puede configurar su propio servidor en los ajustes avanzados de la videollamada.
- La app **no cifra** los datos guardados en el navegador (§12).
- El cifrado no sustituye el cumplimiento del **RGPD** por parte de la clínica.

### 10.4 Los dos permisos: VER primero, GUARDAR después

| | **Permiso 1: VER** | **Permiso 2: GUARDAR** |
|---|---|---|
| **Cuándo** | Al conectarte (o con **«Compartir mis datos»**) | Después de haber compartido los datos |
| **Qué permite** | Que el médico **vea** tus datos durante la llamada | Que el médico **guarde una copia** en sus registros de pacientes |
| **Cómo se da** | Un clic: **«Acepto y comparto mis datos»** | **Consentimiento informado** con casilla + **segunda confirmación** |
| **Cuánto dura** | Hasta que salgas de la llamada | Hasta que lo retires |
| **Si no se da** | Sigues en la llamada sin compartir nada | El médico solo ve la ficha temporal, que se borra al salir |

**Cómo se da el permiso de guardado:**

1. Tras compartir tus datos, pulsa **«Permitir que el médico guarde mis datos»** (barra superior).
2. Se abre el **consentimiento informado**, que explica:
   - **Qué se guardaría:** lo que acabas de compartir (perfil clínico, glucosa, medicación y presión arterial si la usas). DNI y nº de Seguridad Social solo si los marcaste.
   - **Para qué:** el seguimiento clínico de tu diabetes y tu historial de atención.
   - **Dónde y quién:** en el **almacenamiento local del navegador del equipo del médico**. El profesional o la clínica será el **responsable del tratamiento**. Pregúntale su identidad, contacto y plazo de conservación.
   - **Tus derechos:** acceso, rectificación, supresión, limitación, portabilidad y **retirar el consentimiento en cualquier momento** sin que afecte a tu atención. Puedes reclamar ante la **Agencia Española de Protección de Datos (aepd.es)**.
   - **Es voluntario:** puedes negarte y seguir con la consulta.
3. Marca la casilla **«He leído y comprendo esta información y autorizo expresamente…»** y pulsa **«Aceptar y continuar»** (hasta que no marques la casilla el botón está desactivado).
4. Aparece una **confirmación final**: **«Sí, autorizo»** o **«No, volver»**.
5. La autorización se envía al médico. Verás *«Autorización enviada. Esperando la respuesta del médico…»*.
6. **El médico decide si guarda la ficha.** Tú verás el resultado: *«✓ El médico ha guardado tus datos en su ficha de pacientes»* o *«El médico no ha guardado tus datos. Solo los ha visto durante la llamada.»* (en ese caso puedes volver a darle el permiso si quieres).

**Cómo retirar el permiso:** la app del paciente **no tiene un botón para borrar la copia** que ya está en el sistema del médico. Para retirarlo (o pedir acceso, rectificación o supresión), **dirígete al profesional o a la clínica**; ellos deben atender tu solicitud.

### 10.5 Cómo usarla como profesional sanitario

1. Pulsa **📹 Videollamada** y elige el rol **Médico**. Selecciona tu **usuario** de la lista y escribe tu **contraseña** (facilitados por el administrador del sistema, §11). Puedes marcar **«Guardar la contraseña en este equipo»** (**solo en un equipo personal**).
2. **Crea la sala.** El nombre debe tener **al menos 6 letras o números**; si lo dejas en blanco, la app genera un **código aleatorio** (más seguro). Puedes guardar salas habituales con **«Salas…»**. Envía el nombre al paciente **por un canal fiable**.
3. Espera al paciente. Si entra antes de que abras la sala, se conectará solo cuando la abras.
4. Cuando el paciente comparta sus datos aparece su **ficha temporal** (marcada con 🩺 y un **aviso amarillo**). Puedes consultarla como cualquier otro paciente (registros, análisis, informes), pero **no se guarda, no se exporta y se elimina al salir**.
5. Si el paciente **autoriza el guardado**, aparece el aviso **«El paciente autoriza guardar sus datos»**:
   - **«Guardar en mis pacientes»**: la ficha se guarda **en el almacenamiento local de este navegador, junto con la fecha del consentimiento** (y tu usuario). Haz copias de seguridad con regularidad (§2.5) y ten en cuenta la capacidad (§3.3). Si ya tienes un paciente con el mismo DNI (o mismo nombre y fecha de nacimiento), la app **pregunta si quieres sobrescribirlo**.
   - **«No guardar»**: la ficha sigue siendo temporal.
6. Al salir con una ficha temporal abierta, la app pide confirmación porque se eliminará.

> **Responsabilidad del profesional:** al guardar la ficha te conviertes en **responsable del tratamiento** de esos datos (RGPD). Comunica al paciente tu identidad, el plazo de conservación y cómo ejercer sus derechos, y conserva el registro del consentimiento.

### 10.6 Problemas habituales con cámara y micrófono

Si ves **«No podemos acceder al micrófono o la cámara»**, el navegador no tiene permiso. Pulsa **«Show me how to fix it»** o sigue estos pasos:

- **iPhone / iPad:** Ajustes → Safari → Cámara y Micrófono → **Permitir**.
- **Android:** Ajustes → Aplicaciones → tu navegador → Permisos → permitir **Cámara** y **Micrófono**.
- **Ordenador:** haz clic en el icono del candado junto a la dirección y permite **Cámara** y **Micrófono**.

Después, **reinicia el navegador por completo**. Si la llamada no conecta, prueba con otra red (por ejemplo, datos móviles) o avisa a la clínica: puede configurar un servidor de relevo propio.

### 10.7 Avisos importantes

- La videoconsulta y el envío de datos **no sustituyen la atención presencial ni los servicios de urgencias**. **En caso de urgencia, llama al 112.**
- Compartes tus datos **de forma voluntaria** y puedes negarte sin perder la llamada.
- La app ofrece información de apoyo y **no emite diagnósticos**.
- Los textos de consentimiento de la app son informativos: **la clínica o el profesional responsable debe revisarlos y adaptarlos** antes de usarlos con pacientes reales.

---

## 11. Alta de médicos y ajustes de la clínica

**El administrador del sistema** (la persona que instala y mantiene la app para la clínica) es quien **da de alta a los médicos** que pueden crear salas de videollamada. Cada médico recibe de él un **usuario y una contraseña**.

- Si eres **profesional sanitario** y no puedes entrar como médico, **solicita el alta (o el cambio de contraseña) a tu administrador del sistema**.
- Los **pacientes no necesitan usuario ni contraseña**: solo el nombre de la sala que les da su médico.
- Usa una contraseña que **no utilices en ningún otro servicio** y no la compartas.

> **Para la clínica:** el nombre y los datos de contacto que aparecen en la cabecera de la app son marcadores de ejemplo (*«Nombre de su clínica»*, teléfono y email) que **deben sustituirse** por los reales antes de entregar la app a pacientes.

---

## 12. Privacidad, seguridad y cumplimiento

- **Los datos no salen del dispositivo** salvo que tú decidas enviarlos: por **email** (archivo JSON que tú adjuntas y envías) o por **videollamada** (cifrados, con tu consentimiento expreso; ver §10).
- **Cuentas y contraseñas:** los pacientes no necesitan cuenta ni contraseña. Solo los **médicos** que crean salas de videollamada usan usuario y contraseña, facilitados por el administrador del sistema (ver §11).
- **Cifrado en reposo:** la app **no cifra** los datos guardados en el navegador. Usa el cifrado de disco del sistema operativo y no uses equipos compartidos.
- **Cifrado en la videollamada:** los datos del paciente se cifran con AES-256-GCM antes de enviarse; el vídeo y el audio van cifrados por WebRTC. Detalles y límites en §10.5.
- **Ficha temporal:** lo que recibe el médico por videollamada no se guarda y se elimina al salir, salvo que el paciente dé un segundo permiso expreso.
- **Servicios de terceros:** la meteorología (Open-Meteo), las librerías de gráficas y PDF, y la conexión de la videollamada (servidor de señalización y servidores STUN/TURN) dependen de servicios externos. Ninguno recibe tus registros médicos en claro.
- **Recomendaciones:** exporta **semanalmente**, no compartas el `.json` por canales inseguros, revisa los campos antes de enviar y cumple con el RGPD y la LOPDGDD. **La clínica o el profesional responsable del tratamiento debe revisar y adaptar los textos de consentimiento** antes de usarlos con pacientes reales.

---

## 13. Preguntas frecuentes (FAQ)

**¿Necesito internet para usar la app?** Sí, para las gráficas, la exportación a PDF y la meteorología.

**¿Puedo usar la app en varios dispositivos?** Sí, pero no se sincronizan automáticamente.

**¿Puede mi médico ver mis datos durante la videollamada?** Solo si pulsas «Acepto y comparto mis datos». Puedes negarte y seguir en la llamada.

**¿El médico se queda con mis datos al terminar la llamada?** No. Los ve como ficha temporal que se elimina al salir. Solo podrá guardarlos si le das un segundo permiso expreso (§10.4).

**¿Puedo retirar el permiso de guardado?** Sí, en cualquier momento, pidiéndoselo al profesional o a la clínica (RGPD).

**¿Se envían mi DNI y mi nº de Seguridad Social?** No por defecto; solo si marcas la casilla opcional al compartir.

**¿Qué hago si mi médico no abre la sala?** Espera: la llamada se conectará sola cuando la abra.

**¿Cómo registro la presión arterial?** Activa «Monitorizar presión arterial» en el perfil clínico.

**¿Qué pasa si borro los datos del navegador?** Se pierden. Exporta semanalmente.

**¿Puedo cambiar de mg/dL a mmol/L?** Sí, la app convierte automáticamente.

**¿Puedo tener varios pacientes?** Sí. Todos se guardan en el mismo navegador y comparten unos 5 MB, así que caben unos 10 pacientes con un año de datos (§3.3).

**¿Cuántos registros caben?** Cada lectura ocupa unos 0,7 KB; con una lectura al día son unos 0,35 MB por paciente y año. Exporta y archiva los años antiguos.

**¿Puedo registrar solo la insulina?** Sí.

**¿Puedo registrar una dosis omitida?** Sí, marca la casilla **"Omitida"**.

**¿Los informes PDF se envían a algún servidor?** No.

**¿Puedo usar la app en el móvil?** Sí.

**¿Qué hago si el PDF sale mal?** Revisa los márgenes de impresión.

**¿Cada cuánto debo exportar?** Al menos una vez a la semana.

**¿Dónde se guardan los archivos que descarga la app?** En el directorio de descargas por defecto (habitualmente la carpeta **Descargas**).

**¿Cada cuánto debo ir a la consulta?** La frecuencia la decide tu profesional sanitario. Orientación general: **cada 3 meses** (tipo 1 o tipo 2 insulinizada), **cada 6–12 meses** (tipo 2 no insulinizada o bien controlada).

**¿Qué hago si me falta un medicamento o una dosis está mal?** Contacta con tu clínica.

**¿Quién decide mi objetivo personalizado de glucemia?** Tu profesional sanitario.

**¿Se registra la categoría de embarazo (trimestre)?** No, la app no la registra.

**¿Cómo cambio entre tema claro y oscuro?** Con el selector «Tema» de la cabecera.

---

## 14. Solución de problemas

| Problema | Causa probable | Solución |
|---|---|---|
| La app no carga | JavaScript desactivado o navegador antiguo | Activa JavaScript o actualiza el navegador |
| No se guardan los datos | Modo incógnito o almacenamiento lleno | Sal del modo incógnito, exporta una copia de seguridad y borra registros antiguos |
| No aparecen las gráficas | Sin conexión a internet | Conéctate y recarga |
| No se genera el PDF | Sin conexión a internet | Conéctate y vuelve a intentarlo |
| No aparece la meteorología | Sin ubicación configurada o sin conexión | Configura la ubicación y comprueba la conexión |
| El PDF sale cortado | Márgenes de impresión | Ajusta los márgenes en el diálogo de impresión |
| La importación falla | Archivo corrupto o esquema incompatible | Comprueba el JSON |
| Las gráficas salen vacías | No hay datos en el rango seleccionado | Amplía el rango de fechas |
| Los valores se ven en otra unidad | Cambio de mg/dL a mmol/L | La app convierte automáticamente |
| La videollamada no pide cámara/micrófono o dice que no puede acceder | Permisos del navegador denegados | Permite cámara y micrófono en los ajustes del navegador/sistema y reinicia el navegador (ver §10.6) |
| La videollamada no conecta | Cortafuegos o red restrictiva | La app prueba automáticamente conexiones de relevo; prueba otra red (datos móviles) o avisa a la clínica |
| «No se pudieron abrir los datos recibidos» (médico) | Nombre de sala distinto o datos alterados | Comprobad que ambos usáis el mismo nombre de sala y que el paciente vuelva a pulsar «Compartir mis datos» |
| No aparece «Compartir mis datos» | Falta el nombre del paciente o no hay conexión con el médico | Escribe tu nombre, pulsa «Guardar datos» y espera a que conecte el médico |
| El médico no puede entrar | Usuario/contraseña incorrectos o médico no dado de alta | Comprueba los datos o solicita el alta al administrador del sistema (§11); tras 3 fallos hay una espera |
| No encuentro el JSON exportado | Se guarda en el directorio de descargas por defecto | Busca en la carpeta **Descargas** |

---

## 15. Glosario

- **Basal**: insulina de acción prolongada.
- **Bolo**: insulina de acción rápida antes de las comidas.
- **Fenómeno del alba**: hiperglucemia matutina.
- **HbA1c**: hemoglobina glicada.
- **Hipoglucemia**: glucemia por debajo de 70 mg/dL (3,9 mmol/L).
- **Hiperglucemia**: glucemia por encima de 180 mg/dL (10,0 mmol/L).
- **mg/dL**: miligramos por decilitro.
- **mmol/L**: milimoles por litro.
- **UI**: unidad internacional de insulina.
- **Ficha temporal**: copia de los datos de un paciente que el médico ve durante la videollamada y que se elimina al salir.
- **Sala**: nombre de la videollamada; además es la clave que cifra los datos del paciente.
- **WebRTC**: tecnología del navegador que permite la videollamada directa entre dos equipos.
- **STUN/TURN**: servidores auxiliares que ayudan a conectar la llamada cuando hay cortafuegos.
- **RGPD / LOPDGDD**: normativa europea y española de protección de datos.
- **ESC/ESH**: guías europeas de clasificación de la presión arterial.
- **CIMA**: Centro de Información online de Medicamentos de la AEMPS.
- **NUSS**: Número de afiliación a la Seguridad Social. Formato español: 12 dígitos, habitualmente con barras y guiones: `28/12345678-90`.

---

## 16. Anexo A: esquema del archivo JSON

```jsonc
{
  "patients": [
    {
      "id": "string",
      "name": "string",
      "dni": "string",
      "socialSecurity": "string",
      "gender": "male | female | unspecified",
      "dateOfBirth": "YYYY-MM-DD",
      "diabetesType": "type1 | type2 | gestational",
      "patientGroup": "adult | child_adolescent | pregnancy",
      "pregnancyStatus": "not_pregnant | pregnant | lactation | postpartum",
      "pregnancyCategory": "string",
      "glucoseUnit": "mgdl | mmoll",
      "customTarget": null,
      "medicines": [ /* ... */ ],
      "medicationLog": [ /* ... */ ]
    }
  ],
  "currentPatientId": "string",
  "records": [ /* ... */ ],
  "bpRecords": [ /* presión arterial: fecha, hora, sistólica, diastólica, pulso, notas */ ]
}
```

Una ficha guardada tras una videollamada incluye además `consentSaved`: `{ grantedAt, savedAt, via: "videoconsulta", version, doctor }` (fecha del consentimiento del paciente, fecha de guardado y usuario médico).

---

## 17. Anexo B: valores admitidos en campos cerrados

**`meal`**: `breakfast`, `lunch`, `dinner`, `snack`, `other`.

**`exercise.type`**: `walking`, `cycling`, `swimming`, `running`, `other`.

**`moods`**: `normal`, `estresado`, `ansioso`, `cansado`, `fatiga`.

**`dietContext`**: `plan_recomendado`, `comida_familiar`, `exceso_cantidad`, `alcohol`, `salte_comida`, `comida_rapida`, `restaurante`, `evento_especial`, `comida_trabajo`, `otro_imprevisto`.

**`severity`**: `null`, `mild`, `moderate`, `urgent`, `emergency`, `severe`.

**`gender`**: `male`, `female`, `unspecified`.

**`diabetesType`**: `type1`, `type2`, `gestational`.

**`patientGroup`**: `adult`, `child_adolescent`, `pregnancy`.

**`pregnancyStatus`**: `not_pregnant`, `pregnant`, `lactation`, `postpartum`.

**`glucoseUnit`**: `mgdl`, `mmoll`.

---

*Fin del README. Recuerda: la app no diagnostica ni recomienda tratamientos; solo un profesional sanitario puede hacerlo. Consulta con tu equipo de diabetes la frecuencia de tus revisiones y contacta con tu clínica si necesitas corregir algún dato. La videollamada no sustituye la atención presencial ni las urgencias: ante una urgencia, llama al 112.*
