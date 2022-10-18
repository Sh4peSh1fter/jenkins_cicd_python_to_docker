pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'cd app'
                sh 'docker build -f app/Dockerfile -t app .'
            }
        }
        stage('run') {
            steps {
                sh 'ls'
                sh 'docker run app'
            }
        }
    }
}
