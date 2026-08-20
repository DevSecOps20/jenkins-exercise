pipeline{
    agent any
    environment {
        APP_NAME='wallak applciations'
        APP_VERSION='1.0'
        DOCKER_REPO="hothaifaz11/"
        FILE_TO_TEST='./build-info.txt'
    }
    stages{
        stage("build"){
            steps{
                echo "====== build stage ======="
                sh 'echo he need some milk >> app.txt'
                sh 'echo "welcome to the pipeline of applciation ${APP_NAME}\n we are in version ${APP_VERSION}" '
                sh '''
                    echo "application name: $APP_NAME ">> $FILE_TO_TEST
                    echo "$BUILD_NUMER ">> $FILE_TO_TEST
                    date >> $FILE_TO_TEST
                    '''
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