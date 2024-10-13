import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values from lists of height and weight.

    Args:
    height (list[int | float]): List of heights in meters.
    weight (list[int | float]): List of weights in kilograms.

    Returns:
    list[float]: List of calculated BMI values.

    Raises:
    ValueError: If inputs are invalid or lists have different lengths.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise ValueError("Inputs must be lists")
    
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length")
    
    if not all(isinstance(h, (int, float)) for h in height) or \
       not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("All elements must be int or float")
    
    if any(h <= 0 for h in height) or any(w <= 0 for w in weight):
        raise ValueError("Heights and weights must be positive")

    height_array = np.array(height)
    weight_array = np.array(weight)
    
    bmi = weight_array / (height_array ** 2)
    return bmi.tolist()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMI values.

    Args:
    bmi (list[int | float]): List of BMI values.
    limit (int): The BMI limit to apply.

    Returns:
    list[bool]: List of boolean values indicating if BMI is above the limit.

    Raises:
    ValueError: If inputs are invalid.
    """
    if not isinstance(bmi, list) or not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("BMI must be a list of int or float")
    
    if not isinstance(limit, int):
        raise ValueError("Limit must be an integer")

    return [b > limit for b in bmi]

def main():
    height = [1.71, 1.65, 1.73, 1.81, 1.76]
    weight = [65.3, 58.4, 75.6, 72.3, 69.9]

    try:
        bmi_results = give_bmi(height, weight)
        print("BMI results:", bmi_results)
        
        limit = 25
        above_limit = apply_limit(bmi_results, limit)
        print(f"BMI above {limit}:", above_limit)
    except ValueError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
