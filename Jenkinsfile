pipeline{
    agent any
    environment {
        APP_NAME='wallak applciations'
        APP_VERSION='1.0'
        DOCKER_REPO="hothaifaz11/"
        FILE_TO_TEST='./build-info.txt'
    }
    parameters {
        string(name: 'SEARCH_WORD')
    }
    
    stages{
        stage("build"){
            steps{
                echo "====== build stage ======="
                sh 'echo he need some milk >> app.txt'
                sh 'echo "welcome to the pipeline of applciation ${APP_NAME}\n we are in version ${APP_VERSION}" '
                sh '''
                    echo "application name: $APP_NAME ">> $FILE_TO_TEST
                    echo "$BUILD_NUMBER ">> $FILE_TO_TEST
                    date >> $FILE_TO_TEST
                    '''
                sh 'ls'
                sh 'cat $FILE_TO_TEST' 
            }
        }
        stage("test"){
                  
                parallel{
                    stage("file test"){
                        steps{
                            sh '''
                                if [ -f app.txt ]; then
                                    echo app exists
                                else
                                    echo ERROR: app.txt does not exist
                                    exit 1
                                fi
                            '''
                        }
                    }
                    stage("build info test"){
                        steps{
                            sh "python3 test.py ${params.SEARCH_WORD}"
                            
                        }
                    }
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