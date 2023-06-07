## Modern Data Architectures with Large Language Models

This repository provides the source code for use cases where applications interact with Large Language Model (LLM) using Langchain framework and text to SQL.
There are two modes demonstrated here:

**Mode 1** - Use of LLMs with Langchain via Amazon Sagemaker Jumpstart.  Amazon Sagemaker Jumpstart makes it simple to host LLMs as Sagemaker Endpoints enabling uses-cases for inference and embeddings generation.

Refer to Notebooks - 

i. Path - blogs/Simple-text-to-sql/mda_with_llm_langchain_smjumpstart_flant5xl.ipynb

Dependency - Run the cloudformation script (blogs/Simple-text-to-sql/mda-llm-cfn.yml ) prior to running the notebook.

Notes - The notebook showcases the concept with one database source but can be easily extended to other data bases. Connection code is commented for some of the supported databases. For those databases, ensure AWS Glue Crawler is first run on the underlying data sources.

**Mode 2** - Bring your own model api. In this case, provide API keys of your LLM to the Langchain framework.

i. Path - blogs/Simple-text-to-sql/mda_with_llm_langchain_byo_model.ipynb

Dependency - Run the cloudformation script (blogs/Simple-text-to-sql/mda-llm-cfn.yml ) prior to running the notebook.

Notes - The notebook showcases the concept with one database source but can be easily extended to other data bases. Connection code is commented for some of the supported databases. For those databases, ensure AWS Glue Crawler is first run on the underlying data sources.

ii. Path - blogs/Simple-text-to-sql/mda_with_llm_langchain_byo_model_wo_cloudformation.ipynb

Dependency - Ensure the Sagemaker execution role has all the required privileges mentioned in teh notebook. No need to run the cloudformation acript.

Notes - The notebook runs seamlessly for one data source. It can be easily extended to multiple data base sources.
For the sake of showing multiple data sources, Weather API has been added.

**Mode 3** - Use of LLMs with Langchain via Amazon Bedrock.

TBD

## Repository structure
The code in this repo is organized into the following sub-folders.

```├── README.md
├── blogs/
├──────/Simple text to sql
├── workshop/
├──────/TBD
├── images/

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

