from PIL import Image
arr_fon = []
arr_countour =[]
def Search():
    image = Image.open("../data/1.jpg")

    pixels = image.load()

    width = image.size[0]
    height = image.size[1]
    img = Image.new('RGB', (width, height))
    img.putpixel((2,3), 900)
    print(pixels[0,0])

    draw_countour(width, height)
    img.show()


def draw_countour(width, height):
    img = Image.new('RGB', (width, height))


    for pixel in arr_countour:
        img.putpixel(pixel[0],900)
    img.show()
def create_map(photo):
    link = "../data/"
    image = Image.open(link+photo)

    pixels = image.load()

    width = image.size[0]
    height = image.size[1]
    return pixels, width, height

def Backward(width, height, pixels):
    p_s = p_active = search_start_p(width, height, pixels)
    p_n1 = search_clockwise(p_s)
    p_n2 = search_conter_clockwise(p_s)
    if p_n1 == p_n2:
        arr_fon.append(p_active)
        Backward(width, height, pixels)
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
        Backward(width, height, pixels)


def search_start_p(width, height, pixels):
 for i in range(width):
    for j in range(height):
       if pixels[i, j] != (1, 1, 1) and [i, j] not in arr_fon:
           return [i, j]
def search_clockwise(pixel):
    pass #OLES
def search_conter_clockwise(pixel):
    pass #OLES
def search_coutour_neighbour (pixel):
    pass #OLES
class BackwardBoundaryTracing():
    def __init__(self):
        pass

    def draw_countour(self, width, height):
        img = Image.new('RGB', (width, height))

        for pixel in arr_countour:
            img.putpixel(pixel[0], 900)
        img.show()

    def create_map(self,photo):
        link = "../data/"
        image = Image.open(link + photo)

        pixels = image.load()

        width = image.size[0]
        height = image.size[1]
        return pixels, width, height

    def Backward(self,width, height, pixels):
        p_s = p_active = search_start_p(width, height, pixels)
        p_n1 = search_clockwise(p_s)
        p_n2 = search_conter_clockwise(p_s)
        if p_n1 == p_n2:
            arr_fon.append(p_active)
            Backward(width, height, pixels)
        elif p_n1 != p_n2:
            p_end = p_s
            p_active = p_n1
            arr_countour.append(p_n1)
        while True:
            p_contour_neighbour = search_coutour_neighbour(p_active)
            if p_contour_neighbour != p_end:
                break
            if p_contour_neighbour in arr_countour and p_contour_neighbour != p_end:
                arr_countour.remove(p_contour_neighbour)
                arr_fon.append(p_contour_neighbour)
                p_active = arr_countour[-1]
            else:
                arr_countour.append(p_contour_neighbour)

        if p_contour_neighbour == p_end and len(arr_countour) > 1:
            return arr_countour
        else:
            Backward(width, height, pixels)

    def search_start_p(self, width, height, pixels):
        for i in range(width):
            for j in range(height):
                if pixels[i, j] != (1, 1, 1) and [i, j] not in arr_fon:
                    return [i, j]

    def search_clockwise(self,pixel):
        pass  # OLES

    def search_conter_clockwise(self,pixel):
        pass  # OLES

    def search_coutour_neighbour(self,pixel):
        pass  # OLES