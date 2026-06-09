# vitisense

# README.md
```markdown
# VITISENSE: Smart Viticulture Ecosystem

VITISENSE is an intelligent, edge-integrated agricultural system designed to optimize grape harvesting and market placement. By combining Convolutional Neural Networks (CNNs), real-time computer vision, hardware-level sensor fusion, and Machine Learning classifiers, VITISENSE evaluates leaf health, assesses fruit maturity, and guides farmers on whether to harvest for local consumption or premium export.

---

## 🚀 Key Features
* **Automated Disease Diagnosis:** Laptop/Edge AI identification of Powdery Mildew, Downy Mildew, and Leaf Blight using a deep learning CNN architecture.
* **Wireless Field Inspection:** Remote image acquisition of grape clusters via an ultra-low-power ESP32/ESP32-S3 camera module.
* **HSV Color Metric Processing:** Robust ripeness estimation immune to changing outdoor lighting conditions.
* **Quantitative Sweetness Validation:** Real-time Sugar Content logging measured in Degrees Brix (°Brix) with on-site LCD feedback.
* **Predictive Market Engine:** An ML-based decision matrix that optimizes harvesting schedules and maximizes profitability (Local vs. Export).

---

## 📊 System Architecture & Workflow


```
[Leaf Image (Laptop Camera)] --------> [CNN Disease Classifier Model]
│
▼ Output: Health Report
[Grape Bunch (ESP32-S3 Cam)] ──(Wi-Fi POST)──> [Flask Base Station Server]
│
▼
[HSV Color Analysis]
│
▼ Output: Ripeness Stage
[Brix Sugar Sensor + LCD] ────(Manual/Serial)─> [ML Decision Engine (SVM/RF)]
│
▼
[Final Recommendation Report]
- Action: Harvest Now / Wait
- Market: Export / Local
```

---

## 🛠️ Hardware & Component Configuration

| Component | Function / Purpose | Pinout / Communication Protocol |
| :--- | :--- | :--- |
| **ESP32-S3-CAM / ESP32-CAM** | Wireless Image Acquisition Node | Wi-Fi (802.11 b/g/n), HTTP POST |
| **I2C 16x2 LCD Display** | On-site °Brix & System Status Readout | I2C Protocol (SDA: GPIO 15, SCL: GPIO 14) |
| **Brix Interface Modality** | Potentiometer / Analog Input Simulation | ADC Channel (GPIO 34) |
| **Base Station System** | Model Inference & Core Compute | Laptop Host / Local Server |

---

## 💻 Tech Stack & Software Frameworks

* **Firmware:** C++ (Arduino IDE / PlatformIO), ESP-IDF Wireless Stack
* **Backend Server:** Python 3.x, Flask Web Framework
* **Computer Vision:** OpenCV (Open Source Computer Vision Library), NumPy
* **Machine Learning / AI:** TensorFlow/Keras (CNNs), Scikit-Learn (Random Forest/SVM Classifier)
* **Dataset Source:** PlantVillage Grape Dataset (Kaggle)

---

## 📂 Project Structure

```text
├── hardware/
│   ├── esp32_cam_firmware/      # Arduino C++ source code for image capture & Wi-Fi
│   └── schematics/              # Fritzing/KiCAD circuit wiring diagrams
├── server/
│   ├── app.py                   # Flask server handling requests and HSV processing
│   ├── models/                  # Trained ML/DL model files (.h5, .pkl)
│   └── templates_and_reports/   # Automated farmer summary formatting scripts
└── ml_ai/
    ├── leaf_disease_cnn.ipynb   # Jupyter Notebook: CNN training on PlantVillage dataset
    └── market_classifier.ipynb  # Jupyter Notebook: Random Forest Decision training

```
## 🔧 Installation & Deployment Steps
### 1. Hardware Flashing
 1. Navigate to hardware/esp32_cam_firmware/.
 2. Update the ssid and password variables with your local Wi-Fi credentials.
 3. Configure your target server's local IPv4 Address (e.g., http://192.168.1.X:5000/upload).
 4. Select the proper board configuration (**AI Thinker ESP32-CAM** or **ESP32S3 Dev Module**) and compile/upload.
### 2. Base Station Server Setup
Clone the repository and install the dependencies:
```bash
git clone [https://github.com/yourusername/VITISENSE.git](https://github.com/yourusername/VITISENSE.git)
cd VITISENSE/server
pip install -r requirements.txt

```
*Note: Create a requirements.txt file containing: flask, opencv-python, numpy, scikit-learn, tensorflow.*
### 3. Execution Execution
Start the Flask back-end script:
```bash
python app.py

```
Ensure the hardware node mounts onto the exact local server network. The console will print incoming image frame logs along with mathematical ripeness evaluations.
## 📈 Decision Metric Reference
The final analytical recommendation is drawn directly from agricultural thresholds mapped within our Machine Learning layer:
| Color Maturity Index | Sugar Content Range | Decision Matrix Output |
|---|---|---|
| **Optimal Stage** | > 16 °Brix | Export Quality - Harvest Now |
| **Optimal Stage** | 12 - 15 °Brix | Local Market - Harvest Now |
| **Early Stage** | Any Range | Do Not Harvest - Retain on Vine |
| **Over-Ripe Stage** | Any Range | Immediate Local Processing / Wine Target |
## 👥 Project Mentorship & Contributors
 * **Developer:** Sarvesh Mule (Electronics & Communication Engineering)
 * **Project Guides:** Prof. Mahesh Kamthe, Prof. Dr. Shankar Gambhire
 * **Institution:** MIT ADT University, Pune
```

***


