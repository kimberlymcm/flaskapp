This is code that was uploaded separately as a lambda function to AWS to
send the data in the IOT Core MQTT message to RDS MySql.

Package and Package.zip just include the one python package lambda needs

Lambda_package.zip is created by running 'zip lambda_package.zip -r .' in this folder

NOTE: I use Mac OS while AWS uses Linux. Due to that, the way the psychopg2
compiles on mac does not work with AWS lambda. To resolve that, I directly
downloaded the package from here: https://github.com/jkehler/awslambda-psycopg2
