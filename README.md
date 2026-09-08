# AS Academy Shop - Web Scraping Challenge

## Descripción

Desarrollar un crawler en Python capaz de extraer información de los productos disponibles en:

https://as-academy-shop.vercel.app/

El objetivo de esta tarea es poner en práctica conceptos de **web scraping**, navegación entre páginas, autenticación mediante formularios, interacción con elementos dinámicos, envío de formularios y persistencia de información.

Además de obtener la información de los productos, el crawler deberá iniciar sesión en la plataforma y publicar una review/comentario en cada producto encontrado.

---

## Objetivos

El crawler deberá ser capaz de:

* Acceder al sitio.
* Realizar correctamente el proceso de login.
* Navegar por los productos disponibles.
* Extraer la información requerida de cada producto.
* Acceder al detalle de cada producto cuando sea necesario.
* Publicar una review en cada producto.
* Asignar nombres ficticios diferentes a las reviews.
* Utilizar diferentes cantidades de estrellas entre los productos.
* Guardar los productos obtenidos en formato CSV.
* Evitar la pérdida de información si el crawler falla durante la ejecución.
* Permitir que una ejecución pueda continuar trabajando con información previamente obtenida.

---

# Datos requeridos

Por cada producto se deberá obtener como mínimo la siguiente información:

| Campo          | Descripción                            |
| -------------- | -------------------------------------- |
| `name`         | Nombre del producto                    |
| `title`        | Título del producto                    |
| `price`        | Precio original                        |
| `sale_price`   | Precio en oferta, únicamente si existe |
| `category`     | Categoría a la que pertenece           |
| `description`  | Descripción del producto               |
| `availability` | Estado de disponibilidad               |
| `image`        | URL de la imagen principal             |

Cuando un producto no tenga `sale_price`, el campo deberá mantenerse vacío o utilizar un valor nulo consistente con el formato utilizado en el proyecto.

---

# Output

El resultado final del scraping deberá almacenarse en un archivo:

```text
products.csv
```

Cada fila deberá representar un producto.

Ejemplo conceptual:

```csv
name,title,price,sale_price,category,description,availability,image
Product A,Product A Title,120.00,99.00,Electronics,Product description,In Stock,https://example.com/image.jpg
Product B,Product B Title,50.00,,Accessories,Product description,In Stock,https://example.com/image2.jpg
```

Los datos deben almacenarse de manera consistente y preparados para ser posteriormente procesados o analizados.

---

# Persistencia y recuperación ante fallos

El crawler deberá contemplar posibles errores durante su ejecución.

No se deberá depender únicamente de que el crawler llegue correctamente hasta el final para guardar los productos.

Los productos que ya hayan sido obtenidos deberán conservarse durante la ejecución.

Por ejemplo, si existen 50 productos y el crawler falla mientras procesa el producto número 40, los productos obtenidos previamente no deberán perderse.

Al iniciar nuevamente el crawler se deberá poder utilizar la información previamente almacenada para evitar repetir innecesariamente el trabajo realizado.

La implementación utilizada para resolver esta situación queda a criterio del desarrollador.

Se evaluará especialmente:

* Persistencia progresiva de resultados.
* Prevención de pérdida de información.
* Manejo de excepciones.
* Posibilidad de recuperación después de un fallo.
* Prevención de registros duplicados.

---

# Login

Antes de realizar determinadas operaciones sobre los productos, el crawler deberá completar correctamente el flujo de autenticación disponible en el sitio.

El objetivo de esta parte de la tarea es practicar:

* Identificación de formularios.
* Localización de inputs.
* Ingreso de información.
* Envío de formularios.
* Manejo de sesiones autenticadas.
* Validación de una autenticación exitosa.

Las credenciales utilizadas para realizar el login deberán manejarse mediante variables de entorno.

No deberán escribirse credenciales directamente dentro del código fuente.

---

# Reviews de productos

Después de iniciar sesión, el crawler deberá publicar una review en cada producto.

El comentario deberá respetar la siguiente estructura:

```text
La verdad que el producto [product name] cumple con mis expectativas, su precio [product price] totalmente accesible. Recomiendo este producto.
```

Donde:

```text
[product name]
```

deberá reemplazarse dinámicamente por el nombre del producto actual.

Y:

```text
[product price]
```

deberá reemplazarse dinámicamente por el precio correspondiente al producto.

Por ejemplo:

```text
La verdad que el producto Wireless Headphones cumple con mis expectativas, su precio 49.99 totalmente accesible. Recomiendo este producto.
```

El comentario no deberá estar hardcodeado individualmente para cada producto.

Deberá generarse dinámicamente utilizando la información obtenida por el crawler.

---

# Nombre de las reviews

Cada review deberá utilizar un nombre ficticio.

Los nombres pueden generarse dinámicamente o seleccionarse desde una colección previamente definida.

Ejemplos:

```text
Lucas Martínez
Sofía Gómez
Matías Fernández
Camila Rodríguez
Valentina López
Nicolás Torres
```

Se deberá evitar, en la medida de lo posible, utilizar exactamente el mismo nombre para todos los productos.

---

# Rating

Cada producto deberá recibir una cantidad de estrellas.

No todos los productos deberán recibir la misma valoración.

Por ejemplo:

```text
Producto A -> 5 estrellas
Producto B -> 4 estrellas
Producto C -> 3 estrellas
Producto D -> 5 estrellas
Producto E -> 4 estrellas
```

Las estrellas pueden asignarse mediante una estrategia aleatoria o utilizando alguna lógica definida por el desarrollador.

La valoración deberá encontrarse dentro del rango permitido por el formulario del sitio.

---

# Manejo de formularios

La tarea deberá contemplar como mínimo dos tipos de interacción mediante formularios:

```text
Login
```

y

```text
Creación de reviews
```

El crawler deberá verificar que las acciones realizadas realmente hayan sido procesadas por la aplicación.

No se deberá asumir que un click o un envío de formulario fue exitoso únicamente porque no se produjo una excepción.

---

# Manejo de errores

El crawler deberá manejar adecuadamente situaciones como:

* Elementos que no aparecen.
* Cambios inesperados durante la navegación.
* Productos que no pueden procesarse.
* Errores durante el login.
* Errores durante la publicación de una review.
* Timeouts.
* Navegación fallida.
* Errores de conexión.
* Campos opcionales inexistentes.
* Interrupciones inesperadas de la ejecución.

Un error sobre un producto individual no debería necesariamente detener todo el proceso de scraping.

Cuando sea posible, el crawler deberá registrar el error y continuar procesando los siguientes productos.

---

# Logging

La aplicación deberá proporcionar información suficiente para conocer el estado de la ejecución.

Por ejemplo:

```text
Crawler started
Login successful
Products detected: 50
Processing product 1/50
Product saved
Review submitted successfully
Processing product 2/50
...
Crawler finished
```

También deberán registrarse errores relevantes.

No es necesario utilizar exactamente estos mensajes.

---

# Configuración

Los valores configurables deberán mantenerse separados de la lógica principal.

Variables como:

* URL base.
* Credenciales.
* Timeouts.
* Nombre del archivo de salida.
* Configuración del navegador.

deberán gestionarse utilizando `config.py` y/o variables de entorno según corresponda.

---

# Variables de entorno

El proyecto deberá incluir:

```text
.env
.env.example
```

El archivo `.env` contendrá las variables reales utilizadas localmente.

Por ejemplo:

```env
SHOP_EMAIL=
SHOP_PASSWORD=
```

El archivo `.env.example` deberá mostrar las variables necesarias sin incluir credenciales reales.

Ejemplo:

```env
SHOP_EMAIL=your_email@example.com
SHOP_PASSWORD=your_password
```

El archivo `.env` deberá estar incluido dentro del `.gitignore`.

---

# Estructura del proyecto

La estructura mínima requerida será:

```text
project/
│
├── main.py
├── config.py
├── web_driver.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── products.csv
```

---

## `main.py`

Archivo principal encargado de coordinar la ejecución del crawler.

Deberá contener o utilizar la lógica necesaria para coordinar:

* Inicio del crawler.
* Login.
* Obtención de productos.
* Procesamiento individual.
* Guardado de resultados.
* Publicación de reviews.
* Manejo general de errores.

---

## `config.py`

Centralizará la configuración utilizada por la aplicación.

Por ejemplo:

* URLs.
* Timeouts.
* Rutas.
* Variables de entorno.
* Configuraciones generales del crawler.

---

## `web_driver.py`

Deberá concentrar la configuración y creación del navegador utilizado para realizar la automatización.

El resto de la aplicación no debería repetir innecesariamente la configuración del driver.

---

## `requirements.txt`

Deberá contener todas las dependencias necesarias para ejecutar el proyecto.

El proyecto deberá poder instalarse mediante:

```bash
pip install -r requirements.txt
```

---

## `.gitignore`

Deberá excluir archivos que no deben formar parte del repositorio, incluyendo como mínimo:

```text
.env
__pycache__/
*.pyc
```

También podrán excluirse archivos temporales generados por el navegador o por el entorno utilizado.

---

# Calidad de los datos

Antes de almacenar un producto se deberá comprobar que la información obtenida sea coherente.

Se deberá prestar atención a:

* Precios correctamente normalizados.
* URLs completas de imágenes.
* Valores vacíos.
* Campos opcionales.
* Duplicados.
* Caracteres especiales.
* Espacios innecesarios.

Los productos no deberán duplicarse en `products.csv` debido a reintentos o reinicios del crawler.

---

# Requerimientos técnicos

El proyecto deberá:

* Estar desarrollado en Python.
* Utilizar una herramienta de automatización/web scraping apropiada.
* Mantener una estructura clara.
* Separar configuración y lógica.
* Utilizar variables de entorno para información sensible.
* Manejar excepciones correctamente.
* Implementar persistencia progresiva de productos.
* Generar como resultado final un archivo CSV.
* Mantener una sesión autenticada durante las operaciones que lo requieran.
* Automatizar la publicación de reviews.
* Evitar duplicar productos después de reiniciar el crawler.

---

# Entregables

El proyecto entregado deberá contener como mínimo:

```text
main.py
config.py
web_driver.py
requirements.txt
.env.example
.gitignore
products.csv
```

El archivo `.env` deberá existir localmente para ejecutar el proyecto, pero **no deberá subirse al repositorio**.

---

# Resultado esperado

Al finalizar correctamente la ejecución deberá existir un archivo `products.csv` con todos los productos encontrados en el sitio.

Además, cada producto deberá haber recibido una review generada utilizando:

* Nombre ficticio.
* Nombre real del producto.
* Precio real del producto.
* Rating variable.

El proyecto deberá poder tolerar fallos durante la ejecución sin perder los productos que ya hayan sido procesados.

El objetivo principal no es únicamente conseguir los datos, sino desarrollar un crawler organizado, recuperable, mantenible y capaz de interactuar correctamente con formularios y sesiones autenticadas.
