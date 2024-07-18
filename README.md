Software Development
Home Assignment
Please solve the test using Python and provide the files as a ZIP.

Guidelines
You will be measured on:
● Architecture: Propose a suitable architecture that will allow for extensibility and
composability.
● Maintainability: Ideally, we want to be able to add more fields to the final object and additional
ways to output the data.
● Explainability: Your code should be self-explanatory.
● Correctness: It should do what it needs to do.
Constraints:
● The solution must be implemented in Python.
● Do not use any external platforms or services.
● Minimize the use of third-party packages; standard library usage is
preferred.

The purpose of this task is to demonstrate a basic ability to build a program that gets data from a URL
and presents it.
Get candidate data from the provided URL and extract their work experience. For each “candidate” that
you find there, extract the following:
● Name of the candidate
● Job experience (including role, dates, office location)
● If a certain candidate has “gaps” between two jobs, print the gap in between the job lines (Gap in
CV for X days) - you should add it to both forms of output (your call where the gaps will be in the
json).
Output String Example:

Hello Shimon Peres,
Worked as: Programmer, From Jan/20/2013 To Dec/31/2014 in New
York, NY, US Gap in CV for 20 days
Worked as: Programmer, From Jan/02/2010 To Dec/31/2012 in Newark,
NJ, US

Deliverables:
1. PythonScripts:
● For the data extraction, transformation, and backend automation tasks.
2. SampleData:
● Include any necessary JSON files or mock data for testing.
3. README.md:
● Provide instructions on how to run the scripts.
● Include any assumptions and design decisions made during the implementation.

This assignment aims to test your ability to handle data extraction and transformation while
maintaining a focus on clean, maintainable, and extensible code.
