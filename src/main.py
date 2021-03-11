import argparse
import logging
from distance_calculate import Location, DistanceCalculate

from input_loader import InputReader, OutWriter

EARTH_RADIUS = 6371

def get_closer_customers(customer_data: list, target_location: Location, limit:int):
    dist_calc = DistanceCalculate(EARTH_RADIUS)
    customers = []
    for customer in customer_data:
        d = dist_calc.great_circle_dist(target_location, Location(customer.latitude, customer.longitude))
        if (d <= limit):
            customers.append(customer)
    return customers

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

    close_customers = get_closer_customers(customer_data, office_loc, args.distance)
    # sort by user_id
    close_customers = sorted(close_customers, key=lambda k: k.user_id)
    # get name and IDs
    results = list(map(lambda d: d.getNameAndIDs(), close_customers))

    #output names and user_ids
    OutWriter.output(args.output_name, results)
