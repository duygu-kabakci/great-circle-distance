from distance_calculate import Location, DistanceCalculate
import pytest

earth_radius = 6371
def test_great_circle_dist_between_two_points():
    test_dist_calc = DistanceCalculate(earth_radius)
    coord_x, coord_y = 53.339428, -6.257664
    test_x, test_y = 52.986375, -6.043701
    assert(test_dist_calc.great_circle_dist(Location(coord_x, coord_y), Location(test_x, test_y )) == pytest.approx(41.7687, 0.0001 ) )

def test_great_circle_dist_between_identical_points():
    test_dist_calc = DistanceCalculate(earth_radius)
    coord_x, coord_y = 53.339428, -6.257664
    assert(test_dist_calc.great_circle_dist(Location(coord_x, coord_y), Location(coord_x, coord_y )) == 0 )

def test_great_circle_dist_between_office_and_london():
    test_dist_calc = DistanceCalculate(earth_radius)
    coord_x, coord_y = 53.339428, -6.257664
    test_x, test_y = 51.509865, -0.118092
    assert(test_dist_calc.great_circle_dist(Location(coord_x, coord_y), Location(test_x, test_y )) == pytest.approx(463, 0.001 ) )