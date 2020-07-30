#DESCRIPTION

Programa que alerta sobre cambios en archivo Excel.
[Creo que puede resultar especialmente útil en aquellos ambientes de trabajo donde se tiene la costumbre de consolidar información mediante un archivo Excel que está en carpetas compartidas]



#CONFIGURACION

Al ejecutarse se quedará todo el tiempo revisando y solo se cerrará si no encuentra el archivo.
Las configuraciones se deben hacer en el archivo config.txt
 - io: ruta completa al archivo
 - sheet_name: nombre de la hoja
 - header: número de fila (comenzando por 0) donde comienza la tabla. Lo que este en esa fila se toma como nombre para las columnas.
 - delay: tiempo entre captura de datos para su comparación en segundos.
 *Todos los parámetros son obligatorios.
