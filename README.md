# vitisense


# 🍇 Vitisense - Smart Viticulture & Agronomy System

Vitisense is an intelligent agricultural ecosystem designed to optimize grape farming and viticulture management. By leveraging AI, computer vision, and sensor fusion, Vitisense assists farmers in assessing plant health, determining fruit ripeness, and making data-driven decisions on whether to target local markets or premium exports.

## 🚀 Live Demo
Check out the live application here: [vitisnece.vercel.app](https://vitisnece.vercel.app)

## ✨ Core Features
* **Fruit Ripeness & Quality Analysis:** Utilizes computer vision and HSV color analysis to evaluate grape color and ripeness stages.
* **Sugar Content (°Brix) Tracking:** Processes sensor data to assess the sweetness and maturity of the fruit.
* **Plant Health & Disease Detection:** Analyzes leaf imagery to detect early signs of disease, ensuring optimal crop yield.
* **AI-Powered Agronomist Reports:** Integrates Google GenAI to automatically generate professional, actionable PDF reports for farmers, providing clear guidance on harvesting schedules and market classification.

## 🛠️ Tech Stack & Hardware
* **Backend:** Python (Flask)
* **Frontend:** HTML 
* **AI & Vision:** Google GenAI (`google-genai`), OpenCV
* **Hardware Integration:** Compatible with ESP32-CAM and ESP32-S3-CAM modules for real-time image capture.
* **Deployment:** Vercel (Configured via `vercel.json`)

## ⚙️ System Architecture
1. **Data Collection:** Hardware modules (like the ESP32-CAM) capture images of grape bunches and leaves while sensors gather environmental metrics.
2. **Image Processing:** The Python backend processes the imagery, using computer vision to extract critical ripeness and health indicators.
3. **AI Evaluation:** Processed metrics are passed to Google's Generative AI to formulate expert-level agronomy insights.
4. **Actionable Output:** Farmers access the web dashboard to view results or download generated PDF reports to guide their harvest strategy.

## 💻 Local Setup & Installation

Follow these steps to run the Vitisense backend locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sarveshmule1504/vitisnece.git](https://github.com/sarveshmule1504/vitisnece.git)
   cd vitisnece

```

2. **Set up a virtual environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure Environment Variables:**
You will need a valid Google Gemini API key to utilize the AI reporting features.
* Create a `.env` file in the root directory.
* Add your key: `GEMINI_API_KEY=your_api_key_here`


5. **Run the application:**
```bash
python app.py

```


*The application will be hosted locally at `http://127.0.0.1:5000`.*

## ☁️ Deployment

This project is configured for serverless deployment on **Vercel**.

* The `vercel.json` file handles the routing of the Python backend.
* Ensure that your `GEMINI_API_KEY` is added to your Vercel project's Environment Variables before deploying to avoid application errors.


```

```
