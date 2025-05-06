def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """
    Adds optional prefix/suffix, capitalizes text, and trims to max length.
    """
    if capitalize:
        text = text.capitalize()

    # Combine parts
    result = prefix + text + suffix

    # Limit length if needed
    if max_length is not None:
        result = result[:max_length]

    return result

# Example usage
if __name__ == "__main__":
    print(format_text("hello", prefix=">>", suffix="<<", capitalize=True, max_length=10))
    # Output: >>Hello<<
