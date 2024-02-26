def round_decimals(number, decimal_places):
    error = "Error: Number of decimal places must be positive!"
    if decimal_places < 0:
        return error
    number_list = []
    number_string = str(number)
    for i in number_string:
        number_list.append(i)
#    print(number_list)
    rounded_list = []
    index_of_decimal_point = number_list.index(".")
    no_of_characters = index_of_decimal_point + decimal_places
    for place in range(0, no_of_characters + 1):
        rounded_list.append(number_list[place])
    if "e" in number_list:
        index_of_e = number_list.index("e")
        length_of_list = len(number_list)
        for character in range(index_of_e, length_of_list):
            rounded_list.append(number_list[character])
    if int(number_list[no_of_characters + 1]) >= 5:
        old_value = number_list[no_of_characters]
        if old_value == ".":
            old_value = number_list[no_of_characters - 1]
            rounded_list.remove(".")
            new_value = str(int(old_value) + 1)
            rounded_list[no_of_characters - 1] = new_value
        else:
            new_value = str(int(old_value) + 1)
            rounded_list[no_of_characters] = new_value
#        print(rounded_list)
        x = decimal_places
        y = index_of_decimal_point
        while x > 0:
            if rounded_list[x + y] == "10":
                rounded_list[x + y] = "0"
                old_value = rounded_list[x + y - 1]
                new_value = str(int(old_value) + 1)
                rounded_list[x + y - 1] = new_value
                x -= 1
            else:
                x -= 1
    if decimal_places == 0 and "." in rounded_list:
        rounded_list.remove(".")
    final_number_string = ""
    if decimal_places == 0:
        rounded_value = int(final_number_string.join(rounded_list))
    else:
        rounded_value = float(final_number_string.join(rounded_list))
    return rounded_value


SPEED_OF_LIGHT = 3e8
ELECTRONVOLT = 1.602e-19
PLANCK_CONSTANT = 6.626e-34
n1 = 2
n2 = 1

energy_state_1 = (-13.6/n1**2)
energy_state_2 = (-13.6/n2**2)
photon_energy_in_eV = energy_state_1 - energy_state_2
photon_energy_in_J = photon_energy_in_eV * ELECTRONVOLT
frequency = (photon_energy_in_J / PLANCK_CONSTANT)
wavelength = SPEED_OF_LIGHT / frequency

print(f"{wavelength} nm\n...or...")
print(f"{round_decimals(wavelength, 2)} m")
wavelength_in_nm = wavelength * 1000000000
print(f"{wavelength_in_nm} nm\n...or...")
print(f"{round_decimals(wavelength_in_nm, 0)} nm")
