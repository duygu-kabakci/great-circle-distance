from input_loader import ListOp

test_data = [{"latitude": "52.986375", "user_id": 6, "name": "Jane Xyz", "longitude": "-6.043701", "distance": 71},
        {"latitude": "54.1225", "user_id": 9, "name": "John Yyy", "longitude": "-8.143333", "distance": 21.5},
        {"latitude": "52.966", "user_id": 5, "name": "Lily Xxx", "longitude": "-6.463", "distance": 121.9}
        ]
def test_filter_json_list_all_passed():
    test_list_op = ListOp(test_data)
    distance_limit = 150
    assert(test_list_op.filter_data(distance_limit, "distance"))
    assert(len(test_list_op.data) == len(test_data))

def test_filter_json_list_no_passed():
    test_list_op = ListOp(test_data)
    distance_limit = 20
    assert(test_list_op.filter_data(distance_limit, "distance"))
    assert(len(test_list_op.data) == 0)

def test_filter_json_list_one_passed():
    test_list_op = ListOp(test_data)
    distance_limit = 50
    assert(test_list_op.filter_data(distance_limit, "distance"))
    assert(len(test_list_op.data) == 1)
    assert (test_list_op.data[0] == test_data[1] )

def test_filter_empty_list():
    test_list_op = ListOp([])
    distance_limit = 50
    assert(test_list_op.filter_data(distance_limit, "distance"))
    assert(len(test_list_op.data) == 0)

def test_filter_key_not_exists():
    test_list_op = ListOp(test_data)
    distance_limit = 50
    assert(not test_list_op.filter_data(distance_limit, "dist"))

def test_sort_by_key_asc():
    test_list_op = ListOp(test_data)
    key = "user_id"
    assert(test_list_op.sort_data(key))
    assert (test_list_op.data[0][key] == 5)
    assert (test_list_op.data[1][key] == 6)
    assert (test_list_op.data[2][key] == 9)

def test_sort_by_nonexist_key():
    test_list_op = ListOp(test_data)
    key = "userid"
    assert(not test_list_op.sort_data(key))

def test_get_name_id_of_customers():
    test_list_op = ListOp(test_data)
    result = test_list_op.getNameAndIDs()
    assert(result[0] == ("Jane Xyz", 6) )
    assert (result[1] == ("John Yyy", 9) )
    assert (result[2] == ("Lily Xxx", 5) )