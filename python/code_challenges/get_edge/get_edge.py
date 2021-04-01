# code from whiteboard...needs fixing??

def get_edge(graph,trip_list)

    cost = 0

    round_trip = False

    for city in trip_list:
        connected = graph.get_neighbor(city)
            for item in connected:
                if item[0] != city
                    return ('False. $0')
                else:
                    cost+= item[1]
                    round_trip = True

    print(f'{round_trip}. ${cost})
    return round_trip, cost