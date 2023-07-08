# Estimador de Precios de Viviendas en Santa Cruz de la Sierra

## Resumen del proyecto

* Se creó una herramienta que permite **estimar el precio de viviendas** en Santa Cruz de la Sierra, Bolivia. Esto con el fin de proveer una primera aproximación del precio para una diversidad de escenarios.
* Los datos se extrajeron de páginas donde se ofertan viviendas, en las cuales vienen incluidos el precio y diferentes características de las mismas. Se utilizó técnicas de **web scraping** para este propósito.
* Se preprocesaron y se aplicaron técnicas de **feature engineering** a los datos para extraer características útiles para el modelado.
* Se entrenaron diversos algoritmos de regresión, utilizando **grid search** para optimizar los *hiperparámetros* y obtener el mejor modelo. Los modelos puestos a prueba fueron: *Lasso Regression*, *Random Forest Regressor*, *Gradient Boosting Regressor* y *KNN Regressor*.
* Se construyó una **página web** que permite utilizar el modelo seleccionado. En la misma también se hace accesible un **dashboard** para explorar la base de datos utilizada.
* Adicionalmente se hace accesible el modelo mediante una **API**, esta se implementó usando **Flask**.

## Página Web

La herramienta se hace accesible a través de la siguiente página web, hosting provisto por Google Cloud:

[bienes-raices-scz-ohh5653uva-uc.a.run.app](https://bienes-raices-scz-ohh5653uva-uc.a.run.app/)

## Requerimientos

* **Versión de Python:** 3.10
* **Librerias:** selenium, numpy, pandas, matplotlib, seaborn, scikit-learn, plotly, dash
* **Requerimientos para reproducir el análisis:** requirements.txt
* **Conda environment:** environment.yml
* **Requerimientos para la app:** requirements_app.txt

## Web Scraping

Los datos se obtuvieron de páginas en las que se ofertan viviendas. Junto con el precio, también se listan diversas características tales como dimensiones, número de ambientes, ubicación, entre otros. 

De ellas se escogieron las siguientes: Descripción de la propiedad, Precio, Descripción de la ubicación, Número de ambientes, Número de baños, Terreno (en m2), Año de construcción, Número de dormitorios, Área construida, Número de estacionamientos, Ubicación: latitud y longitud.

Para este paso se utilizó **Selenium** y se obtuvo un total de 1520 propiedades para su posterior análisis.

## Preprocesado de los datos

Los datos tuvieron que pasar por un proceso de preprocesado para asegurar la calidad de los mismos. Los pasos fueron los siguientes:

* De la descripción de la ubicación se extrajo la ciudad y la zona.
* Se aseguró la consistencia de la fecha de construcción y únicamente se tomó el año.
* Se quitaron decimales a las coordenadas, por temas de privacidad.
* Al inspeccionar los valores repetidos, se pudo constatar que en su mayoría corresponden a diferentes propiedades pero dentro del mismo proyecto inmobiliario. Por ello, se conservaron estos puntos para el modelado.

## Análisis Exploratorio de los Datos

El primer paso en esta etapa fue explorar los valores faltantes y escoger técnicas de imputación de los mismos para cada caso. En el caso del número de ambientes, se seleccionó *KNN-imputer*, donde el número de *neighbors* se tomó como *hiperparámetro* a seleccionar en la siguiente etapa.

Luego, se aseguró el correcto formato y tipo de datos de cada columna.

Una vez se tuvo una base de datos limpia, se procedió a analizar distintas visualizaciones. A continuación se muestran las más destacadas.

<img src="images/corr.png" alt="Alt text 1" width="300"/>  <img src="images/tipo.png" alt="Alt text 1" width="300"/> <br>

<img src="images/zona.png" alt="Alt text 1" width="300"/>  <img src="images/violin.png" alt="Alt text 1" width="300"/>

## Construcción del modelo

El modelo que mejor se desempeñó fue **Gradient Boosting Regressor**, utilizando el *test set* y utilizando el coeficiente de determinación, *r2*, como métrica.

Para llegar a este resultado, se utilizó **GridSearch** con **Cross Validation** para encontrar los mejores hiperparámetros para los algoritmos considerados. Estos fueron: *Random Forest Regressor*, *Gradient Boosting Regressor* y *KNN Regressor*. También se integraron las técnicas de imputación de valores faltantes antes discutidas.

Se escogió *Lasso Regression* como modelo base y los otros tres se consideraron debido a la naturaleza no lineal del problema: el precio de las propiedades es fuertemente dependiente de la ubicación, representadas por puntos en un plano.

## Desempeño de los modelos

* **Lasso Regression**: R2(test set) = 0.534
* **Gradient Boosting Regressor**: R2(test set) = 0.897
* **Random Forest Regressor**: R2(test set) = 0.871
* **KNN Regressor**: R2(test set) = 0.853

## Puesta en producción

En este paso, el modelo se hace accesible mediante una página web utilizando **Dash** como *framework*. La puesta en producción se realizó utilizando **Google Cloud Run**, el servicio *serverless* de Google. Este servicio se encarga de gestionar el contenedor Docker generado para la página.

En la página principal se presentan los *inputs* para el modelo y adicionalmente se presenta un **Dashboard** interactivo en el cual se puede explorar con mayor detalle la base de datos usada para entrenar el modelo.

<img src="images/app1.png" alt="Alt text 1" width="300"/>  <img src="images/app2.png" alt="Alt text 1" width="300"/>

## Siguientes pasos

Es necesario recabar más datos para ampliar el rango de precios y las categorias de propiedades cubiertas por el modelo. Con más datos se puede cubrir propiedades por encima de los US $130 000, límite actual del modelo, y además se puede incluir terrenos, quintas y casas de varios pisos en el mismo. 

También, con una recolección de datos más amplia, es posible extender el análisis para cubrir otras ciudades en el país.

## API

Para mayor detalle: [Link al repositorio de la API](https://github.com/a-jimenezc/bienes_raices_scz_api "Clic para acceder al repositorio").


## Licencia 

GNU General Public License v2.0

## Autor

Antonio Jimenez Caballero

## Contacto

[Linkedin](https://www.linkedin.com/in/antonio-jimnzc/)

