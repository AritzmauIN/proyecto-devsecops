pipeline {
    agent any

    stages {

        stage('Limpiar Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Descargar Código') {
            steps {
                echo 'Clonando el repositorio desde GitHub...'
                git branch: 'desarrollo', url: 'https://github.com/AritzmauIN/proyecto-devsecops.git'
            }
        }

        stage('Construir Imagen Docker (Build)') {
            steps {
                echo 'Construyendo el contenedor seguro...'
                sh 'docker build -t mi-app-segura:latest .'
            }
        }

        stage('Análisis de Seguridad (Trivy)') {
            steps {
                echo 'Analizando vulnerabilidades CRÍTICAS...'
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/aquasecurity/trivy:latest image --exit-code 1 --severity CRITICAL mi-app-segura:latest'
            }
        }
    }
}


