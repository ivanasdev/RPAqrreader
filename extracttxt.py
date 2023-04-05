


 #Se lee toda la cadena de 0 a 400 chars
        datos=data[:800]
        #se quitan signos y caracteres de la cadena 
        datos=datos.replace("[","").replace("]","").replace("'","").replace(".","")



        #NOMBRE
        serachname=int(datos.find("Nombre"))
        serachfin=int(datos.find("Apellido"))
        nameslice=serachname+6    
        nombreclean=datos[nameslice:serachfin:1]

        #Apellido Paterno
        searchap=int(datos.find("Apellido Paterno")) 
        searchapem=int(datos.find("Apellido Materno"))
        apdef=searchap+17
        apellidopaterno=datos[apdef:searchapem:1]

        #Apellido MAterno 
        searchapellido=int(datos.find("Apellido Materno"))
        searchfinam=int(datos.find("Identificador electrónico"))  
        amfind=searchapellido+17
        amdef=datos[amfind:searchfinam:1]
        print(datos[amfind:amfind:1])

        #ID ELECTRONICO
        searchie=int(datos.find("Identificador electrónico"))
        findfinie=int(datos.find("CURP"))
        ieslice=searchie+14
        iedef=datos[ieslice:findfinie:1]

        #CURP
        searchcurp=int(datos.find("CURP"))
        findendcurp=int(datos.find("Número de crédito"))
        curpslice=searchcurp+4
        curpdef=datos[curpslice:findendcurp:1]


        #Credito
        searchcredito=int(datos.find("Número de crédito"))
        fincredito=int(datos.find("BP"))
        creditoslice=searchcredito+17
        creditodef=datos[creditoslice:fincredito:1]

        #BP
        searchbp=int(datos.find("BP"))
        finbp=int(datos.find("Sucursal"))
        bpslice=searchbp+2
        bpdef=datos[bpslice:finbp:1]
   
        #Sucursal
        searchsucursal=int(datos.find("Sucursal"))
        finsucursal=int(datos.find("Saludos"))
        sucursalslice=searchsucursal+8
        sucursaldef=datos[sucursalslice:finsucursal:1]

        #CLEAN DATA
        nombrecliente=nombreclean.replace("\n","").replace(" ","")
        apellidopaterno=apellidopaterno.replace("\n","").replace(" ","")
        apelllidomaterno=amdef.replace("\n","").replace(" ","")
        curpofical=curpdef.replace("\n","").replace(" ","")
        ielectronico=iedef.replace("\n","").replace(" ","")
        bpagente=bpdef.replace("\n","").replace(" ","")
        numerocredito=creditodef.replace("\n","").replace(" ","")
        sucursalcredito=sucursaldef.replace("\n","").replace(" ","")

        print(nombrecliente)
        print(apellidopaterno)
        print(apelllidomaterno)
        print(ielectronico)
        print(curpofical)
        print(numerocredito)
        print(bpagente)
        print(sucursalcredito)