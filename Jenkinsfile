pipeline {
  agent any
  parameters{
    string(name: 'VERSION', defaultValue:'', description:'version to deploy on prod')
    choice(name: 'VERSION' , choices: ['1.1.0', '1.2.0', '1.3.0'] , description: '')
    booleanParam(name: 'executeTests', defaultValue : true, description: '')
  }
  stages {
    stage("build"){
      steps{
        echo 'building the application'
      }
    }
    stage("tests"){
      when{
        expression{
          params.executeTests
        }
      }
      steps{
        echo 'testing the application'
      }
    }
    stage("deploy"){
        input{
          message "Select the env to deploy to"
          ok "Done"
          parameters{
           choice(name: 'ENV' , choices: ['dev', 'STG', 'prod'] , description: '')
          }
        }
      steps{
        echo 'deploying the application'
<<<<<<< HEAD
        echo "deploying version ${VERSION}"
=======
        echo "deploying to ${ENV}"
>>>>>>> aab6ee9af8a78d255d0ba190aafd1338f9cb5a68
      }
    }
  }
}
