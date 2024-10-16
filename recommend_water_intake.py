from .basetool import BaseTool

class RecommendWaterIntake(BaseTool):
    name = "recommend_water_intake"
    description = "A tool to recommend daily water intake based on user weight"

    def __init__(self):
        super().__init__()

    # Handle arbitrary arguments like '__arg1'
    def _run(self, **kwargs) -> str:
        # Extract 'weight' from kwargs, handle '__arg1' if present
        weight = kwargs.get('weight') or kwargs.get('__arg1')
        
        if not weight:
            weight = float(input("Please enter your weight (in kg): "))
        else:
            weight = float(weight)  # Convert to float if it's passed as a string
        
        # Recommended water intake formula (rough estimate)
        water_intake = weight * 0.033
        return f"Your recommended daily water intake is: {water_intake:.2f} liters"

    async def _arun(self, **kwargs) -> str:
        # Asynchronous version not implemented
        raise NotImplementedError("Async run is not implemented yet.")
