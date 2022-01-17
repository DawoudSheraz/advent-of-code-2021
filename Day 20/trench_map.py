
from copy import deepcopy

PIXEL_MAP = {
    '.': '#',
    '#': '.'
}


def add_dark_pixel_boundary(image, max_x, max_y, pixel_to_add):
    """
    Helper method to add dark pixels around the image. This caters for the
    infinite size part. Each enhancement of the image only alters the image's boundary
    and not the entire infinite area.
    """
    new_x = max_x + 2
    new_y = max_y + 2
    image_list = []
    for y in range(0, new_y):
        out_list = []
        for x in range(0, new_x):
            if x == 0 or y == 0 or x == (new_x-1) or y == (new_y-1):
                out_list.append(pixel_to_add)
            else:
                out_list.append(image[y-1][x-1])
        image_list.append(out_list)
    return image_list


def get_pixel_value(image, x, y, neighbor_pixel_value):
    try:
        return image[y][x]
    except IndexError:
        return neighbor_pixel_value


def get_lit_pixel_count(image_list):
    count = 0
    for rows in image_list:
        for col in rows:
            if col == '#':
                count += 1
    return count


def enhance_image(input_img, algo, neighbor_pixel_value):
    output_img = deepcopy(input_img)

    for y, row in enumerate(input_img):
        for x, _ in enumerate(row):
            bin_str = ''
            for y_factor in range(y-1, y+2):
                for x_factor in range(x-1, x+2):
                    bin_str += get_pixel_value(input_img, x_factor, y_factor, neighbor_pixel_value)
            bin_str = bin_str.replace('#', '1').replace('.', '0')
            algo_index = int(bin_str, 2)
            output_img[y][x] = algo[algo_index]

    return output_img


def enhance(input_str, enhancements=2):
    data = input_str.splitlines()
    algo = data[0]
    image = data[2:]
    pixel_to_add = '.'
    for enhancement in range(enhancements):
        y_length = len(image)
        x_length = len(image[0])
        output = add_dark_pixel_boundary(image, x_length, y_length, pixel_to_add)
        image = enhance_image(output, algo, pixel_to_add)
        # If the first character in algo is #, each enhancement essentially flips the
        # the image b/w # and . Therefore, it is important to toggle the pixel value to add
        # on boundary and the neighbors when out of bounds b/w # and .
        # Thanks Reddit groups for this hint, that was dirty trick. I could not
        # figure it out and spent a good deal of time bashing my code.
        if algo[0] == '#':
            pixel_to_add = PIXEL_MAP[pixel_to_add]

    return get_lit_pixel_count(image)


with open('input.in', 'r') as f:
    print(enhance(f.read(), 50))
