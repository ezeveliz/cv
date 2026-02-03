## Atención
* Para generar una nueva versión, se DEBE agregar una entrada al archivo `RELEASES.md` con el **número de versión incremental**, el changelog correspondiente, y las siguientes variables de configuración:
  * `shouldCreateRelease`: debe ser `"true"` para iniciar el proceso de deploy.
  * `shouldCreatePDF`: debe ser `"true"` para generar y adjuntar el PDF del CV. Si es `"false"` o se omite, solo se creará el tag/release en GitHub sin el binario.

* [Link](https://github.com/ezeveliz/cv/releases/latest/download/Ezequiel_Veliz_CV.pdf) de acceso a la última versión.
## Desarrollo Local (Local Development)

Este proyecto utiliza **Jekyll** pero puede ser ejecutado localmente utilizando **Eleventy (11ty)** via Node.js sin necesidad de instalar Ruby.

Para levantar el servidor localmente:

1. Instalar dependencias:
   ```bash
   npm install
   ```
2. Iniciar el servidor:
   ```bash
   npm start
   ```

Esto levantará el sitio en [http://localhost:8080/](http://localhost:8080/).
