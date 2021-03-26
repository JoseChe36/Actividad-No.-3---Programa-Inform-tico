import re

salir = False
while salir == False:
    while True:
        
        filename='Apoyo.txt'
        textfile=open(filename, "r")
        
        regex = "int\s"
        reg = re.compile(regex)
        for line in textfile:
            
            resultint = 0
            resultint = len(reg.findall(line))
        textfile.close()
        filename = "Apoyo.txt"
        textfile = open(filename, "r")
        
        regex = "double\s"
        reg = re.compile(regex)
        for line in textfile:
            
            resultdouble = 0
            resultdouble = len(reg.findall(line))
        textfile.close()
        filename = "Apoyo.txt"
        textfile = open(filename, "r")
        
        regex = "string\s"
        reg = re.compile(regex)
        for line in textfile:
            
            resultstring = 0
            resultstring = len(reg.findall(line))
        textfile.close()
        filename = "Apoyo.txt"
        textfile = open(filename, "r")
        
        regex = "boolean\s"
        reg = re.compile(regex)
        for line in textfile:
            
            resultboolean = 0
            resultboolean = len(reg.findall(line))
        textfile.close()
       
        if resultint >= 1:
            filename = "Apoyo.txt"
            textfile = open(filename, "r")
            regex = "(int\s[\w(\w\d)]+\s?\=\s?[\d|\w]+\s?[\+|\*|\-|\/]\s?[\d|\w]+;)|(int\s[\w(\w\d)]+\s?\=\s?[\d|\w]+;)|(int\s[\w(\w\d)]+;)"
            reg = re.compile(regex)
            for line in textfile:
                
                intvalor = 0
                intvalor = len(reg.findall(line))
                if intvalor >= 1:
                    print("Tarea finalizada")
                else:
                    print("Error---Asignacion incorrecta---")
            textfile.close()
            salir = True
            break
        
        if resultdouble >= 1:
            filename = "Apoyo.txt"
            textfile = open(filename, "r")
            
            regex2 = "(double\s[\w(\w\d)]+\s?\=\s?[\d\.\d|\w]+\s?[\+|\*|\-|\/]\s?[\d\.\d|\w]+;)|(double\s[\w(\w\d)]+\s?\=\s?[\d\.\d|\w]+;)|(double\s[\w(\w\d)]+;)"
            reg = re.compile(regex2)
            for line in textfile:
                doublevalor = 0
                doublevalor = len(reg.findall(line))
                if doublevalor >= 1:
                    print("Tarea finalizada")
                else:
                    print("Error---Asignacion incorrecta---")
            textfile.close()
            salir = True
            break
        
        if resultstring >= 1:
            filename = "Apoyo.txt"
            textfile = open(filename, "r")
           
            regex3 = "(string\s[\w(\w\d)]+\s?\=\s?\"[\w\W]+\"[\s?\+\s?\"[\w\W]+\"]*;)|(string\s[\w(\w\d)]+\s?\=\s?\"[\w\W]+\";)|(string\s[\w(\w\d)]+;)"
            reg = re.compile(regex3)
            for line in textfile:
                stringvalor = 0
                stringvalor = len(reg.findall(line))
                if stringvalor >= 1:
                    print("Tarea finalizada")
                else:
                    print("Error---Asignacion incorrecta---")
            textfile.close()
            salir = True
            break
        
        if resultboolean >= 1:
            filename = "Apoyo.txt"
            textfile = open(filename, "r")
            
            regex4 = "(^boolean\s\w+\s\=\strue\;$)|(^boolean\s\w+\s\=\s\d+\s(<|>|<=|>=)\s\d+\;$)|(^boolean\s\w+\;\n^[a-z]+\s\=\s\d+\s(<|>|<=|>=)\s\d+\;$)|(^boolean\s\w+\;\n^[a-z]+\s\=\strue\;$)"
            reg = re.compile(regex4)
            for line in textfile:
                booleanvalor = 0
                booleanvalor = len(reg.findall(line))
                if booleanvalor >= 1:
                    print("Tarea finalizada")
                else:
                    print("Error---Asignacion incorrecta---")
            textfile.close()
            salir = True
            break