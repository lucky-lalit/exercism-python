"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return(record[-1])
 
        
def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)
    # for item in coordinate:
    #     new_coordinate = tuple()


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    new_azara_record = tuple(azara_record[-1])
    # print(azara_record)
    # print(new_azara_record)
    # print(type(azara_record))
    # print(type(new_azara_record))
    # print(azara_record[-1],azara_record[-2])
    # print(new_azara_record[-1],new_azara_record[-2])
    # print((new_azara_record[-2] and new_azara_record[-1]) in rui_record)
    if (new_azara_record in rui_record):
        return True
    else:
        return False
    pass


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    # print(type(azara_record))
    if compare_records(azara_record,rui_record):
        return azara_record + rui_record
    else:
        return 'not a match'
    pass


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    result = ''
    print(len(combined_record_group))
    for item in combined_record_group:
        new_record = item[:1] + item[2:]
        print('debug1',new_record)
        print('debug2',type(result),result)
        # break
        result = result + (str(new_record)+'\n')
        
        # result
        print(result)
    return result

        # if compare_records()

    pass
