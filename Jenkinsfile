pipeline {
    agent any

    triggers {
        cron('H 8 13,19 * *') // 8 AM on 13th & 19th of every month
    }

    stages {
        stage('Install pip') {
            steps {
                echo 'Checking and installing pip if not present...'
                sh '''
                    if ! command -v pip3 &> /dev/null
                    then
                        echo "pip3 not found. Installing..."
                        apt-get update && apt-get install -y python3-pip
                    else
                        echo "pip3 already installed."
                    fi
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip3 install --user requests'
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
