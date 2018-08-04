import math

def calculate_distance(lon1, lat1, lon2, lat2):
    """
    :return: It returns the distance between two locations in meters
    """
    R = 6371e3  # meters
    φ1 = math.radians(lat1)
    φ2 = math.radians(lat2)
    Δφ = math.radians(lat2 - lat1)
    Δλ = math.radians(lon2 - lon1)

    a = math.sin(Δφ / 2) * math.sin(Δφ / 2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ / 2) * math.sin(Δλ / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    print("Distance is", d)
    return d


# print(calculate_distance(121.058805, 14.552797, 120.994260, 14.593999))
