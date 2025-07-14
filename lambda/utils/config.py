import os
import boto3

class Config:
    BUCKET_NAME = os.environ['BUCKET_NAME']
    DDSTRIBUTION_DOMAIN = os.environ['DDSTRIBUTION_DOMAIN']
    BEDROCK_INVOKE_JOB_ROLE = os.environ['BEDROCK_ROLE_ARN']
    VECTOR_DIMENSION = 1024
    VECTOR_TEXT_DIMENSION = 1024
    OPENSEARCH_ENDPOINT = os.environ['OPENSEARCH_ENDPOINT']
    COLLECTION_INDEX_NAME = 'image-index-multi-1024'
    MULTIMODEL_LLM_ID = 'amazon.nova-pro-v1:0' # 'anthropic.claude-3-haiku-20240307-v1:0'
    RERANK_LLM_ID = 'amazon.nova-pro-v1:0'
    EMVEDDINGMODEL_ID = 'amazon.titan-embed-image-v1'
    IMG_DESCN_PROMPT = """
        You are analyzing a calculus question that includes a mathematical diagram. Your task is to provide a detailed description of both the question text and the diagram.

        Follow these steps in order:

        1. First, carefully read and understand the question text in the image {$IMAGE}.

        2. Next, examine the mathematical diagram in the image with the context from the question text in mind.

        3. Then, in Markdown format, provide the following comprehensive analysis:

        a. **Question Text Transcription**:
        - Provide a verbatim transcription of the question text
        - Include any given information, constraints, or instructions

        b. **Mathematical Concepts**: 
        - List the key calculus concepts present in the question (e.g., derivatives, integrals, limits, series, etc.)

        c. **Diagram Analysis**: 
        - Describe the mathematical diagram in detail
        - Identify all labeled points, curves, regions, and coordinates
        - Note any special mathematical notations or symbols
        - Explain how the diagram relates to the question text

        d. **Question Objective**: 
        - Clearly identify what the student needs to calculate, prove, or determine
        - Note any constraints or special conditions

        e. **Relevant Formulas**: 
        - List any formulas that appear in the image
        - Include any standard formulas that would be needed to solve this problem

        Format your response as follows:

        # Calculus Question Analysis

        ## Question Text
        [Verbatim transcription of the question]

        ## Mathematical Concepts
        - Concept 1
        - Concept 2
        - Concept 3

        ## Diagram Analysis
        Detailed description of the mathematical diagram, including all labeled elements and how they relate to the question.

        ## Question Objective
        A clear summary of what the calculus problem is asking the student to do.

        ## Relevant Formulas
        - Formula 1
        - Formula 2

        Provide your response within <result> tags.

    """ 

    @staticmethod
    def get_aws_session():
        return boto3.Session()
