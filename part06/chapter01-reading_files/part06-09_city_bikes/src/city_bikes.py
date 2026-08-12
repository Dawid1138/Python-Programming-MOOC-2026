def get_station_data(filename: str):
    station_dict = {}
    with open(filename) as file:

        for line in file:
            part = line.strip().split(";")
            if part[0] == "Longitude":
                continue
            station_dict[part[3]] = (float(part[0]), float(part[1]))

    return station_dict


def distance(stations: dict, station1: str, station2: str):
    import math
    longitude1 = stations[station1][0]
    latitude1 = stations[station1][1]
    longitude2 = stations[station2][0]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict):
    max_distance = 0
    for station1 in stations:
        for station2 in stations:
            if station1 != station2:
                current_distance = distance(stations, station1, station2)
                if current_distance > max_distance:
                    max_distance = current_distance
                    max_station1 = station1
                    max_station2 = station2
    return (max_station1, max_station2, max_distance)