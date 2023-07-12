# Weather Web App

The Weather Web App is a web application that provides current weather information for different locations. It is built using the Django framework for the backend and JavaScript for the frontend.

## Features

- **Location Search:** Users can search for weather information by entering a location name.
- **Current Weather:** Displays the current weather conditions, including temperature, humidity, wind speed, and weather description.
- **Forecast:** Shows a 5-day weather forecast for the selected location.
- **Responsive Design:** The web app is designed to be responsive and accessible across different devices and screen sizes.

## Technologies Used

- Django: A high-level Python web framework used for the backend.
- JavaScript: Used for client-side interactions and dynamic content.
- OpenWeatherMap API: The app fetches weather data from the OpenWeatherMap API.
- HTML/CSS: Used for structuring and styling the web pages.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/weather-web-app.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your OpenWeatherMap API key:
   ```
   API_KEY=your_api_key
   ```

4. Run the Django migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the web app at `http://localhost:8000`.

## Configuration

You can modify the following settings in the `settings.py` file:

- `API_KEY`: Your OpenWeatherMap API key.
- `UNITS`: The units for temperature (metric, imperial, or kelvin).

## Contributing

Contributions to the Weather Web App are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and expand upon this README file based on your specific project requirements and additional features you may have implemented. Make sure to include any relevant instructions for setting up and running the application.
