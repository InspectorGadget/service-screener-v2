# Service Screener

An open source guidance tool for AWS environments.

## Overview
Service Screener is a tool that runs automated checks on AWS environments and provide recommendations based on the [AWS Well Architected Framework](https://aws.amazon.com/architecture/well-architected/). 

AWS customers can use this tool on their own environments and use the recommendations to improve the Security, Reliability, Operational Excellence, Performance Efficiency and Cost Optimisation of their workloads. 

This tool aims to complement the [AWS Well Architected Tool](https://aws.amazon.com/well-architected-tool/). 

## How does it work?
Service Screener uses [AWS Cloudshell](https://aws.amazon.com/cloudshell/), a free serivce that provides a browser-based shell to run scripts using the AWS CLI. It runs multiple `describe` and `get` API calls to determine the configuration of your environment.

## How much does it cost?
Running this tool is free as it is covered under the AWS Free Tier. If you have exceeded the free tier limits, each run will cost less than $0.01.

## Prerequisites
1. Please review the [DISCLAIMER](./DISCLAIMER.md) before proceeding. 
2. You must have an existing AWS Account.
3. You must have an IAM User with sufficient read permissions. Here is a sample [policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_read-only-console.html). Additionally, The IAM User must also have full access to AWS CloudShell i.e. AWSCloudShellFullAccess. 

## Installing service-screener V2
1. [Log in to your AWS account](https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html#start-session) using the IAM User with sufficient permissions described above. 
2. Launch [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html#launch-region-shell) in any region. 

![Launch AWS CloudShell](https://d39bs20xyg7k53.cloudfront.net/services-screener/p1-cloudshell.gif)

In the AWS CloudShell terminal, run this script this to install the dependencies:
```bash
python3 -m venv .
source bin/activate
rm -rf service-screner-v2
git clone https://github.com/aws-samples/service-screener-v2.git
cd service-screener-v2
pip install -r requirements.txt
alias screener="python3 $(pwd)/main.py"

```

![Install dependencies](https://d39bs20xyg7k53.cloudfront.net/services-screener/p2-dependencies.gif)

## Using Service Screener
When running Service Screener, you will need to specify the regions and services you would like it to run on. It currently supports Amazon Cloudfront, AWS Cloudtrail, Amazon Dynamodb, Amazon EC2, Amazon EFS, Amazon RDS, Amazon EKS, Amazon Elasticache, Amazon Guardduty, AWS IAM, Amazon Opensearch, AWS Lambda, and Amazon S3.

We recommend running it in all regions where you have deployed workloads in. Adjust the code samples below to suit your needs then copy and paste it into Cloudshell to run Service Screener. 

**Example 1: Running in the Singapore region, checking all services**
```
screener --regions ap-southeast-1 
```

**Example 2: Running in the Singapore region, checking only Amazon S3**
```
screener --regions ap-southeast-1 --services s3
```

**Example 3: Running in the Singapore & North Virginia regions, checking all services**
```
screener --regions ap-southeast-1,us-east-1
```

**Example 4: Running in the Singapore & North Virginia regions, checking RDS and IAM**
```
screener --regions ap-southeast-1,us-east-1 --services rds,iam
```

**Example 5: Running in the Singapore regions, by filtered resources based on tags (e.g: Name=env Values=prod and Name=department Values=hr,coe)**
```
## NOT SUPPORTED YET, RELEASE SOON
screener --regions ap-southeast-1 --filters env=prod%department=hr,coe
```

**Example 6: Running in all regions, and all services**
```
screener --regions ALL
```

### Other parameters
```bash
##mode
--mode api-full | api-raw | report

# api-full: give full results in JSON format
# api-raw: raw findings
# report: generate default web html
```
![Get Report](https://d39bs20xyg7k53.cloudfront.net/services-screener/p3-getreport.gif)

### Downloading the report
The output is generated as an ~/service-screener-v2/output.zip file. 
You can [download the file](https://docs.aws.amazon.com/cloudshell/latest/userguide/working-with-cloudshell.html#files-storage) in the CloudShell console by clicking the *Download file* button under the *Actions* menu on the top right of the Cloudshell console. 

![Download Output](https://d39bs20xyg7k53.cloudfront.net/services-screener/p4-outputzip.gif)

Once downloaded, unzip the file and open 'index.html' in your browser. You should see a page like this:

![front page](https://d39bs20xyg7k53.cloudfront.net/services-screener/service-screener.jpg?v1)

Ensure that you can see the service(s) run on listed on the left pane.
You can navigate to the service(s) listed to see detailed findings on each service. 

![Sample Output](https://d39bs20xyg7k53.cloudfront.net/services-screener/p5-sample.gif)

## Using the report 
The report provides you an easy-to-navigate dashboard of the various best-practice checks that were run. 

Use the left navigation bar to explore the checks per service. You can then expand on each check to read a description of the check, find out which resources were highlighted, and read a recommendation on how to remediate the finding.  

## Contributing to service-screener
We encourage public contributions! Please review [CONTRIBUTING](./CONTRIBUTING.md) for details on our code of conduct and development process.

## Contact
Please review [CONTRIBUTING](./CONTRIBUTING.md) to raise any issues. 

## Security
See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License
This project is licensed under the Apache-2.0 License.

