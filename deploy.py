from hello_planet.flow import hello_planet, hello_solar_system 
from prefect.deployments import Deployment
from prefect_aws import ECSTask, S3Bucket
from prefect.filesystems import GitHub

hello_planet_deployment = Deployment.build_from_flow(
    flow=hello_planet,
    name="hello-planet-python-deployment",
    output="./deployment_yamls/hello-planet-python-deployment.yaml",
    infrastructure=ECSTask.load("my-ecs-task"),
    storage=S3Bucket.load("my-s3-bucket"),
)

hello_planet_deployment.apply()

hello_solar_system_deployment = Deployment.build_from_flow(
    flow=hello_solar_system,
    name="hello-solar-system-python-deployment",
    output="./deployment_yamls/hello-solar-system-python-deployment.yaml",
    infrastructure=ECSTask.load("my-ecs-task"),
    storage=S3Bucket.load("my-s3-bucket"),
)

hello_solar_system_deployment.apply()
