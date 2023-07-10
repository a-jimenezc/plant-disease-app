import base64

def encode_image(image_path):
    """
    Encodes an image file into a base64 string.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The base64-encoded image string.
    """
    with open(image_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode("utf-8")
    return encoded_string
