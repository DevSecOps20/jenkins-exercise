pipeline{
    agent any
    environment {
        APP_NAME='wallak applciations'
        APP_VERSION='1.0'
        DOCKER_REPO="hothaifaz11/"
    }
    stages{
        stage("build"){
            steps{
                echo "====== build stage ======="
                sh 'echo he need some milk >> app.txt'
                sh 'echo "welcome to the pipeline of applciation ${APP_NAME}\n we are in version ${APP_VERSION}" '
            }
        }
        stage("test"){
            steps{
                echo "====== test stage ======="
                sh 'test -f app.txt'
                echo "for any details please visit: ${JOB_URL}. for build #${BUILD_NUMBER}"
            }
        }
        stage("deploy"){
            steps{
                echo "====== deploy stage ======="
                sh 'mkdir deploy'
                sh 'cp app.txt deploy/'
                sh 'ls deploy'
            }
        }
    }
    post{
        always{
            cleanWs()
        }
    }
}