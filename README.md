# 🗺️ U.S. States Game

Un juego educativo creado con Python que desafía al usuario a nombrar los 50 estados de EE.UU. A medida que introduces respuestas correctas, sus nombres se muestran directamente en el mapa. Ideal para practicar geografía o demostrar habilidades con `pandas` y `turtle`.

---

## 🎮 ¿Cómo se juega?

- Se muestra un mapa en blanco de los Estados Unidos.
- Introduce nombres de estados en el cuadro emergente.
- Si aciertas, el nombre aparece en la posición correcta del mapa.
- El juego termina cuando:
  - Aciertas los 50 estados ✅
  - O cierras el cuadro de entrada ❌

---

## 🧠 Funcionalidades

- Interfaz visual con `turtle`
- Validación de respuestas repetidas
- Detección de cancelación del juego
- Escritura de nombres en coordenadas reales del mapa

---

## 📦 Tecnologías usadas

- Python 3
- `turtle` – para gráficos y entrada de texto
- `pandas` – para manipular datos del archivo CSV

---

## 📁 Estructura del proyecto
├── blank_states_img.gif # Imagen base del mapa

├── 50_states.csv # CSV con los estados y sus coordenadas X/Y

├── main.py # Código principal del juego

└── README.md

## 🚀 Cómo ejecutar

1. Asegúrate de tener Python 3 y las bibliotecas necesarias:
   ```bash
   pip install pandas
2.
   Ejecuta el programa:
  python main.py

  📚 Créditos
  datos: https://www.kaggle.com/datasets
  Mapa base: proporcionado por el curso 100 Days of Code: Python
  
 
