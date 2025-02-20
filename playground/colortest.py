
def find_peaks(list_of_pixels):
    """Find peaks

    Find local maxima for a given list of intensities. 
    Intensities are defined as local maxima if the 
    intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.

    Args:
        list_of_intensities (list of tuples): a list of
            rgb tuples

    Returns:
        list of floats: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)
    """
    max_value = 0
    list_of_maxima = []
    list_of_intensities = []
    
    for pixel in list_of_pixels:
        list_of_intensities.append(sum(pixel))
    for pos, element in enumerate(list_of_intensities):
        if pos == 0:
            continue
        if pos == len(list_of_intensities) - 1:
            continue
        if list_of_intensities[pos - 1] > element < list_of_intensities[pos + 1]:
            max_value = element
            list_of_maxima.append(pos)
    return list_of_maxima
