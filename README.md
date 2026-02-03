## Atención
* Para generar la última versión del CV en version PDF, se DEBE agregar un nuevo release al archivo RELEASES.md con la variable shouldCreateRelease seteada en true y el correspondiente changelog.

* [Link](https://github.com/ezeveliz/cv/releases/latest/download/Ezequiel_Veliz_CV.pdf) de acceso a la última versión.
## Desarrollo Local (Local Development)

Este proyecto utiliza **Jekyll** pero puede ser ejecutado localmente utilizando **Eleventy (11ty)** via Node.js sin necesidad de instalar Ruby.

Para levantar el servidor localmente:

```bash
npx @11ty/eleventy --serve
```

Esto levantará el sitio en [http://localhost:8080/](http://localhost:8080/).
