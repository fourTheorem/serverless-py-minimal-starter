# Serverless Python Minimal Template

This is a minimal Serverless Framework Python template that provides a simple starting point for building serverless applications with Python.

## Features

- Configured to use Python 3.9 runtime
- Includes the [aws-lambda-powertools-python Lambda layer](https://awslabs.github.io/aws-lambda-powertools-python/2.13.0/#install) for metrics, logging and tracing
- Uses [serverless-slic-watch-plugin](https://github.com/fourTheorem/slic-watch) plugin to add CloudWatch Alarms and Dashboards
- Uses [serverless-python-requirements](https://www.serverless.com/plugins/serverless-python-requirements) plugin for packaging Python dependencies
- Uses the [serverless-iam-roles-per-function](https://github.com/functionalone/serverless-iam-roles-per-function) plugin to manage IAM roles separately for each function

## Requirements

To use this template, you need to have the following software installed on your machine:

- Node.js (v16 or later), so you can run [The Serverless Framework](https://www.serverless.com/framework)
- Python (v3.9 or later)
- Docker (if using native dependencies that must be built for the target Linux architecture used by AWS Lambda)

You also need to have an AWS account and AWS CLI configured with your credentials.

## Usage

To create a new service based on this template, use the following command:

```
serverless create --template-url https://github.com/fourTheorem/serverless-minimal-starter --path <service-name>
```

Replace `<service-name>` with the desired name of your new service. This will create a new directory with the specified name, containing the files from this template.

To deploy the service, use the following command:

```
serverless deploy --stage <stage> --region <region>
```

Replace `<stage>` and `<region>` with the desired values. The default stage is `dev` and the default region is `eu-west-1`.

To delete all resources created as part of this service, use the following command:

```
serverless remove --stage <stage> --region <region>
```

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details.
