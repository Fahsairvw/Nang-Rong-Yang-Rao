# 🌍 Nang-Rong-Yang-Rao

## 👥 Team Members

- **Raveewan Santipong** (Fahsairvw) – 6610545928  
  Department of Software and Knowledge Engineering, Kasetsart University  
- **Yatichapat Dechaeamsakulchai** – 6610545235  
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

## 🧰 Prerequisites

- **Python** (>= 3.8): [Download Python](https://www.python.org/)
- **Connexion** library (for OpenAPI integration)

---

## ⚙️ Installation

### Installation
Clone the repository

``` git clone https://github.com/Fahsairvw/Nang-Rong-Yang-Rao.git ```

Go to Directory

``` cd Nang-Rong-Yang-Rao ```

### Step how to run the code
1. User starts the virtual in the virtual env. 

   ``` python -m venv venv ```
2. Activate the virtual env on Linux and MacOS

   ```source venv/bin/activate ```
 
    Or, on MS Windows:

   ```.\venv\Scripts\activate```
3. Install requirement
 
   ```pip install -r requirements.txt```
4. Run program
   
   ```python app.py```
5. Go to dash board

   ```http://127.0.0.1:8080```

6. Open API specification

   ```http://127.0.0.1:8080/air-quality-api/v1/ui/```
