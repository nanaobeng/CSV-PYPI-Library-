import csv


def add_file(filename):
    file = {}
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if(line_count == 0):
                file["Columns"] = row
                line_count = line_count + 1
            else:
                file[line_count] = row
                line_count = line_count + 1
                
            
    return file
    
def getColumns(file):
    return(file["Columns"])

def isColumnPresent(column,file):
    x = file["Columns"]
        
    for i in x:
        
        if i == column:
            return True
        else:
            return False

def isValuePresent(value,file):
    for x in file:
        if value in file[x]:
            return True
        else:
            return False
def getColumnValues(column,file):
    x = file["Columns"]
    index = 0
    column_result = []
    
    for i in x:
        
        if i == column:
            
            for j in x:
                if(j==column):
                    for x in file:
                        column_result.append(file[x][index])
                        
                      
                else:
                    index = index + 1
                
                
             
            
            
        
        
            return(column_result)
    return "Heading does not exist"

def removeColumn(column,file):
    x = file["Columns"]
    index = 0
  
    
    for i in x:
        
        if i == column:
            
            for j in x:
                if(j==column):
                    for x in file:

                            del file[x][index]
                        
                      
                else:
                    index = index + 1
                
                
             
            
            
        
        
            return(file)
    return "Column does not exist"
    
def removeRow(value1,value2,file):
    index = 0
    key = ""
  
    
    for i in file:
        
        if "Mr" in file[i] and "Selbyen" in file[i]:
            print(i)
            key = i
    if key == "":
        pass
    else:
        del file[key]

    return(file)

        
        
def rowCount(file):
    return(len(file)-1)


def retrieveAll(file):
    data = []
    for i in file:
        data.append(file[i])
    return data
                
             
            
            
        
        
     
    
    

file = add_file('ss.csv')
#print(getColumns(file))
#print(isColumnPresent("Task Ordexr",file))
#print(isValuePresent("Title",file))
#print(getColumnValues("Gender",file))
#print(removeColumn("Title",file))
#print(removeRow("value1","value2",file))
#print(rowCount(file))
#print(retrievAll(file))

