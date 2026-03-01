from shapely import Point, Polygon

def is_in(long, lat, area_coords):
    point = Point(long, lat)
    area = Polygon(area_coords)

    if area.contains(point):
        return True
    else:
        return False

if __name__ == "__main__":

    hagersten_coords = [(17.9467343,59.287934),
                    (17.9379569,59.303844),
                    (18.0076911,59.320101),
                    (18.0414431,59.308723),
                    (17.9847621,59.287582)]

    staden_coords = [(17.9023521, 59.295544),
                    (18.0020611, 59.363135),
                    (18.0971011, 59.369088),
                    (18.1686171, 59.323611),
                    (18.1612161, 59.251646),
                    (18.0854581, 59.221866)]
    
    is_in(18.0259821, 59.351278, hagersten_coords)