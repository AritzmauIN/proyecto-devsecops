pipeline {
   agent any

   stages {

       stage('Descargar Código') {
           steps {
               echo 'Clonando el repositorio...'
               git branch: 'desarrollo', url: 'https://github.com/AritzmauIN/proyecto-devsecops.git'
           }
       }

       stage('Construir Imagen (Build)') {
           steps {
               echo 'Construyendo el contenedor...'
               sh 'docker build -t mi-app-segura:latest .'
           }
       }

       stage('Análisis de Seguridad (Trivy)') {
           steps {
               echo 'Buscando vulnerabilidades CRÍTICAS...'
               sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/aquasecurity/trivy:latest image --exit-code 1 --severity CRITICAL mi-app-segura:latest'
           }
       }

       stage('Despliegue en Producción (CD)') {
           steps {
               echo 'Desplegando aplicación...'

               sh 'docker stop app-produccion || true'
               sh 'docker rm app-produccion || true'
               sh 'docker run -d --name app-produccion mi-app-segura:latest'
           }
       }
   }
}
