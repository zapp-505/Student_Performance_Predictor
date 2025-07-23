import os
import sys
from src.components.data_injestion import DataIngestion
from src.components.data_transformation import DataTransformation  
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

class TrainPipeline:
    def __init__(self):
        pass
    
    def initiate_training(self):
        """
        Run the complete training pipeline to generate artifacts
        """
        try:
            logging.info("Starting training pipeline...")
            
            # Step 1: Data Ingestion
            logging.info("Step 1: Data Ingestion")
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_injestion()
            logging.info(f"Data ingestion completed. Train: {train_data_path}, Test: {test_data_path}")
            
            # Step 2: Data Transformation
            logging.info("Step 2: Data Transformation")
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
                train_data_path, test_data_path
            )
            logging.info(f"Data transformation completed. Preprocessor saved at: {preprocessor_path}")
            
            # Step 3: Model Training
            logging.info("Step 3: Model Training")
            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f"Model training completed. R² Score: {r2_score}")
            
            logging.info("Training pipeline completed successfully!")
            return r2_score
            
        except Exception as e:
            logging.error(f"Error in training pipeline: {str(e)}")
            raise CustomException(e, sys)

def check_artifacts_exist():
    """
    Check if required artifacts exist
    """
    model_path = 'artifacts/model.pkl'
    preprocessor_path = 'artifacts/preprocessor.pkl'
    
    return os.path.exists(model_path) and os.path.exists(preprocessor_path)

if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    train_pipeline.initiate_training()