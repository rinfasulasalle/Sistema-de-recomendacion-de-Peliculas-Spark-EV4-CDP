<div align="center">
    <table>
        <theader>
        <tr>
            <th>
            <img src="https://github.com/rescobedoulasalle/git_github/blob/main/ulasalle.png?raw=true" alt="EPIS" style="width:90%; height:auto"/>
            </th>
            <th>
            <span style="font-weight:bold;">UNIVERSIDAD LA SALLE</span><br />
            <span style="font-weight:bold;">FACULTAD DE INGENIERÍAS</span><br />
            <span style="font-weight:bold;">DEPARTAMENTO DE INGENIERÍA Y MATEMÁTICAS</span><br />
            <span style="font-weight:bold;">CARRERA PROFESIONAL DE INGENIERÍA DE SOFTWARE</span>
            </th>            
        </tr>
        </theader>
    </table>
</div>

<table>
    <theader>
        <tr>
        <th colspan="2">INFORMACIÓN BÁSICA</th>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td>ALUMNO:</td>
            <td>Roger Infa Sanchez</td>
        </tr>
        <tr>
            <td>CURSO:</td>
            <td>Computación Distribuida y Paralela</td>
        </tr>
        <tr>
            <td>DOCENTE:</td>
            <td>Renzo Mauricio Rivera Zavala  - rriveraz@ulasalle.edu.pe</td>
        </tr>
        <tr>
            <td>TAREA:</td>
            <td>Sistema de recomendación de Películas Spark </td>
        </tr>
        <tr>
            <td>DESCRIPCION:</td>
            <td>Crear una aplicación Spark que genere un sistema de recomendación de películas mediante el filtrado colaborativo. La aplicación debería poder recomendar películas a los usuarios en función de sus clasificaciones de películas.</td>
        </tr>
        <tr>
            <td colspan="2">RECURSOS:</td>
        </tr>
        <tr>
            <td colspan="2">
                <ul>
                <li><a href="https://sparkbyexamples.com/pyspark/spark-submit-python-file/?expand_article=1">How to Spark Submit Python | PySpark File (.py)?</a></li>
                <li><a href="https://spark.apache.org/docs/latest/">Documentacion de Spark</a></li>
                <li><a href="https://github.com/rescobedoulasalle/git_github/blob/main/ulasalle.png?raw=true">Logo La Salle</a></li>
                <li> Maquina Virtual proporcionada mediante Clasroom.
                </ul>
            </td>
        </tr>
    </tbody>
</table>

## Clonacion de maquinas virtuales y verifiacion adaptador NET
Las maquinas vituales son **Spark_Master_Node** y **Spark_Worker_Node1**
![Alt text](images/image-1.png)
Posterior verifiacremos sus adaptadores de red, primero de **Spark_Master_Node**
![Alt text](images\image-2.png)
Y luego de **Spark_Worker_Node1**
![Alt text](images/image-3.png)
Esto para que cada maquina virtual tenga su propia IP

## Cambiar nombre de host de la maquina clonada (Spark_Worker_Node1)
Para cambiar el nombre del Host se debe ejecutar en consola:
```bash
hostnamectl set-hostname worker1
```
![Alt text](images\image-4.png)

## Verificar variables de entorno en ambos nodos:
Primero en **Spark_Master_Node**
![Alt text](images\image-5.png)
Luego en **Spark_Worker_Node1**
![Alt text](images\image-6.png)

Y  ejecutamos para verificar
```bash
source ~/.bashrc
```
## Configurar archivo de ambiente de Cluster de Spark (solo Master Node)
Ejecutamos
```bas
nano $SPARK_HOME/conf/spark-env.sh
```
y agregaremos las siguientes lineas
```bash
export SPARK_MASTER_HOST=&lt;Direccion IP de nodo master&gt;
export SPARK_MASTER_PORT=7077
export SPARK_WORKER_INSTANCES=1
export SPARK_WORKER_CORES=2
export SPARK_WORKER_MEMORY=2g
export SPARK_WORKER_PORT=8888
```
![Alt text](images\image-7.png)

## Verificar o crear archivo de configuración de Spark (solo Master Node)
Para este paso necesitaremos conocer la IP de la maquina, pondremos
```bash
ip addr show
```
![Alt text](images/image-8.png)
En este caso la IP de **Spark_Master_Node** es **192.168.1.12**

Ejecutamos en Master
```bas
nano $SPARK_HOME/conf/spark-defaults.conf
```
y agregaremos la siguiente linea
```bash
spark.master spark://192.168.1.12:7077
```

## Iniciar nodo maestro (solo Master Node)
Ejecutamos 
```bas
start-master.sh
```
![Alt text](images\image-9.png)

## Verificar funcionamiento de nodo maestro (solo Master Node)
En el buscador ponemos la direccion ip del servidor y nos aparece una interfaz web que indica si todo esta bien configurado , em este caso ponemos
```bas
http://192.168.1.12:8080/
```
![Alt text](images\image-10.png)

## Iniciar nodo worker en maquina clonada (solo Worker Node)
En **Spark_Worker_Node1** podremos este comadno 
```bas
start-worker.sh spark://192.168.1.12:7077
```

![Alt text](images\image-11.png)
