from PIL import Image
import math

class BackwardBoundaryTracing:
    def __init__(self, photo):
        link = "../data/"
        self.img = Image.open(link + photo)
        self.image = self.img.load()

        self.cont = []
        self.fone = []
        self.height = self.img.size[1]
        self.width = self.img.size[0]
        self.path = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        self.end = None

    def start(self):
        self.tracing()
        self.draw_countour()

    def draw_countour(self):
        img = Image.new('RGB', (self.width, self.height))

        for pixel in self.cont:
            img.putpixel(pixel, (255, 255, 255))
        img.show()

    def tracing(self):
        active = self.find_start()
        neighbour_c = self.search_clockwise(active)
        neighbour_cc = self.search_cclockwise(active)
        index = 0
        while True:
            if neighbour_c != neighbour_cc:
                start = active
                self.cont.append(start)
                self.end = start
                self.cont.append(neighbour_c)
                active = neighbour_c
                while active != self.end:
                    pixik, x = self.search_clockwise(active, 1, index)
                    active = pixik
                    index = x
                    if active not in self.cont and active not in self.fone:
                        self.cont.append(active)
            else:
                while neighbour_c != neighbour_cc:
                    self.fone.append(active)
                    active = neighbour_c
                    neighbour_c = self.search_clockwise(active)
                    neighbour_cc = self.search_cclockwise(active)
            break


    def find_start(self):
        for i in range(self.width):
            for k in range(self.height):
                if not BackwardBoundaryTracing.is_grey(self.image[i, k]) and self.image[i, k] not in self.fone:
                    return (i, k)

    def search_clockwise(self, pixel, check=None, k=0):
        first, second = pixel
        if check:
            k = (k + 6) % 8
            for i in range(k, len(self.path) + k):
                try:
                    if i > len(self.path) - 1:
                        i -= len(self.path)
                    if not BackwardBoundaryTracing.is_grey(self.image[first + self.path[i][0], second + self.path[i][1]]):
                        if (len(self.cont) > 5 and (first + self.path[i][0], second + self.path[i][1]) == self.end) or (
                                (first + self.path[i][0], second + self.path[i][1]) not in self.cont and (
                            first + self.path[i][0], second + self.path[i][1]) not in self.fone):
                            self.cont.append((first, second))
                            return (first + self.path[i][0], second + self.path[i][1]), i
                except IndexError:
                    continue
            pix = self.cont.pop()
            self.fone.append(pix)
            return self.cont[-1], 0
        else:
            for i in self.path:
                try:
                    if not BackwardBoundaryTracing.is_grey(self.image[first + i[0], second + i[1]]) and (first + i[0], second + i[1]) not in self.cont:
                        return (first + i[0], second + i[1])
                except IndexError:
                    continue

    def search_cclockwise(self, pixel):
        first, second = pixel
        for i in range(0, -8, -1):
            try:
                if not BackwardBoundaryTracing.is_grey(self.image[first + self.path[i][0], second + self.path[i][1]]):
                    if (first + self.path[i][0], second + self.path[i][1]) not in self.cont:
                        return (first + self.path[i][0], second + self.path[i][1])
            except IndexError:
                continue

    @staticmethod
    def is_grey(rgb):
        return math.sqrt(rgb[0] ** 2 + rgb[1] ** 2 + rgb[2] ** 2) < 50
