Almacena en una variable name tu nombre.
name=Paula

Imprime esa variable.
echo $name


Crea un directorio nuevo que se llame como el contenido de la variable name.
mkdir $name


Elimina ese directorio.
rmdir $name


Por cada archivo dentro de la carpeta lorem imprime el número de carácteres que tienen sus nombres. Intenta primero mostrar los archivos mediante un bucle for

Imprime los ficheros
Imprime las longitudes de los nombres de los ficheros
Imprime outputs con la siguiente estructura: lorem has 5 characters lenght
for %f in lorem;


Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:
ps/ top

Muestra información sobre tu procesador por pantalla
uname -a

Crea 3 alias y haz que estén disponibles cada vez que inicias sesión

Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz
zip lorem-compressed.tar.gz lorem lorem-copy

Descomprime el archivo lorem-compressed.tar.gz en la carpeta lorem-uncompressed
tar -xvf lorem-compressed.tar.gz