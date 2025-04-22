# 🌍 Nang-Rong-Yang-Rao

## 👥 Team Members

- **Raveewan Santipong** (Fahsairvw) – 6610545928  
  Department of Software and Knowledge Engineering, Kasetsart University  
- **Yatichapat Dechaeamsakulchai** (Yatichapat)– 6610545235  
  Department of Software and Knowledge Engineering, Kasetsart University  

---

## 📖 Project Overview

**Nang-Rong-Yang-Rao** is a web-based environmental monitoring API system that collects, stores, and visualizes air quality and sound level data from Bangkok district. It provides real-time access and predictive insights based on collected values such as:

- PM2.5
- PM10
- AQI
- Sound levels

The system supports interactive frontend visualization and a RESTful API documented with OpenAPI.

---

## ✨ Features

- View current and historical values of PM2.5, PM10, AQI, and sound.
- Visualize data using line graphs.
- Explore relationships through scatter plot.
- Access OpenAPI 3.0-based interactive API documentation.

---
## 📋 Database Table Structure: `nangrong`

| Field    | Type     | Description                         |
|----------|----------|-------------------------------------|
| `id`     | INT      | Unique identifier                   |
| `hour`   | DATETIME | Timestamp of the measurement        |
| `lat`    | INT      | Latitude of the location            |
| `lon`    | INT      | Longitude of the location           |
| `sound`  | FLOAT    | Sound level (dB)                    |
| `pm25`   | FLOAT    | PM2.5 value (μg/m³)                 |
| `pm10`   | FLOAT    | PM10 value (μg/m³)                  |
| `aqi`    | INT      | Air Quality Index                   |

---

## 🧰 Prerequisites

Before running the project, make sure you have the following installed:

- **Python** (>= 3.8): [Download Python](https://www.python.org/)
- **pip** (comes with Python)
- **DBUtils** (==3.1.0): For database connection pooling  
- **PyMySQL** (==1.1.1): For MySQL database connection
- **connexion** (==2.14.2): For building RESTful APIs

---

## ⚙️ Installation

### Installation
Clone the repository

```bash
git clone https://github.com/Fahsairvw/Nang-Rong-Yang-Rao.git 
```

Go to Directory

``` bash
cd Nang-Rong-Yang-Rao 
```

### Step how to run the code
1. User starts the virtual in the virtual env. 

   ``` bash
    python -m venv venv 
   ```
2. Activate the virtual env on Linux and MacOS

   ```bash
    source venv/bin/activate 
   ```
 
    Or, on MS Windows:

   ```bash
    .\venv\Scripts\activate
   ```
3. Install requirement
 
   ```bash
    pip install -r requirements.txt
   ```
4. Run program
   
   ```bash
    python app.py
   ```
5. Go to dash board

   ```bash
    http://127.0.0.1:8080
   ```

6. Open API specification

   ```bash
   http://127.0.0.1:8080/air-quality-api/v1/ui/
   ```
---
## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
