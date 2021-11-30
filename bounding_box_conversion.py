

# Format 1 : Convert bounding boxes from boundary coordinates (x_min, y_min, x_max, y_max) to center-size coordinates (c_x, c_y, w, h)

def xy_to_cxcy(box_coordinates):
    c_x = (box_coordinates[0] + box_coordinates[2])/2
    c_y = (box_coordinates[1] + box_coordinates[3])/2
    w = box_coordinates[2] - box_coordinates[0]
    h = box_coordinates[3] - box_coordinates[1]
    return [c_x, c_y, w, h]


# Format 2 : Convert bounding boxes from center-size coordinates (x, y, w, h) to (x_min, y_min, x_max, y_max)

def cxcy_to_xy(box_coordinates):
    x_min = box_coordinates[0] -w/2
    x_max = box_coordinates[0] + w/2
    y_min = box_coordinates[1] - h/2
    y_max = box_coordinates[1] + h/2
