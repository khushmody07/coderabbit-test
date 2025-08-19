# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverse the characters in a string.
    
    Parameters:
        text (str): Input string to reverse.
    
    Returns:
        str: A new string containing the characters of `text` in reverse order.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the number of whitespace-delimited words in a sentence.
    
    Splits the input using Python's default str.split() (splits on any whitespace)
    and returns the length of the resulting list. An empty or all-whitespace
    string yields 0.
    
    Parameters:
        sentence (str): Input text to measure. Must support the `.split()` method.
    
    Returns:
        int: Number of words found.
    
    Raises:
        AttributeError: If `sentence` does not have a `split` method.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (int | float): Temperature in degrees Celsius.
    
    Returns:
        float: Equivalent temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32
