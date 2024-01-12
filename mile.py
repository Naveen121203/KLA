def calculate_die_index_and_llc(wafer_diameter, die_size, die_shift_vector, reference_die_distance):
    die_index_and_llc = []

    num_dies_x = int(wafer_diameter / die_size[0])
    num_dies_y = int(wafer_diameter / die_size[1])

    reference_die_distance_x, reference_die_distance_y = reference_die_distance

    for i in range(num_dies_x):
        for j in range(num_dies_y):
            die_index = (i, j)

            llc_x = i * die_size[0] + die_shift_vector[0] + reference_die_distance_x - wafer_diameter / 2
            llc_y = j * die_size[1] + die_shift_vector[1] + reference_die_distance_y - wafer_diameter / 2

            # Check if the die is fully or partially within the wafer
            if (
                -wafer_diameter / 2 <= llc_x <= wafer_diameter / 2 - die_size[0] and
                -wafer_diameter / 2 <= llc_y <= wafer_diameter / 2 - die_size[1]
            ):
                die_index_and_llc.append((die_index, (llc_x, llc_y)))
            else:
                # Handle partially valid dies if needed
                pass

    return die_index_and_llc

wafer_diameter = 200
die_size = (10, 10)
die_shift_vector = (10, 10)
reference_die_distance = (25, 25)

result = calculate_die_index_and_llc(wafer_diameter, die_size, die_shift_vector, reference_die_distance)

for die in result:
    print(f"{die[0]}: ({die[1][0]:.4f}, {die[1][1]:.4f})")





