# 1. Please complete the following:
#   Your First name and Last Name: Siwon Lee
#   Your Student ID: 261279717


# 2. Write your program here:
import random
import math

# 1. Constants
MIN_LAT = -90
MAX_LAT = 90
MIN_LONG = -180
MAX_LONG = 180
EARTH_RADIUS = 6378 # in kilometers
STORM_STEPS = 5
DEG_TO_RAD = math.pi / 180
WAVE_PROBABILITY = 0.2
WAYPOINT_TOLERANCE = 10
# suggested constant: ARRIVAL_RADIUS_KM

# 2. Calibrate the Compass: Degrees to Radians
def degrees_to_radians(degrees):
    '''
    Returns the angle in radians given the angle in degrees

    Parameters:
        degrees: a float
    Returns:
        conversion (float): the computed conversion from degrees to radians
    Examples:
    >>> degrees_to_radians(180)
    3.14
    >>> degrees_to_radians(90)
    1.57
    >>> degrees_to_radians(145)
    2.53
    '''
    radians = round(degrees * DEG_TO_RAD, 2)
    return radians


# 3. Acquire a Fix: Validate a Coordinate
def get_valid_coordinate(val_name, min_float, max_float):
    '''
    Returns a valid coordinate input given a value name, minimum float,
    and maximum float

    Parameters:
        val_name: a string
        min_float: a float
        max_float: a float
    Returns:
        coordinate_input (float): The computed coordinate input
    Examples:
    >>> get_valid_coordinate('latitude', -90, 90)
    What is your latitude? -100
    Invalid latitude
    What is your latitude? -87.6
    -87.6
    >>> get_valid_coordinate('longitude', -180, 180)
    What is your longitude? -180
    Invalid longitude
    What is your longitude? 68
    68.0
    >>> get_valid_coordinate('y_coordinate', -10, 20)
    What is your y_coordinate? 27
    Invalid y_coordinate
    What is your y_coordinate? 16
    16.0
    '''
    # No coordinate yet, so it's initially set to False to enter while loop
    correct_input = False

    while not correct_input:
        coordinate_input = float(input('What is your ' + val_name + '? '))

        # The coordinate must be within the given minimum and maximum values
        if min_float < coordinate_input < max_float:
            correct_input = True
            return coordinate_input

        else:
            print('Invalid', val_name)


# 4. Plot Our Position: Get GPS Location
def get_gps_location():
    '''
    Returns a valid latitude and longitude of the given gps location

    Parameters:
        None
    Returns:
        latitude (float): The computed latitude
        longitude (float): The computed longitude
    Examples:
    >>> get_gps_location()
    What is your latitude? -100
    Invalid latitude
    What is your latitude? 50
    What is your longitude? -200
    Invalid longitude
    What is your longitude? 0
    (50.0, 0.0)
    >>> get_gps_location()
    What is your latitude? 3.14
    What is your longitude? 2.2
    (3.14, 2.2)
    >>> get_gps_location()
    What is your latitude? 25.5
    What is your longitude? -180
    Invalid longitude
    What is your longitude? 0
    (25.5, 0.0)
    '''
    latitude = get_valid_coordinate('latitude', MIN_LAT, MAX_LAT)
    longitude = get_valid_coordinate('longitude', MIN_LONG, MAX_LONG)
    return latitude, longitude


# 5. Chart the Distance: Great-circle Calculator
def distance_two_points(latitude_1, longitude_1, latitude_2, longitude_2):
    '''
    Returns "the great-circle distance between two points on a sphere given
    their longitudes and latitudes" (source: wikipedia)

    Parameters:
        latitude_1: a float
        longitude_1: a float
        latitude_2: a float
        longitude_2: a float
    Returns:
        distance (float): the computed distance
    Examples:
    >>> distance_two_points(1, 1, 2, 2)
    90.18
    >>> distance_two_points(10, 10, 10, 10)
    0.0
    >>> distance_two_points(79, 22, 25, 159)
    8130.7
    '''
    # First, convert deg to rad
    latitude_1, longitude_1, latitude_2, longitude_2 = degrees_to_radians(
        latitude_1), degrees_to_radians(longitude_1), degrees_to_radians(
        latitude_2), degrees_to_radians(longitude_2)

    # Using the Haversine formula to calculate distance
    a = math.sin((latitude_2 - latitude_1) / 2) ** 2 + math.cos(
        latitude_1) * math.cos(latitude_2) * math.sin(
        (longitude_2 - longitude_1) / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = EARTH_RADIUS * c
    return round(distance, 2)


# 6. Helm Nudge: Apply Wave Impact to a Coordinate
def apply_wave_impact(position, min_float, max_float):
    '''
    Returns the position of a randomly generated wave impact given the
    wave's position and its boundary (a minimum and maximum value)

    Parameters:
        position: a float
        min_float: a float
        max_float: a float
    Returns:
        position (float): the computed position in the range [-1, 1)
    Examples:
    >>> apply_wave_impact(0, -5, 5)
    -0.9
    >>> apply_wave_impact(0, -5, 5)
    0.76
    >>> apply_wave_impact(0, -5, 5)
    -0.14
    '''
    # No value yet, so initially set to False to enter the while loop
    valid_number = False

    while not valid_number:
        added_value = 2 * random.random() - 1

        # New position must be within the given boundary (max and min float)
        if min_float < position + added_value < max_float:
            position = round(position + added_value, 2)
            valid_number = True
            return position


# 7. Wave Hit Event: Reorient and Recheck
def wave_hit_vessel(vessel_latitude, vessel_longitude):
    '''
    Returns a valid vessel position given the wave's position

    Parameters:
        vessel_latitude: a float
        vessel_longitude: a float
    Returns:
        vessel_latitude (float): the computed vessel latitude
        vessel_longitude (float): the computed vessel longitude
    Examples:
    >>> wave_hit_vessel(80, -17)
    (79.2, -17.83)
    >>> wave_hit_vessel(55.5, 127)
    (55.16, 127.61)
    >>> wave_hit_vessel(79.9, 57)
    (80.77, 57.06)
    '''
    vessel_latitude = apply_wave_impact(vessel_latitude, MIN_LAT, MAX_LAT)
    vessel_longitude = apply_wave_impact(vessel_longitude, MIN_LONG, MAX_LONG)
    return vessel_latitude, vessel_longitude


# 8. Helm Advance: Move Toward Waypoint
def move_toward_waypoint(current_latitude, current_longitude,
                         waypoint_latitude, waypoint_longitude):
    '''
    Returns a new location closer to the waypoint given the current
    latitude, current longitude, waypoint latitude, and waypoint longitude

    Parameters:
        current_latitude: a float
        current_longitude: a float
        waypoint_latitude: a float
        waypoint_longitude: a float
    Returns:
        new_latitude (float): the computed new latitude
        new_longitude (float): the computed new longitude
    Examples:
    >>> move_toward_waypoint(10, 10, 20, 25)
    (18.58, 22.88)
    >>> move_toward_waypoint(10, 10, 10, 10)
    (10.0, 10.0)
    >>> move_toward_waypoint(50, 100, -50, -100)
    (-41.55, -83.1)
    '''
    # random number in the range [1, 2)
    scale = 1 + random.random()

    new_latitude = round(current_latitude + (
            waypoint_latitude - current_latitude) / scale, 2)

    # Boundary checking the new latitude
    if new_latitude < MIN_LAT:
        new_latitude = MIN_LAT

    elif new_latitude > MAX_LAT:
        new_latitude = MAX_LAT

    new_longitude = round(current_longitude + (
            waypoint_longitude - current_longitude) / scale, 2)

    # Boundary checking the new longitude
    if new_longitude < MIN_LONG:
        new_longitude = MIN_LONG

    elif new_longitude > MAX_LONG:
        new_longitude = MAX_LONG

    return new_latitude, new_longitude


# 9. Bridge Console: Storm Run to Waypoint
def vessel_menu():
    '''
    Displays an interactive vessel menu. The menu allows the user to:
        1) Set a waypoint (latitude and longitude)
        2) Move toward the waypoint and reports its status (wave impact or not)
        3) Exit the program

    The program ends if either the distance between the waypoint and the vessel
    is within the waypoint tolerance or when the storm hits the vessel.

    Parameters:
        None
    Returns:
        None
    '''
    exit_loop = False
    is_waypoint_set = False
    storm_countdown = STORM_STEPS

    print("Welcome to the boat menu!")
    vessel_latitude, vessel_longitude = get_gps_location()

    while not exit_loop:
        print("Please select an option below:")
        print("1) Set waypoint")
        print("2) Move toward waypoint and Status report")
        print("3) Exit boat menu")
        pick_a_number = int(input("Choose: "))

        # If 1 is entered, then the program asks user to set a waypoint
        if pick_a_number == 1:
            print("Enter waypoint coordinates.")
            new_waypoint_latitude, new_waypoint_longitude = get_gps_location()
            print("Waypoint set to latitude of", new_waypoint_latitude,
                  "and longitude of", new_waypoint_longitude)
            is_waypoint_set = True

        # If 2 is entered, then the vessel travels towards the set waypoint
        elif pick_a_number == 2:
            if not is_waypoint_set:
                print("No waypoint set.")

            elif is_waypoint_set:
                vessel_latitude, vessel_longitude = move_toward_waypoint(
                    vessel_latitude, vessel_longitude,
                    new_waypoint_latitude, new_waypoint_longitude)
                print("Captain Log: Journeyed towards waypoint.")

                # 20% chance of wave impacting the vessel
                if random.random() < WAVE_PROBABILITY:
                    vessel_latitude, vessel_longitude = wave_hit_vessel(
                        vessel_latitude, vessel_longitude)
                    print("Captain Log: Wave impact recorded.")

                print("Current position is latitude of",
                      vessel_latitude, "and longitude of", vessel_longitude)

                distance_to_waypoint = distance_two_points(
                vessel_latitude, vessel_longitude,
                new_waypoint_latitude, new_waypoint_longitude)

                print("Distance to waypoint:", distance_to_waypoint, "km")

                # If distance is within threshold, then mission success
                if distance_to_waypoint <= WAYPOINT_TOLERANCE:
                    print(
                        "Mission success: waypoint reached before storm.")
                    exit_loop = True

                else:
                    storm_countdown -= 1
                    print("Storm T-minus:", storm_countdown)

                    # If storm hits before reaching threshold, mission fails
                    if storm_countdown <= 0:
                        print("Mission failed: storm hit before arrival.")
                        exit_loop = True

        # If 3 is entered, then the user exits program
        elif pick_a_number == 3:
            print("Console closed by captain.")
            exit_loop = True