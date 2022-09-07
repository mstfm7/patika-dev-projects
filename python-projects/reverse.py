given_list = [[1, [2,5,[3,9,7]]], [3,[9,1,0,3,[7,2]] ,4], [5, 6, 7]] #Sitedeki örneğin biraz daha zorlaştırılmış halini kullandım.

def reversing(list1):
    """
    Listeyi tersine çeviren fonksiyon
    """
    return [e for e in list1[(len(list1)-1): : -1]]

def find_nestedLists(liste):
    """ 
    Nested listeleri bulup reversing fonksiyonu kullanımıyla tersine çeviren fonksiyon.
    """
    for i in range(len(liste)):
        if isinstance(liste[i], list):
            liste[i] = reversing(liste[i])
            liste[i] = find_nestedLists(liste[i])
    
    return liste

given_list = reversing(given_list)

given_list = find_nestedLists(given_list)

print(given_list)

