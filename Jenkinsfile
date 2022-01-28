pipeline {
  agent any
  stages {
    stage("build"){
      steps{
        echo 'building the application'
      }
    }
    stage("build an image"){
      steps{
        echo ('building Docker image')
        withCredentials([usernamePassword(credentialsId: 'jaanuk-docker', passwordVariable: 'PASS', usernameVariable: 'USER')])
        sh "docker build -t jaanuk/devops:Test-1.0 ."
        sh "echo PASS | docker login -u $USER --password-stdin "
        sh "docker push jaanuk/devops:Test-1.0"
      }
    }
    stage("tests"){
      steps{
        echo 'testing the application'
      }
    }
  }
}