from math import radians, cos, sin, acos

EARTH_RADIUS = 6367445  # meters


def get_distance(lat_a_deg, lgt_a_deg, lat_b_deg, lgt_b_deg):
    """
        Get the distance, in meters, between two points which geolocation is known
    """
    lat_a = radians(lat_a_deg)
    lgt_a = radians(lgt_a_deg)
    lat_b = radians(lat_b_deg)
    lgt_b = radians(lgt_b_deg)

    return EARTH_RADIUS * acos(sin(lat_a) * sin(lat_b) + cos(lat_a) * cos(lat_b) * cos(lgt_a - lgt_b))


def get_element_as_json(name, distance=None, lat=None, long=None):
    return {
        "name": name,
        "distance": distance,
        "latitude": lat,
        "longitude": long
    }
