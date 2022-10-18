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
            withCredentials([gitUsernamePassword(credentialsId: 'working-github-toke')]) {
                sh 'git config --global user.email "you@example.com"'
                sh 'git config --global user.name "Your Name"'
                sh 'git commit --allow-empty --only --amend -m "success"'
                sh 'git push --force origin master'
            }
        }
        failure {
            withCredentials([gitUsernamePassword(credentialsId: 'working-github-token')]) {
                sh 'git config --global user.email "you@example.com"'
                sh 'git config --global user.name "Your Name"'
                sh 'git add .'
                sh 'git commit --allow-empty --only --amend -m "fail"'
                sh 'git push --force origin master'
            }
        }
    }
}
