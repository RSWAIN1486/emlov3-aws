import boto3
import subprocess

def push_docker_image(repository_name, image_tag, docker_image):
    # Create a Boto3 ECR client
    ecr_client = boto3.client('ecr')

    # Get the ECR registry ID and repository URI
    # response = ecr_client.describe_repositories(repositoryNames=[repository_name])
    # registry_id = response['repositories'][0]['registryId']
    repository_uri = 'public.ecr.aws/r3o6f2a0/emlov3-gpt'

    # Authenticate Docker with ECR
    # ecr_auth_response = ecr_client.get_authorization_token()
    # print(ecr_auth_response['authorizationData'][0])
    # username, password = ecr_auth_response['authorizationData'][0]['authorizationToken'].split(':')
    # ecr_registry = ecr_auth_response['authorizationData'][0]['proxyEndpoint']
    # docker_login_cmd = f'docker login -u {username} -p {password} {ecr_registry}'
    # You can execute the 'docker login' command here using 'subprocess' or other methods.
    docker_login_cmd = f'docker login'
    subprocess.call(docker_login_cmd, shell=True)

    # Tag the Docker image with the ECR repository URI
    docker_tag = f'{repository_uri}:{image_tag}'
    docker_tag_cmd = f'docker tag {docker_image} {docker_tag}'
    # Execute the 'docker tag' command here using 'subprocess' or other methods.
    subprocess.call(docker_tag_cmd, shell=True)

    # Push the Docker image to ECR
    docker_push_cmd = f'docker push {docker_tag}'
    # Execute the 'docker push' command here using 'subprocess' or other methods.
    subprocess.call(docker_push_cmd, shell=True)

if __name__ == "__main__":
    repository_name = 'emlov3-gpt'  # Replace with your ECR repository name
    image_tag = 'latest'  # Replace with the desired image tag (e.g., version number)
    docker_image = 'gpt-script-gradio-aws:latest'  # Replace with the name of your Docker image

    push_docker_image(repository_name, image_tag, docker_image)
