import os
os.system('cls'if os.name == 'nt' else 'clear')


Departamentos= {
"0101": "Atlantida "  "La Ceiba",  
"0102": "Atlantida " "El Porvenir",  
"0103": "Atlantida " "Esparta ",
"0104": "Atlantida " "Jutiapa", 
"0105": "Atlantida " "La Masica", 
"0106": "Atlantida " "San Francisco",
"0107": "Atlantida " "Tela",
"0108": "Atlantida " "Arizona",
"0201": "Colon " "Trujillo",
"0202": "Colon " "Balfate",
"0203": "Colon " "Iriona", 
"0204": "Colon " "Limón", 
"0205": "Colon " "Sabá", 
"0206": "Colon " "Santa Fe", 
"0207": "Colon " "Santa Rosa de Aguán", 
"0208": "Colon " "Sonaguera", 
"0209": "Colon " "Tocoa", 
"0210": "Colon " "Bonito Oriental",
"0301": "Comayagua ""Comayagua", 
"0302": "Comayagua ""Ajuterique", 
"0303": "Comayagua ""El Rosario",
"0304": "Comayagua ""Esquías", 
"0305": "Comayagua ""Humuya", 
"0306": "Comayagua ""La Libertad", 
"0307": "Comayagua ""Lamaní", 
"0308": "Comayagua ""La Trinidad", 
"0309": "Comayagua ""Lejamaní", 
"0310": "Comayagua ""Meámbar", 
"0311": "Comayagua ""Minas de Oro", 
"0312": "Comayagua ""Ojos de Agua", 
"0313": "Comayagua ""San Jerónimo", 
"0314": "Comayagua ""San José de Comayagua",
"0315": "Comayagua ""San José del Potrero", 
"0316": "Comayagua ""San Luis",
"0317": "Comayagua ""San Sebastián", 
"0318": "Comayagua ""Siguatepeque", 
"0319": "Comayagua ""Villa de San Antonio", 
"0320": "Comayagua ""Las Lajas", 
"0321": "Comayagua ""Taulabé" 
}   
opcion = "S"
while opcion.upper() == "S":
    print("Ingrese su numero de cedula")
    cedula = input()

    if len(cedula) >= 8 :  
        try:
            ano = int(cedula[4:8])
            departamento = str(cedula[0:4])
            edad = 2024 - ano

            if departamento in Departamentos and ano <= 2024:  
                print("Su departamento es:", Departamentos[departamento], "\nSu edad es:", edad)
            else:
                print("Algo salio mal, vuelve a intentarlo")

        except ValueError:
            print("La cedula debe contener numeros validos para el año y el departamento")

        print("Desea ingresar otra cedula? S/N")
        opcion = input()

    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    


    
