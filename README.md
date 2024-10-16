# Pikachu Health Agent

Pikachu Health Agent is an intelligent health assistant that can provide advice on BMI calculation, recommend daily water intake based on your weight, and give general health tips. This agent leverages tool-augmented LLM capabilities to interact with users in a conversational manner and deliver personalized health-related information.

## Features
The Pikachu Health Agent currently supports the following features:
- **BMI Calculation**: Based on the user’s input of weight and height, the agent calculates their BMI and provides feedback.
- **Water Intake Recommendation**: Recommends daily water intake based on the user’s weight.
- **General Health Tips**: Provides a set of general health tips for maintaining a healthy lifestyle.

## Files in the Repository
1. **`agent.yaml`**: The configuration file for the Pikachu Health Agent, defining its tasks and plugin tools.
2. **`calculate_bmi.py`**: The plugin that handles BMI calculation based on user-provided weight and height.
3. **`recommend_water_intake.py`**: The plugin that provides a recommendation for daily water intake based on the user's weight.
4. **`general_health_tips.py`**: The plugin that gives general health advice.

## Usage
To run the Pikachu Health Agent, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/tejsamineni/pikachu_health.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd pikachu_health
    ```
3. Run the agent using the following command:
    ```bash
    python assemble.py pikachu_health
    ```

## Example Prompts and Outputs

### 1. BMI Calculation
**User Prompt**: 
```bash
Can you calculate my BMI? My weight is 70 kg and my height is 1.75 meters.
```
```bash
How much water should I drink if I weigh 80 kg?
```
```bash
Can you give me some general health tips?
```
## Contribution

Feel free to fork the repository and submit a pull request if you’d like to contribute or enhance the agent’s capabilities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

