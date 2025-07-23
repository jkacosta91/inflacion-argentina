# 📈 Predicción de Inflación en Argentina

Este proyecto tiene como objetivo construir un modelo predictivo de la inflación mensual en Argentina utilizando Python y técnicas de ciencia de datos.

Incluye procesos de:

- Extracción de datos del INDEC y BCRA
- Limpieza y transformación (ETL)
- Modelado predictivo con algoritmos estadísticos y de machine learning
- Visualización y análisis con Power BI

---

## 📁 Estructura del proyecto

```plaintext
inflacion-argentina/
├── data/            # Datos crudos y procesados (.csv)
├── notebooks/       # Exploraciones y notebooks de análisis
├── src/
│   ├── etl/         # Extracción y limpieza de datos (ETL)
│   │   └── ipc_ingest.py      # Script para obtener series desde archivo_series.csv
│   └── models/      # Modelos predictivos
│   └── utils/       # Funciones auxiliares
├── reports/         # Visualizaciones, reportes de resultados
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Cómo ejecutar

### 1. Clonar el repositorio

```bash
git clone https://github.com/jkacosta91/inflacion-argentina.git
cd inflacion-argentina
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
.
env\Scripts\Activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 📊 Tecnologías utilizadas

- **Python 3.12**
- **Pandas**, **Scikit-Learn**, **Statsmodels**, **Requests**
- **Power BI** para visualización
- **Git** + **GitHub** para control de versiones

---

## 🧠 Objetivos del análisis

- Entender la evolución de la inflación argentina (mensual, interanual)
- Predecir inflación a corto y mediano plazo
- Relacionar inflación con otras variables (tasas, tipo de cambio, etc.)
- Comunicar hallazgos con dashboards interactivos

---

## 📌 Autor

**jkacosta91**  
🔗 GitHub: [@jkacosta91](https://github.com/jkacosta91)

---

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT.
