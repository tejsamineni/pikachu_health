from .basetool import BaseTool

class CalculateBMI(BaseTool):
    name = "calculate_bmi"
    description = "A tool to calculate BMI based on user input weight and height"

    def _run(self, **kwargs) -> str:
        # If weight and height are not provided in kwargs, ask for them
        if 'weight' not in kwargs:
            weight = input("Please enter your weight (in kg): ")
        else:
            weight = kwargs['weight']

        if 'height' not in kwargs:
            height = input("Please enter your height (in meters): ")
        else:
            height = kwargs['height']

        try:
            # Convert the provided weight and height to float
            weight = float(weight)
            height = float(height)
        except ValueError:
            return "Error: Weight and height must be valid numbers."
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        return f"Your BMI is: {bmi:.2f}"

    async def _arun(self, **kwargs) -> str:
        raise NotImplementedError("Async run is not implemented yet.")
