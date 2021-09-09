# Asks For User Input
miles = input('Enter a distance in miles: ')
# kilometers_value = miles_value * 1.609344

# Convert The Input From String To Integer
distance_in_miles = int(miles)

# Perform The Miles to Km Formula
distance_in_kilometers = distance_in_miles * 1.609344

# Reconvert the Distance in km to string to concatenate it with another string
print("Then Your Distance In Km Equals: "+str(distance_in_kilometers))
