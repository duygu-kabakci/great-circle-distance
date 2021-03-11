import argparse
import logging
from distance_calculate import Location, DistanceCalculate

from input_loader import InputReader, ListOp, OutWriter

EARTH_RADIUS = 6371

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s %(asctime)s] %(message)s')
    parser = argparse.ArgumentParser(description='Find closest customers')
    parser.add_argument('--customer-list', required=True, type=str,
                        help='input file path of customer information')
    parser.add_argument('--output-name', required=False, type=str, default="output.txt",
                        help='output file path')
    parser.add_argument('--distance', required=False, type= float, default=100,
                        help='distance limit to source in KM, default:100 KM')
    args = parser.parse_args()

    customer_data = InputReader.load_data(args.customer_list)

    office_coord_x,  office_coord_y= 53.339428, -6.257664
    office_loc = Location(office_coord_x, office_coord_y)
    dist_calc = DistanceCalculate(EARTH_RADIUS)
    #TODO: validate input has latitude and longitude all the time.
    for customer in customer_data:
        d = dist_calc.great_circle_dist(office_loc, Location(customer["latitude"], customer["longitude"] ) )
        customer["distance"] = d

    customer_ops = ListOp(customer_data)
    customer_ops.filter_data(args.distance, "distance")
    customer_ops.sort_data("user_id")
    results = customer_ops.getNameAndIDs()

    OutWriter.output(args.output_name, results)
