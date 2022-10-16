
# Avid Code Test

<b>Simple Code Test</b>

Create a proper python script that calls the api method = POST

Take the results and create a csv file

All data returned in api call should be on one line in the csv file with the fields returned as the header
for example:


{"field1":value1,"field2":value2} 

should be

field1, field2
value1,value2

The Api call that will return your data is:
https://mko2aswez1.execute-api.us-west-2.amazonaws.com/V1/AvidCodeTest

ApiKey is in the .env file
Pass the apikey to the call by using the header x-api-key

<b>Questions: </b></br>
<ul>
<li>Why is bad practice to include the .env file in a git repository?
<li>What file would you create in a git repository to make sure that this file was not included?
</ul>
</br>
Send the answers to these questions to ahill@avidac.com</br>

To complete the assignment:</br>

Use git commands to do the following:</br>
<ul>
<li>Fork a copy of this repository into your git hub account
<li>Clone the repository to your local development computer
<li>Create a branch using the Git Checkout command
<li>Create the program in the app.py file in the repository
<li>Commit your changes and push this branch to your repository
<li>Upload the csv file to the github repository with your firstname_customerloan.csv firstname being your first name
<li>Send me the link to your repository (ahill@avidac.com)
 </ul>

To help you get started, here is a CURL example:

<p><code style="font-size: 5em">curl --location --request POST 'https://mko2aswez1.execute-api.us-west-2.amazonaws.com/V1/AvidCodeTest' --header 'x-api-key: qaEMpgfPNC4wvRuApSEiD7HzNRGrKTkd1yBFiwXP' </code></p>

<b>Stretch Goal</b></br>
Send me an email and let me know if you would like to attempt this. (ahill@avidac.com)</br>
Once you send a request to try this challenge I will send you the access key and secret key to use for your AWS profile.</br>
You will need to install the AWS Sdk and then issue a aws configure command.  It will ask you some questions.</br>
  </br>
<ul>
<li>The AWS Access Key ID is the Access Key I will send you.
<li>The AWS Secret Access Key is the Secret Key I will send you.
<li>The Default region name is us-west-2
<li>The Default output format is json
</ul>
You now have a credentials file on your machine with a profile in it representing the information you input above.</br>
</br>
See https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html for more information.</br>
</br>
<ul>
<li>Use the requirements file in the repository to install Boto3
<li>Write a method in the project that will send me an email using AWS Simple Notification Service or SNS.
<li>In the body of the email, send me the contents of the api call.
</ul>
</br>
<b>Lastly, and maybe most important, if you have questions, reach out and ask!</b>
