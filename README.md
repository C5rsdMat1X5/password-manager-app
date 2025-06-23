# 🔐 Password Manager App

Esta aplicación es un **gestor de contraseñas** desarrollado en Python, usando `PySide6` para la interfaz gráfica y `cryptography` para cifrar las contraseñas de forma segura.

## 🧰 Tecnologías usadas

- 🖼️ [PySide6](https://doc.qt.io/qtforpython/) - Para la interfaz gráfica
- 🔐 [cryptography](https://cryptography.io/en/latest/) - Para el cifrado seguro de las contraseñas
- 🐍 Python 3.10+

## 📦 Estructura del proyecto

```
├── assets/              # Archivos estáticos (CSS)
│   └── style.css        # Stylesheet (CSS)
├── core/                # Lógica principal y ventanas
│   ├── config.py        # Configuraciones globales
│   ├── list_window.py   # Ventana que lista contraseñas
│   ├── login_window.py  # Ventana de inicio de sesión
│   ├── manager.py       # Ventana principal del gestor
│   ├── startup.py       # Inicialización de la app
│   └── utils.py         # Utilidades varias
├── data/                # Aquí se guarda la base de datos encriptada
├── main.py              # Archivo principal de entrada
├── requirements.txt     # Dependencias del proyecto
└── README.md
```

## 🚀 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/C5rsdMat1X5/password-manager-app
   cd password-manager-app
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación:**

   - En **Linux/macOS**:
     ```bash
     python3 main.py
     ```

   - En **Windows**:
     ```bash
     python main.py
     ```

## 📁 Datos

- Las contraseñas se almacenan cifradas dentro de la carpeta `data/`.
- El acceso a la app requiere una contraseña maestra, la cual se establece al primer uso.

## ⚠️ Notas de seguridad

- Este proyecto es solo con fines educativos. No se recomienda usarlo para gestionar contraseñas reales sin antes revisarlo y adaptarlo adecuadamente.
- Asegúrate de mantener el archivo `data/` seguro y respaldado si decides usarlo.

## 🧠 Autor

Desarrollado por Matías Henríquez.
