pipeline {
    agent any

    stages {
        stage('stop recursion') {
            steps {
                script {
                    def msg = sh(script:'git log -1 --pretty=%B', returnStdout:true).trim()
                    if( msg.contains("pipeline") ) {
                        error 'echo exiting from recursion'
                    }
                }
            }
        }
        stage('build') {
            steps {
                sh 'docker build --progress=plain -f app/Dockerfile -t app .'
                sh 'git log -1 --pretty=%B'
            }
        }
        stage('test') {
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
                sh 'git commit --amend -m "cicd pipeline succeeded"'
                sh 'git push --force origin HEAD:master'
            }
        }
        failure {
            withCredentials([gitUsernamePassword(credentialsId: 'working-github-token')]) {
                sh 'git config --global user.email "you@example.com"'
                sh 'git config --global user.name "Your Name"'
                sh 'git commit --amend -m "cicd pipeline failed"'
                sh 'git push --force origin HEAD:master'
            }
        }
    }
}
