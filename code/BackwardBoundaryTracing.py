from PIL import Image

arr_fon = []
arr_countour =[]
def backward():
    p_s = p_active = search_start_p()
    p_n1 = search_clockwise(p_s)
    p_n2 = search_conter_clockwise(p_s)
    if p_n1 == p_n2:
        arr_fon.append(p_active)
    elif p_n1 != p_n2:
        p_end = p_s
        p_active = p_n1
        arr_countour.append(p_n1)
    while True:
        p_contour_neighbour = search_coutour_neighbour (p_active)
        if p_contour_neighbour!= p_end:
            break
        if p_contour_neighbour in arr_countour and p_contour_neighbour != p_end:
            arr_countour.remove(p_contour_neighbour)
            arr_fon.append(p_contour_neighbour)
            p_active = arr_countour[-1]
        else:
            arr_countour.append(p_contour_neighbour)

    if p_contour_neighbour == p_end and len(arr_countour)>1:
        return arr_countour
    else:
        Backward()


def search_start_p():
    pass  #my code
def search_clockwise(pixel):
    pass #OLES
def search_conter_clockwise(pixel):
    pass #OLES
def search_coutour_neighbour (pixel):
    pass #OLES

img = Image.new( 'RGB', (250,250), "black")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = (i, j, 100)

img.show()
