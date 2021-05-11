Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker 'python:3.9.1' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}