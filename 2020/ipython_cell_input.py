import numpy
new_seat_state_equal = False

seat_state = numpy.array(seat_state_original)

x_dim_size = seat_state.shape[0]
y_dim_size = seat_state.shape[1]

while not new_seat_state_equal:

    # Blank slate to store the new seating. 
    # Since check for each seat happens all at once, hence we can't update the current layout
    new_seat_state = numpy.empty(shape=(x_dim_size,y_dim_size), dtype=str)
    
    # Iterate over each element and update seatings!
    for index, element in numpy.ndenumerate(seat_state):
        x_pos = index[0]
        y_pos = index[1]

        # Ignore if this is a floor tile
        if element == ".":
            new_seat_state[x_pos, y_pos] = "."
            continue

        # Check if the current seat is occupied or not
        current_seat_occupied = True if element == "#" else False

        nr_of_occupied_adjacent = 0
        for direction in adjacent:
            x_pos_adjacent = x_pos + direction[0]
            y_pos_adjacent = y_pos + direction[1]
            if isIndexOutOfBounds(x_pos_adjacent, y_pos_adjacent):
                continue;
            
            adjacent_tile = seat_state[x_pos_adjacent, y_pos_adjacent]
            if adjacent_tile == "#":
                nr_of_occupied_adjacent += 1
        
        # If current seat is not occupied and there are no adjacent seats occupied. Occupie the seat
        if not current_seat_occupied and nr_of_occupied_adjacent == 0:
            new_seat_state[x_pos, y_pos] = "#"

        elif current_seat_occupied and nr_of_occupied_adjacent >= 4:
            new_seat_state[x_pos, y_pos] = "L"
        
        else:
            new_seat_state[x_pos, y_pos] = element
    
    if numpy.array_equal(seat_state, new_seat_state):
        print("New seat state didn't change!")
        new_seat_state_equal = True

    # Update the seating to check for the next iteration
    seat_state = numpy.copy(new_seat_state)
