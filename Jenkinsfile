pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo '✅ Code checked out successfully.'
            }
        }

        stage('Check Environment') {
            steps {
                bat 'python --version'
                echo '✅ Python environment verified.'
            }
        }

        // 👇 THIS IS WHERE THE INSTALL STAGE GOES 👇
        stage('Install Modules') {
            steps {
                echo '📦 Installing Python dependencies...'
                bat 'pip install -r requirement.txt'
            }
        }

        stage('Run Automated Tracker') {
            steps {
                echo '🚀 Executing main.py...'
                bat 'python main.py'
            }
        }
    }
}
