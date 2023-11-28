TEQUILA_CURRENCY = "EUR"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, fly):
        self.stop_overs = 0
        self.via_city = ""
        self.airlines = fly["airlines"]
        self.availability = fly["availability"]["seats"]
        self.price = float(fly["conversion"][TEQUILA_CURRENCY])
        self.cityFrom = fly["cityFrom"]
        self.cityCodeFrom = fly["cityCodeFrom"]
        self.cityTo = fly["cityTo"]
        self.cityCodeTo = fly["cityCodeTo"]
        self.local_departure = fly["local_departure"]
        self.local_arrival = fly["local_arrival"]
        self.return_departure = ""
        self.return_arrival = ""
        self.nightsInDest = fly["nightsInDest"]
        self.stop_over = 0
        self.return_stop_over = 0
        self.via_city = []
        self.return_via_city = []
        self.route = []
        way_return = False
        for fly_route in fly["route"]:
            new_route = {
                "airline": fly_route["airline"],
                "cityFrom": fly_route["cityFrom"],
                "cityCodeFrom": fly_route["cityCodeFrom"],
                "cityTo": fly_route["cityTo"],
                "cityCodeTo": fly_route["cityCodeTo"],
                "local_arrival": fly_route["local_arrival"],
                "local_departure": fly_route["local_departure"]
            }
            self.route.append(new_route)
            if new_route["cityFrom"] == self.cityTo:
                way_return = True
                self.return_departure = new_route["local_departure"]
            if new_route["cityTo"] == self.cityFrom:
                self.return_arrival = new_route["local_arrival"]

            if new_route["cityFrom"] != self.cityFrom and new_route["cityFrom"] != self.cityTo:
                if way_return:
                    self.return_stop_over += 1
                    self.return_via_city.append(new_route["cityFrom"])
                else:
                    self.stop_over += 1
                    self.via_city.append(new_route["cityFrom"])

    def display(self):
        print(f"\nAirlines: {self.airlines}")
        print(f"Price: {self.price}")
        print(f"Availability: {self.availability}")
        print(f"From: {self.cityFrom} {self.cityCodeFrom}")
        print(f"To: {self.cityTo} {self.cityCodeTo}")
        if self.stop_over != 0:
            print(f"Via: {self.via_city} with {self.stop_over} stop over")
        if self.return_stop_over != 0:
            print(f"Return via: {self.return_via_city} with {self.return_stop_over} stop over")
        print(f"Departure: {self.local_departure}")
        print(f"Arrival: {self.local_arrival}")
        print(f"Return departure: {self.return_departure}")
        print(f"Return arrival: {self.return_arrival}")
        print(f"Nights in destination: {self.nightsInDest}")
        for route in self.route:
            print(f"\nAirline: {route['airline']}")
            print(f"From: {route['cityFrom']} {route['cityCodeFrom']}")
            print(f"To: {route['cityTo']} {route['cityCodeTo']}")
            print(f"Departure: {route['local_departure']}")
            print(f"Arrival: {route['local_arrival']}")

    def build_message(self):
        message = (f"Title: Low price alert! Only {self.price}€ to fly from {self.cityFrom}-{self.cityCodeFrom}"
                   f"to {self.cityTo}-{self.cityCodeTo}"
                   f"from {self.local_departure} to {self.local_arrival}")
        if self.stop_over != 0:
            message += f"Flight has {self.stop_over} stop over, via {self.via_city}."
        elif self.return_stop_over != 0:
            message += f"Flight has {self.return_stop_over} return stop over, via {self.return_via_city}."
        return message
