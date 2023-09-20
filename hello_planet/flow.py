# from prefect import flow
# from prefect import get_run_logger

# from loguru import logger
# import fsspec
# import yaml
# from pathlib import Path
# from prefect.deployments import run_deployment
# import datetime
# #TODO make a parent flow that calls this for each planet using the yaml loading

# @flow
# def hello_planet(planet: str = "Earth"):
#     prefect_logger = get_run_logger()

#     logger.warning(f"Loguru says hello {planet}!")
#     prefect_logger.warning(f"Prefect says hello {planet}")

# @flow
# def hello_solar_system():

#     prefect_logger = get_run_logger()
#     prefect_logger.info("Starting parent flow...")

#     config_dir = "./flow_configs"
#     fs = fsspec.filesystem('')
#     glob_path = config_dir.strip('/') + '/*.yaml'
#     prefect_logger.info(glob_path)
#     all_paths = fs.glob(glob_path)

#     prefect_logger.info(all_paths)
#     logger_test("hello joe is this how prefect loggers work?")


#     for config_path in all_paths:
#         config_json = yaml.safe_load(Path(config_path).open())

#     #planet_list = ["jupiter", "mars", "venus", "saturn"]
#     #for planet in planet_list:

#         prefect_logger.info(f"launching subflow for {config_json['planet']}")
#         run_deployment(
#             name="hello-planet/hello-planet-python-deployment",
#             parameters={"planet": config_json['planet']},
#             flow_run_name=f"{config_json['planet']}--{datetime.datetime.now().isoformat()}",
#             timeout=1,
#         )


# def logger_test(message):
#     logger = get_run_logger()
#     logger.warning(message)
#     print("wololo")