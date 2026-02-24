pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // NOTE: This will only work if you configured Jenkins to use "Pipeline script from SCM"
                checkout scm
                echo '✅ Code checked out successfully.'
            }
        }

        stage('Check Environment') {
            steps {
                // Using your exact explicit path
                bat '"C:\\Users\\Sanjjey Arumugam\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" --version'
                echo '✅ Python environment verified.'
            }
        }

        // ❌ The Install Modules stage has been removed because you don't need it! ❌

        stage('Run Automated Tracker') {
            steps {
                echo '🚀 Executing main.py...'
                // Using your exact explicit path
                bat '"C:\\Users\\Sanjjey Arumugam\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" main.py'
            }
        }
    }
}
