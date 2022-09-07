given_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] #Sitedeki örneği kullandım. 

def number_of_list_elements(liste1):
    
    """
    Listenin liste tipinde elemanlar içerip içermediğini ve eğer içeriyorsa sayısını tespit eden fonksiyon.
    """
    i = 0
    for e in liste1:
        if (type(e) == list):
            i += 1
    return i

def flat(duz_liste):
    """
    Tespit edilen liste tipindeki elemanların düzleştirilmesini sağlayan fonksiyon.
    """
    
    free = []
    
    for element in duz_liste:
        if (type(element) == list):
            flatten_list = [e for e in element]
            free += flatten_list
        else:
            free.append(element)
    
    return free
        
while(number_of_list_elements(given_list) != 0):
    given_list = flat(given_list)

print(given_list)
