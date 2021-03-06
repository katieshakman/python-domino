from domino import Domino
import os

domino = Domino("system-test/quick-start",
                host=os.environ['DOMINO_API_HOST'])


raw_datasets = domino.datasets_list()
print('Datasets:'+str(raw_datasets))

# Example using the current project's projectId to narrow down the datasets results to a specific project.  
raw_datasets_for_project = domino.datasets_list(domino._project_id)  
print('Datasets for current project:'+str(raw_datasets_for_project))

# Get the details of a dataset, if one exists for the current project
dataset_id = raw_datasets_for_project[0]['datasetId'] 
raw_datasets_details_for_project = domino.datasets_details(dataset_id)
print('Dataset details for current project and specified dataset: ', raw_datasets_details_for_project)