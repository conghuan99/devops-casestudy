pipeline {
    agent { label 'agent-01' }

    environment {
        DOCKER_IMAGE = "conghuan99/flask_app"
        DOCKER_TAG   = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo "Running unit tests..."
                sh '''
                    cd flask_app
                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt --quiet
                    venv/bin/python -m pytest test_app.py -v
		    
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo "Building Docker image ${DOCKER_IMAGE}:${DOCKER_TAG}..."
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ./flask_app
                    docker tag  ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                '''
            }
        }

        stage('Docker Push') {
            steps {
                echo "Pushing image to DockerHub..."
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker push ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to k3s cluster..."
                sh '''
                    # kubectl set image deployment/flask-app-deployment flask-app=${DOCKER_IMAGE}:${DOCKER_TAG}
                    # kubectl annotate deployment/flask-app-deployment kubernetes.io/change-cause="${DOCKER_IMAGE}:${DOCKER_TAG}" --overwrite

                    kubectl set image deployment/flask-app-deployment flask-app=${DOCKER_IMAGE}:${v7}
                    kubectl annotate deployment/flask-app-deployment kubernetes.io/change-cause="${DOCKER_IMAGE}:${v7}" --overwrite

		    # kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml

                    # rollback neu set image thành công nhưng rollout fail
                    if ! kubectl rollout status deployment/flask-app-deployment --timeout=60s; then
                      echo "Rollout failed! Rolling back..."
                      kubectl rollout undo deployment/flask-app-deployment
                      exit 1
                    fi
                '''
            }
        }

    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs above."
        }
    }
}
