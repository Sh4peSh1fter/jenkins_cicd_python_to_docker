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
                sh 'pylint app/'
                sh 'pytest app/test_main.py'
            }
        }
        stage('run') {
            steps {
                sh 'docker run -i app'
            }
        }
    }
    post {
        success {
            echo "yea"
        }
        failure {
            echo "oof"
        }
    }
}
