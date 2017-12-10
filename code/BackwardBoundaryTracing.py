from PIL import Image


class BackwardBoundaryTracing:
    def __init__(self):
        self.arr_fon = []
        self.arr_countour = []

    def draw_countour(self, width, height):
        img = Image.new('RGB', (width, height))

        for pixel in self.arr_countour:
            img.putpixel(pixel[0], 900)
        img.show()

    def create_map(self,photo):
        link = "../data/"
        image = Image.open(link + photo)

        pixels = image.load()

        width = image.size[0]
        height = image.size[1]
        return pixels, width, height

    def backward(self,width, height, pixels):
        p_s = p_active = self.search_start_p(width, height, pixels)
        p_n1 = self.search_clockwise(p_s)
        p_n2 = self.search_conter_clockwise(p_s)
        if p_n1 == p_n2:
            self.arr_fon.append(p_active)
            self.backward(width, height, pixels)
        elif p_n1 != p_n2:
            p_end = p_s
            p_active = p_n1
            self.arr_countour.append(p_n1)
        while True:
            p_contour_neighbour = self.search_coutour_neighbour(p_active)
            if p_contour_neighbour != p_end:
                break
            if p_contour_neighbour in self.arr_countour and p_contour_neighbour != p_end:
                self.arr_countour.remove(p_contour_neighbour)
                self.arr_fon.append(p_contour_neighbour)
                p_active = self.arr_countour[-1]
            else:
                self.arr_countour.append(p_contour_neighbour)

        if p_contour_neighbour == p_end and len(self.arr_countour) > 1:
            return self.arr_countour
        else:
            self.backward(width, height, pixels)

    def search_start_p(self, width, height, pixels):
        for i in range(width):
            for j in range(height):
                if not self.black_pixel(pixels[i, j]) and [i, j] not in self.arr_fon:
                    return [i, j]

    def search_clockwise(self,pixel):
        pass  # OLES

    def search_conter_clockwise(self,pixel):
        pass  # OLES

    def search_coutour_neighbour(self,pixel):
        pass  # OLES

    @staticmethod
    def black_pixel(pixel):
        black = [(0 + i, 0 + i, 0 + i) for i in range(13)]
        return pixel in black

    # зберігати ключ пікселя, доробити пошук