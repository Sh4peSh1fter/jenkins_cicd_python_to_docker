pipeline {
    agent any

    stages {
        stage('stop recursion') {
            steps {
                script {
                    def msg = sh(script:'git log -1 --pretty=%B', returnStdout:true).trim()
                    if( msg.contains("pipeline") ) {
                        skipRemainingStages = true
                    }
                }
            }
        }
        stage('build') {
            when {
                expression {
                    !skipRemainingStages
                }
            }
            steps {
                sh 'docker build --progress=plain -f app/Dockerfile -t app .'
                sh 'git log -1 --pretty=%B'
            }
        }
        stage('test') {
            when {
                expression {
                    !skipRemainingStages
                }
            }
            steps {
                sh 'pylint app/'
                sh 'pytest app/test_main.py'
            }
        }
        stage('run') {
            when {
                expression {
                    !skipRemainingStages
                }
            }
            steps {
                sh 'docker run -i app'
            }
        }
    }
    post {
        when {
            expression {
                !skipRemainingStages
            }
        }
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
