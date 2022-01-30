pipeline {
  agent any
  tools {
    maven 'maven'-e
  }
  stages {
    stage("build jar"){
      steps{
        script{
        echo 'building the application'
        sh 'mvn package'
        }
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
