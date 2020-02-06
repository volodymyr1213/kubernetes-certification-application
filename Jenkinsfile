import hudson.EnvVars


/**
* This jenkins job created for kubernetes certification Practice
* Before run
*   Create repository on dockerhub and change variable {repository}
*   Create Jenkins job with developer/taskone/application location
*/

def app
def appname  = 'tasktwo'
def owner = 'fuchicorp'
def repository = "${owner}/kubernetes-certification"
def appLocation = "/developer/${appname}/application/"
def credentials = 'fuchicorp-dockerhub'


node {

  // Pooling the docker image
  checkout scm

  stage('Build docker image') {
    dir("${WORKSPACE}${appLocation}") {
      // Build the docker image
      app = docker.build("${repository}", "  . ")
    }
  }


  stage('Push image') {

     // Push docker image to the Docker hub
      docker.withRegistry('', "${credentials}") {
          app.push("${appname}.${BUILD_NUMBER}")
          app.push("${appname}.latest")
      }
  }

  stage('Clean up') {
    sh "docker rmi ${repository}:${appname}.${BUILD_NUMBER}"
    sh "docker rmi ${repository}:${appname}.latest"

  }
}
