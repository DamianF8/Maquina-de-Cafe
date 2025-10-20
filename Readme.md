La función verificar_recursos() recibe el valor ingresado por el usuario (la elección de la bebida) y
lo usa para buscar dentro del diccionario principal menu el conjunto de ingredientes y precio correspondientes
a esa bebida.

```python
bebida = menu[eleccion]
```

Aquí, la variable bebida pasa a contener un diccionario interno con los valores específicos de agua, café, leche y
precio que corresponden a la bebida seleccionada.
De esta manera, bebida no es solo el nombre de la bebida, sino un pequeño diccionario con toda la información necesaria para preparar esa opción.
