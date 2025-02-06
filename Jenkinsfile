pipeline{
    agent any
    environment{
        DOCKER_IMAGE="mahdiboudaouara101/my-flask-app:v1.0 "
    }
    stages{
        stage("build"){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                }
                sh "docker build -t $DOCKER_IMAGE ."
                sh "docker push $DOCKER_IMAGE"
            }
        }
    }
}