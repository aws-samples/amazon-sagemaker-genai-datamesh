Modern Data Architecture interactions with Amazon SageMaker and LangChain
================



#### Use AWS Cloud Formation to create the solution stack

We use AWS CloudFormation to create a SageMaker notebook called
`xyz` and an IAM role called `xyz`. Choose
**Launch Stack** for the Region you want to deploy resources to. All
parameters needed by the CloudFormation template have default values
already filled in. **This template takes
about 5 minutes to complete**.

<TBD>
After the stack is created successfully, navigate to the stack’s `Outputs` tab on the AWS CloudFormation console and note the values for
`LLMAppAPIEndpoint`. We use those in the subsequent steps.
