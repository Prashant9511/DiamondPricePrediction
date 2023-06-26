import sys
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import  StandardScaler

from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder


@dataclass
class DataTransformationConfig:
    artifact_dir=os.path.join(artifact_folder)
    transformed_train_file_path=os.path.join(artifact_dir, 'train.npy')
    transformed_test_file_path=os.path.join(artifact_dir, 'test.npy') 
    transformed_object_file_path=os.path.join( artifact_dir, 'preprocessor.pkl' )



class DataTransformation:
    def __init__(self,
                 feature_store_file_path):
       
        self.feature_store_file_path = feature_store_file_path

        self.data_transformation_config = DataTransformationConfig()


        self.utils =  MainUtils()
        
    
    
    @staticmethod
    def get_data(feature_store_file_path:str) -> pd.DataFrame:
        """
        Method Name :   get_data
        Description :   This method reads all the validated raw data from the feature_store_file_path and returns a pandas DataFrame containing the merged data. 
        
        Output      :   a pandas DataFrame containing the merged data 
        On Failure  :   Write an exception log and then raise an exception
        
        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        try:
            data = pd.read_csv(feature_store_file_path)
            data.rename(columns={"Price": TARGET_COLUMN}, inplace=True)


            return data
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_data_transformer_object(self):
        try:

            logging.info('Data Transformation initiated')
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info('Pipeline Initiated')

            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

            )

            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]

            )

            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            return preprocessor

            logging.info('Pipeline Completed')

        except Exception as e:
            raise CustomException(e, sys)
        

             
    def initiate_data_transformation(self) :
        """
            Method Name :   initiate_data_transformation
            Description :   This method initiates the data transformation component for the pipeline 
            
            Output      :   data transformation artifact is created and returned 
            On Failure  :   Write an exception log and then raise an exception
            
            Version     :   1.2
            Revisions   :   moved setup to cloud
        """

        logging.info(
            "Entered initiate_data_transformation method of Data_Transformation class"
        )

        try:
            dataframe = self.get_data(feature_store_file_path=self.feature_store_file_path)
           
            target_column_name = TARGET_COLUMN
            drop_columns = [target_column_name,'id']

            X = dataframe.drop(columns= drop_columns,axis=1)
            y = dataframe[TARGET_COLUMN] 
            
            
            X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2 )


            preprocessor = self.get_data_transformer_object()

            X_train_scaled =  preprocessor.fit_transform(X_train)
            X_test_scaled  =  preprocessor.transform(X_test)

            

            preprocessor_path = self.data_transformation_config.transformed_object_file_path
            os.makedirs(os.path.dirname(preprocessor_path), exist_ok= True)
            self.utils.save_object( file_path= preprocessor_path,
                        obj= preprocessor)
            
            logging.info('Preprocessor pickle file saved')

            train_arr = np.c_[X_train_scaled, np.array(y_train) ]
            test_arr = np.c_[ X_test_scaled, np.array(y_test) ]

            return (train_arr, test_arr, preprocessor_path)
        
           
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise CustomException(e, sys) from e




