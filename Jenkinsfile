pipeline {

    agent any

    stages {

        stage('Checkout SCM') {

            steps {

                git branch: 'main',
                url: 'https://github.com/D-Shravani/-NotesAutomationFramework-Section-3.git'
            }
        }

        stage('Go To Project Folder') {

            steps {

                bat 'dir'
            }
        }

        stage('Install Dependencies') {

            steps {

                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests in Parallel') {

            steps {

                bat 'venv\\Scripts\\python.exe -m pytest tests -n 2 --html=reports/report.html --alluredir=allure-results'
            }
        }

        stage('Archive Reports') {

            steps {

                archiveArtifacts artifacts: 'reports/*, screenshots/*, logs/*, allure-results/*', allowEmptyArchive: true
            }
        }

        stage('Publish HTML Report') {

            steps {

                publishHTML([
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])
            }
        }

        stage('Publish Allure Report') {

            steps {

                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}