pipeline {
    agent any

    triggers {
        // Schedule: 3 times daily — 8 AM, 1 PM, 7 PM
        cron('H 8,13,19 * * *')
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-pat',
                    url: 'https://github.com/Chandrika0806/personalized-news-digest.git'
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
