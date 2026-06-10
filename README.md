# 🍇 Vitisense - Smart Viticulture & Agronomy System

[![Vercel Deployment](https://img.shields.io/badge/Deployed-Vercel-blue?style=flat-square&logo=vercel)](https://vitisnece.vercel.app)
[![Python](https://img.shields.io/badge/Backend-Python%20Flask-blue?style=flat-square&logo=python)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

## 📋 Overview

Vitisense is an intelligent agricultural ecosystem designed to optimize grape farming and viticulture management. By leveraging **AI-powered computer vision**, **sensor fusion**, and **real-time IoT integration**, Vitisense empowers farmers to make data-driven decisions and maximize crop yield.

Whether you're monitoring fruit ripeness, detecting early disease signs, or generating professional agronomist reports, Vitisense combines cutting-edge technology with practical agronomy.

## 🚀 Live Demo

Experience the application in action: **[vitisnece.vercel.app](https://vitisnece.vercel.app)**

## ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🍇 **Fruit Ripeness & Quality Analysis** | Computer vision and HSV color analysis to evaluate grape color, ripeness stages, and quality metrics |
| 🧪 **Sugar Content (°Brix) Tracking** | Real-time sensor data processing to assess sweetness and maturity levels |
| 🌿 **Plant Health & Disease Detection** | AI-powered leaf analysis to identify early disease signs and ensure optimal crop yield |
| 📊 **AI-Powered Agronomist Reports** | Automatic generation of professional, actionable PDF reports with Google GenAI integration |
| 📱 **IoT Hardware Integration** | Seamless compatibility with ESP32-CAM and ESP32-S3-CAM for real-time image capture |
| 🌐 **Web Dashboard** | Intuitive interface for data visualization and report management |

## 🛠️ Tech Stack

### Backend & Infrastructure
- **Framework:** Python Flask (REST API)
- **Frontend:** HTML5 / CSS / JavaScript
- **AI & ML:** Google Gemini API (GenAI)
- **Computer Vision:** OpenCV
- **Deployment:** Vercel (Serverless)

### Hardware Integration
- **Camera Modules:** ESP32-CAM, ESP32-S3-CAM
- **Protocols:** HTTP/HTTPS for data transmission
- **Real-time Processing:** On-device image capture & cloud processing

## ⚙️ System Architecture

```
┌──────────────────┐
│   Hardware       │
│ (ESP32-CAM)      │  ◄─── Image Capture & Sensor Data
└────────┬─────────┘
         │
         ▼
┌──────────────────────────┐
│  Python Backend (Flask)  │  ◄─── Image Processing & Analysis
│  ├─ OpenCV Processing   │
│  └─ Data Aggregation    │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│  Google Gemini AI        │  ◄─── Insights & Report Generation
│  (Generative AI)         │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│  Web Dashboard           │  ◄─── User Interface & PDF Export
│  ├─ Data Visualization  │
│  └─ Report Management   │
└──────────────────────────┘
```

### Process Flow
1. **Data Collection:** IoT hardware captures grape and leaf imagery + environmental sensor metrics
2. **Image Processing:** Backend analyzes imagery using computer vision to extract ripeness/health indicators
3. **AI Evaluation:** Metrics are sent to Google Gemini for expert-level agronomy insights
4. **Actionable Output:** Farmers access the dashboard to view results or download PDF reports

## 💻 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Google Gemini API Key ([Get one here](https://ai.google.dev/))
- Git

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sarveshmule1504/vitisnece.git
   cd vitisnece
   ```

2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

   The application will be available at: **`http://localhost:5000`**

## ☁️ Deployment

### Vercel Deployment

This project is pre-configured for serverless deployment on **Vercel**.

1. **Push to GitHub** (already done)
2. **Connect to Vercel:**
   - Go to [Vercel Dashboard](https://vercel.com)
   - Click "New Project" → Select your repository
3. **Set Environment Variables:**
   - Add `GEMINI_API_KEY` to your project's environment variables
4. **Deploy:**
   - Click "Deploy" → Your app will be live in seconds!

For more details, see [`vercel.json`](vercel.json)

## 📂 Project Structure

```
vitisnece/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── templates/            # HTML templates
├── static/               # CSS, JavaScript, images
├── .env.example          # Environment variables template
└── README.md             # This file
```

## 🔌 Hardware Setup

### ESP32-CAM Configuration

To connect your ESP32-CAM module:

1. Flash the ESP32 with appropriate firmware
2. Configure WiFi credentials
3. Set the backend URL in the device configuration
4. The device will start sending images to the backend for processing

## 📖 API Documentation

### Main Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page / Dashboard |
| POST | `/analyze` | Submit image for analysis |
| GET | `/reports` | Retrieve generated reports |
| POST | `/generate-report` | Generate PDF report |

> For detailed API documentation, check the source code comments in `app.py`

## 🤝 Contributing

We welcome contributions! To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Issues

- **Found a bug?** Open an [issue](https://github.com/sarveshmule1504/vitisnece/issues)
- **Have a question?** Check existing issues or start a discussion
- **Want to help?** Check out [open issues](https://github.com/sarveshmule1504/vitisnece/issues)

## 🔗 Links

- **Live App:** [vitisnece.vercel.app](https://vitisnece.vercel.app)
- **GitHub:** [sarveshmule1504/vitisnece](https://github.com/sarveshmule1504/vitisnece)
- **AI API:** [Google Gemini](https://ai.google.dev/)

---

<div align="center">

**Made with 🍇 by [Sarvesh Mule](https://github.com/sarveshmule1504)**

*Empowering farmers through intelligent agriculture*

</div>
