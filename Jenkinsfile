pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'docker build --progress=plain -f app/Dockerfile -t app .'
            }
        }
        stage('run') {
            steps {
                sh 'docker run -i app'
            }
        }
    }
}
