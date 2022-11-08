# -*- encoding: utf-8 -*-
import openai
from api.config import OPENAI_API_KEY, GPT_MODEL


class TrainingService:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    '''
        Upload training file (JSONL) to openai cloud.
        Returns the id of the uploaded training file.
    '''
    def upload_file(self, filePath):
        with open(filePath) as f:
            response = openai.File.create(file=f, purpose='fine-tune')
            return response.get('id')

    '''
        Create a fine tuned model training job with uploaded training file
        Returns the job response
    '''
    def create_fine_tuned_model(self, training_file_id, model=GPT_MODEL):
        create_args = {
            "training_file": training_file_id,
            "model": model,
            "compute_classification_metrics": True,
            "classification_n_classes": 2,
            "batch_size": 128
        }
        r = openai.FineTune.create(**create_args)
        return r

    '''
        Get status of a training job
    '''
    def get_training_status(self, training_job_id):
        r = openai.FineTune.retrieve(id=training_job_id)
        return r

    '''
        Get a fined tuned model id
    '''
    def get_find_tuned_model_id(self, training_job_id):
        r = openai.FineTune.retrieve(self, id=training_job_id)
        return r.get('fine_tuned_model')

    '''
        List of all current fine tuned models
    '''
    def list_jobs(self):
        r = openai.FineTune.list()
        for deployment in r.data:
            print('{0}: {1} '.format(deployment.get("id"), deployment.get("fine_tuned_model")))
