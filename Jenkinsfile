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
                bat '"C:\\Users\\Sanjjey Arumugam\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" --version'
                echo '✅ Python environment verified.'
            }
        }

        // 👇 THIS IS WHERE THE INSTALL STAGE GOES 👇
        stage('Install Modules') {
            steps {
                echo '📦 Installing Python dependencies...'
                bat '"C:\\Users\\Sanjjey Arumugam\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" install sqllite3 datetime'
            }
        }

        stage('Run Automated Tracker') {
            steps {
                echo '🚀 Executing main.py...'
                bat '"C:\\Users\\Sanjjey Arumugam\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" main.py'
            }
        }
    }
}
