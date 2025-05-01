while True:
    # Read input variables
    reaTZon_y = float(input())
    PriceElectricPowerDynamic = [float(input()) for _ in range(49)]
    TDryBul= [float(input()) for _ in range(49)]

    # Normalized Desired Zone Temperature (21 C for comfort temp in residential buildings)
    desired_temp = 21 + 273.15
    temp_diff = desired_temp - reaTZon_y

    # Energy price forecast, absolute minimum price in the next hours
    min_price = min(PriceElectricPowerDynamic)

    # Increase the weight of the temperature difference in the formula
    # Reduce the impact of the minimum price and outdoor temperature
    if temp_diff >= 0.000000000000000000000000001:  # Lower the threshold to react as early as possible
        temp_diff *= 160  # Increase the weight of temp_diff to make the pump work more

    # Outdoor temperature forecast, absolute minimum in the next hours
    min_outdoor_temp = min(TDryBul)

    # Control based on the temperature difference, price and outdoor temperature
    oveHeaPumY_u = temp_diff*165 - min_price*0.000000000000000000000000001 - min_outdoor_temp  # Reduce the impact of min_price and outdoor temp

    # Compressor speed saturation
    if oveHeaPumY_u < 0:
        oveHeaPumY_u = 0
    elif oveHeaPumY_u > 1:
        oveHeaPumY_u = 1

    # Output the control signal
    print(oveHeaPumY_u)