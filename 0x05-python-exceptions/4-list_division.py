#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
      Args:
      my_list_1 (list): The first list.
      my_list_2 (list): The second list.
      list_length (int): The number of elements to divide.
      Returns:
      A new list of length list_length containing all the 
      divisions.
    """
    length = []
    if (list_length > len(my_list_1) or list_length > len(my_list_2)):
        maxi = list_length
    else:
        maxi = max(len(my_list_1), len(my_list_2))
    for i in range(maxi):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("Division by 0")
            result = 0
        except IndexError:
            print("Out of range")
            result = 0
        except TypeError:
            print("Wrong type")
            result = 0
        finally:
            length.append(result)
    return length
