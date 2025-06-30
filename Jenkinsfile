pipeline {
    agent any

    triggers {
        cron('H 8 13,19 * *') // 8 AM on 13th & 19th every month
    }

    stages {
        stage('Run Script') {
            steps {
                echo 'Running Python news digest script...'
                sh 'python3 news_digest.py'
            }
        }
    }
}
