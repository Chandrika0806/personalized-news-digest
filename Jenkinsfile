pipeline {
    agent any
    triggers {
        cron('H 7 * * *')  // Runs daily at 7AM
    }
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/YOUR_USERNAME/personalized-news-digest.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t news-digest .'
            }
        }
        stage('Run Script') {
            steps {
                sh 'docker run --rm news-digest'
            }
        }
    }
}
