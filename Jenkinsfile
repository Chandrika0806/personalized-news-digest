pipeline {
    agent any

    triggers {
        cron('H 8 13,19 * *') // adjust schedule if needed
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python3 -m pip install --user requests'
            }
        }

        stage('Run Script') {
            steps {
                echo 'Running Python news digest script...'
                sh 'python3 news_digest.py'
            }
        }
    }
}
