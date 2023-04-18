from . import prueba

consulta=prueba.Database()

#Tkinter | filtros | id | sad | añadir /filtro= id: sad

filtro= consulta.muestra(identificador= "SAD")



#Tkinter | filtros | ensayos | Tmin | >300 /filtro = { id: sad, tmin : >300}


filtroTkinter = { "id": "sad", "tmin" : ">300"}


#Tkinter | filtros | buscar 

resultado= consulta.buscar(filtro)































