# Importing BaseModel from pydantic
# BaseModel is a class provided by Pydantic to create data models
# It automatically validates incoming data and converts it into the correct type
from pydantic import BaseModel

# Importing List from typing module
# List is used for type hinting(telling Python what type of data is expected)
from typing import List

# Defining a class SymptomInput that inherits from BaseModel
# This means SymptomInput will behave like a data validation schema
class SymptomInput(BaseModel):
    
    # 'name' is a field of type string
    # This represents the name of the symptom (e.g., fever, cough)
    name: str
    
    # 'severity' is also a string field
    # It indicates how serious the symptom is
    # Expected values: "low", "medium", "high"
    severity: str

# Defining another Pydantic model for request data
# This model will be used when sending data to the AI analysis system
class AIAnalysisRequest(BaseModel):
    
    # 'symptoms' is a list (array) of SymptomInput objects
    # This means the request will contain multiple symptoms
    # Each item in the list mush follow the SymptomInput structure
    symptoms: List[SymptomInput]

# Defining a response model for AI analysis result
# This structure will be returned after processing the request
class AIAnalysisResponse(BaseModel):
    
    # 'risk_level' is a string field
    # It represents the overall risk assessment(e.g., low, medium, high)
    risk_level: str
    
    # 'summary' is a string field
    # It contains a textual explanation or analysis of the symptoms
    summary: str
