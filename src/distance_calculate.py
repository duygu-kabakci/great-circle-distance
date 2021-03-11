from math import radians, cos, sin, acos

# Holds latitude and longitude of corrdinates
class Location:
    def __init__(self, latitude: str, longitude: str):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
    def degree_to_radians(self):
        return radians(self.latitude), radians(self.longitude)

# Holds the logic to calculate great circle distance of two coordinates
class DistanceCalculate:
    def __init__(self, r: float ):
        """

        :type r: float
        """
        self.radius = r
    # Calculates circle distance using the first formula from https://en.wikipedia.org/wiki/Great-circle_distance
    def great_circle_dist(self, loc1: Location, loc2: Location) -> float:
        x1, y1 = loc1.degree_to_radians() #(latitude, longtitude ) order
        x2, y2 = loc2.degree_to_radians()

        central_angle = acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(abs(y1-y2)) )
        distance = central_angle * self.radius
        return distance
