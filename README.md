## Servicio web de Scopus

### Host
IP del contenedor donde se aloja el servicio

### Métodos
#### Verbo HTTP
GET
#### Ruta
/consultaScopus
#### Parámetros
- consulta : Consulta que se le hace a scopus (string) (ejemplo: Heart) 
- limite : Cantidad de papers que va a devolver scopus en el xml, solo una pequena porcion de estos seran desgargados. (integer) 
- user : Usuario de vigtech que hace la consuluta (string) 
- proyecto : proyecto de vigtech al que corresponde la consulta (string)
#### Respuesta
Json que contiene los títulos y los eids de los papers que fueron descargados.
(Adicionalmente el servicio descarga estos archivos y un xml con los metadados correspondientes a la cantidad de archivos definida por 'limite').





