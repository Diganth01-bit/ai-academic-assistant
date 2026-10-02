from langchain_core.tools import tool


@tool
def calculator(
    expression: str
) -> str:
    """
    Calculate a mathematical expression.

    Example:
    30 / 10
    """

    allowed_characters = (
        "0123456789+-*/(). "
    )

    if not all(
        character in allowed_characters
        for character in expression
    ):

        return "Invalid expression."

    try:

        result = eval(
            expression,
            {
                "__builtins__": {}
            },
            {}
        )

        return str(result)

    except Exception:

        return "Calculation failed."