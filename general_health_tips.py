from .basetool import BaseTool

class GeneralHealthTips(BaseTool):
    name = "general_health_tips"
    description = "A tool to provide general health tips"

    def __init__(self):
        super().__init__()

    # Handle arbitrary arguments like '__arg1'
    def _run(self, **kwargs) -> str:
        # Returning a set of general health tips
        tips = """
        1. Drink plenty of water every day.
        2. Eat a balanced diet rich in fruits, vegetables, and whole grains.
        3. Engage in regular physical activity.
        4. Get adequate sleep—7-9 hours per night.
        5. Avoid smoking and limit alcohol consumption.
        """
        return tips

    async def _arun(self, **kwargs) -> str:
        # Asynchronous version not implemented
        raise NotImplementedError("Async run is not implemented yet.")
