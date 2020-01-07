# 1/6/20

# This does not fulfills the lowest cost criteria, and doesn't incldue k connections. I think a trie is the best way to do this? Challenging.
# ------------------

# You are given a huge list of airline ticket prices between different cities around the world on a given day. 
# These are all direct flights. Each element in the list has the format (source_city, destination, price).

# Consider a user who is willing to take up to k connections from their origin city A to their destination B.
#  Find the cheapest fare possible for this journey and print the itinerary for that journey.

# For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are as follows:

# [
#     ('JFK', 'ATL', 150),
#     ('ATL', 'SFO', 400),
#     ('ORD', 'LAX', 200),
#     ('LAX', 'DFW', 80),
#     ('JFK', 'HKG', 800),
#     ('ATL', 'ORD', 90),
#     ('JFK', 'LAX', 500),
# ]
# Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.

class Solution:
    def main(self, start, end, k):
        print(f'To go from {start} to {end} in less that {k} connections:')
        # Input
        itineraries = []
        cost = []
        possibleFlights = [
            ('JFK', 'ATL', 150),
            ('ATL', 'SFO', 400),
            ('ORD', 'LAX', 200),
            ('LAX', 'DFW', 80),
            ('JFK', 'HKG', 800),
            ('ATL', 'ORD', 90),
            ('JFK', 'LAX', 500),
        ]
        # Already there
        for flight in possibleFlights:
            if start == end:
                return print('Already there.')

        # Simple case - direct flight
        for flight in possibleFlights:
            if flight[0] == start:
                if flight[1] == end:
                    itineraries.append([flight[0], flight[1]])
                    cost.append([flight[2]])
                    return print(itineraries[0], cost[0])

        # No direct flights
        for i, flight in enumerate(possibleFlights):
            if flight[0] == start:
                for j, flight2 in enumerate(possibleFlights):
                    if flight[1] == flight2[0] and flight2[1] == end:
                        itineraries.append([possibleFlights[i][0], possibleFlights[j][0], possibleFlights[j][1]])
                        cost.append(possibleFlights[i][2] + possibleFlights[j][2])
                        return print(itineraries[0], cost[0])
        return print("No possible itinerary.")


if __name__=="__main__":
    Solution.main(None, 'JFK', 'HKG', 3)
    Solution.main(None, 'LAX', 'SFO', 2)
    Solution.main(None, 'HKG', 'SFO', 1)
    Solution.main(None, 'JFK', 'ORD', 3)
    Solution.main(None, 'SFO', 'SFO', 2)
    Solution.main(None, 'LAX', 'ATL', 3)
    Solution.main(None, 'ATL', 'LAX', 3)