from shapely import Point, Polygon

def is_in(long, lat, area_coords):
    point = Point(long, lat)
    area = Polygon(area_coords)

    if area.contains(point):
        return True
    else:
        return False

hagersten_coords = [(17.9467343,59.287934),
                  (17.9379569,59.303844),
                  (18.0076911,59.320101),
                  (18.0414431,59.308723),
                  (17.9847621,59.287582)]

sodermalm_coords = [(18.0655, 59.3260),
                    (18.0820, 59.3180),
                    (18.0750, 59.3050),
                    (18.0550, 59.2980),
                    (18.0200, 59.3050),
                    (18.0100, 59.3120),
                    (18.0200, 59.3230),
                    (18.0480, 59.3280),
]