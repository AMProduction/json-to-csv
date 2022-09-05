## The solution architecture

After exploring the sample [datasets](/data) I see here the typical ["star" schema](https://www.databricks.com/glossary/star-schema) to store the data. I suggest creating
three tables: the `bets`, the `games`, and the `players`. The table `bets` is the core table. For the analytical purpose,
I would split the field `bet_dt` (contains datetime "2021-10-04 12:02:26") into four additional fields: `year`,
`number of week`, `month`, and `date`. See the [ERD](https://drive.google.com/file/d/1AeRxW_Y7SpAYrOXgKZVxD02r718KF9as/view?usp=sharing) below


![ERD](/img/ERD.jpg "ERD")

## The solution overview

My solution is using [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) files as a most appropriate and easy to work with. They are ready to import into, for example
 [MS Excel](https://support.microsoft.com/en-us/office/import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba#ID0EBBN=Newer_versions) or [MS PowerBI](https://powerbi.tips/2016/04/import-csv-file-to-power-bi/).
Also, because of appending new portion of data to the same target CSV file we can [just refresh](https://docs.microsoft.com/en-us/power-bi/connect-data/refresh-data)
the source in PowerBI and have always the newest data.  

This solution we can (after small reworking) add to [the Airflow](https://airflow.apache.org/docs/apache-airflow/1.10.1/index.html) scheduler.  

The function `setup_targets()` is using for set-up targets files. We create files and write the headers if needs.

## The potential improvements

In case of using API we should do small refactoring and use [requests](https://pypi.org/project/requests/) library and work with JSON response.
It is easy to implement if we have got all need API access. After this refactoring we could put it into the Airflow and
run the job by schedule.

## The full-scale solution in the cloud

For really bigdata solution I would suggest use [MS Azure services](https://docs.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-analytical-processing) (I familiar most with them). Rewrite job to use
[Azure Databricks](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/data/stream-processing-databricks) to ingest stream data near to real time or run batch jobs and do base transformation.
Use [Azure Data Factory](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/data/hybrid-etl-with-adf) as a scheduler Databricks jobs. Instead of using CSV files we could use more traditional
Data Warehouse solution, create appropriate tables and ingest data to the tables [(Azure Data Lake Gen2](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/enterprise-data-warehouse) for example).
And for analyze and visualize use connection to the [Power BI](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/data/enterprise-bi-adf).
General architecture [overview see bellow](https://drive.google.com/file/d/19whAMy-MhAsZWexaU0KlTlAcH-NaP-fG/view?usp=sharing)

![Azure](/img/Azure%20Data%20Solution.jpg "Azure Data Pipeline")