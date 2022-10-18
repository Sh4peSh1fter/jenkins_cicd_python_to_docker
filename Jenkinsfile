pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'docker build --progress=plain -f app/Dockerfile -t app .'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest app/test_main.py'
            }
        }
        stage('run') {
            steps {
                sh 'docker run -i app'
            }
        }
    }
}
