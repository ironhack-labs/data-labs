Link : https://app.youneedabudget.com/46c718b9-f242-4d73-8541-440fa0c82a31/budget/
Contexto:
Es una pagina que te permite crear un control de ingresos y egresos, utilizando varios tipos de cuentas.
Mi API crea dos dataframes, uno de todas la cuentas,donde se pueden ver los balances de cada una y crea un total de los balances de todas, y otro de todos los gastos que se esperan generar en el mes.
Mi SCRAP contien informacion de la documentacion de YNAB para python.

Proceso : 

Lo primero fue crear una cuenta y generar mi access token para tener acceso a la funciones para extraer la informacion que necesitaba, despues importe las librerias necesarias para utilizar las funciones y finalmente empece a codear.

Cree mis DataFrames de las cuentas y gastos y para esto y quite todas las columnas y filas que no tenian informacion relevante de cada uno, todas las categorias tenian dentro gastos con valores iguales 0, y para removerlos tenia que acceder a cada categoria y manejerlas por seperado, al final genere dataframes unicamente con la informacion relevante.

Junte todos los data frames con la informacion que queria.(Quite valores nulos y multiplique los valores por 0.001 ya que al extraerlos todos los valores estaban en miliunidades) y obtuve mis dos DataFrames finales

Al modificar un valor en la pagina principal de Budget mis DataFrames tambien se actualizan.

Cabe recalcar que si genero una cuenta nueva, esta no se podra ver ya que cada cuenta genera un access_id y se tiene que dar de alta en el codigo.
