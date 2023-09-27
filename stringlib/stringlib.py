def basic_capitalize(data: str) -> str:
    # Check if the input is None or not a string
    if data is None or not isinstance(data, str):
        return data  # Return the input as is

    return data.capitalize()  # Capitalize the string if it's a valid string
