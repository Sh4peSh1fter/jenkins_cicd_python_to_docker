pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'cd app'
                sh 'docker build -t app .'
            }
        }
        stage('run') {
            steps {
                sh 'docker run app'
            }
        }
    }
}
