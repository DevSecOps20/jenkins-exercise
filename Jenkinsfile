pipeline{
    agent any
    
    stages{
        stage("build"){
            steps{
                echo "====== build stage ======="
                sh 'echo he need some milk >> app.txt'
            }
        }
        stage("test"){
            steps{
                echo "====== test stage ======="
                sh 'test -f app.txt'
            }
        }
        stage("deploy"){
            steps{
                echo "====== deploy stage ======="
                sh 'mdkir deploy'
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