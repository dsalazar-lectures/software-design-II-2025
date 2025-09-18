# Tutorial Flask con VS Code

## 1) Prerrequisitos

-   **VS Code** con la **extensión de Python** instalada (Microsoft).
    
-   **Python 3** instalado.
    
    -   Windows: recomendado el instalador de [python.org].
        
    -   Linux: suele venir Python 3; para paquetes: `sudo apt install python3-pip`.
        
    -   macOS: `brew install python` (Homebrew) o instalador de python.org.
        
-   (Windows) Verifica que Python esté en el **PATH**:
    
    ```
    where python
    python --version 
    ```
    
    Si no aparece, en **Configuración de Windows** busca “**Editar las variables de entorno**” → edita `Path` y agrega la carpeta del intérprete.

## 2) Crear el entorno del proyecto (virtualenv) en VS Code

1.  Estar en la carpeta **appFlask**.
    
2.  Abre esa carpeta en VS Code:
    
    -   Terminal → navega a la carpeta y ejecuta `code .`, **o**
        
    -   En VS Code: **File > Open Folder…**
        
3.  Abre la **Command Palette**: **View > Command Palette…** (Ctrl+Shift+P).
    
4.  Ejecuta: **Python: Create Environment** → elige **venv** → selecciona la versión de **Python**.

![Creando el .venv de Python](/imagenes/Python%20Env.png)
    
### Nota (PowerShell bloquea `Activate.ps1`)

En Windows, si tu terminal por defecto es **PowerShell** puedes ver un error al activar el entorno: _“no puede ejecutar activate.ps1 porque la ejecución de scripts está deshabilitada”_.  
Soluciones:

-   **Opción 1: Solo esta sesión (rápida):**
    
    `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
    .\.venv\Scripts\Activate.ps1` 
    
-   **Opción 2: Permanente para tu usuario:**
    
    `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    .\.venv\Scripts\Activate.ps1` 
    
-   **Alternativa sin cambiar políticas:** usa otro perfil de terminal en VS Code:  
    **Terminal: Select Default Profile** → **Command Prompt** o **Git Bash**.  
    (En CMD, activa con `.\.venv\Scripts\activate.bat`).

5.  Cuando termine, usa **Terminal: Create New Terminal** (Ctrl+Shift+ñ) o desde la Paleta de Comandos, VS code activa automáticamente el entorno virtual ejecutando su script de activación. Si no se hace la nota anterior dará error, pero el programa podrá correr sin problemas es para para aislar dependencias.


## 3) Instalar Flask dentro del entorno

Con el terminal del proyecto **activado**(Estar dentro de la carpeta appFlask):

`python -m pip install flask` 

(En nuevas terminales, VS Code suele re-activar el entorno. Si abres un terminal aparte, actívalo manualmente:  
Linux/macOS: `source .venv/bin/activate` • Windows: `.\.venv\Scripts\Activate.ps1`)


## 4) Ejecutar una app mínima

1. En la misma terminal dentro de la carpeta **appFlask** ejecuta el siguiente comando: `python -m flask run`, que ejecuta el servidor de desarrollo de Flask. El servidor de desarrollo busca app.py por defecto. Al ejecutar Flask, debería ver un resultado similar al siguiente:

![Corriendo Flask sin debugger](/imagenes/Flask%20run.png)

    o

    python app.py (usa `app.run(debug=True)`).

![Corriendo Flask con debugger](/imagenes/Flask%20run%20debugger.png)    


Ctrl+clic en la URL para abrir en el navegador.  
    (Para otro host/puerto: `python -m flask run --host=0.0.0.0 --port=8000`)


> Si aparece “Flask no se encuentra”, reinstala dentro del entorno: `python -m pip install flask`.


## 5) Evidencias


Con la app corriendo (por defecto en `http://127.0.0.1:5000`) y usando Insomnia:

-   **GET /** 
    
![Evidencia GET](/imagenes/Evidencia%20Get.png) 
    
-   **POST /** (OK)
    
.json de ejemplo    
{
"name": "Paula"
}
    
![Evidencia POST](/imagenes/Evidencia%20Post.png) 

    
-   **GET /petName/nombreMascota**
    
   Ejemplo:  `http://127.0.0.1:5000/petName/Coco` 

![Evidencia Get/URL](/imagenes/Evidencia%20GetUrl.png) 