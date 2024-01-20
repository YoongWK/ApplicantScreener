# Applicant Screener
The Applicant Screener app is a comprehensive solution designed to streamline and automate the manual and labour-intensive recruitment screening process for organisations. Leveraging UiPath Studio for robotic process automation, the app integrates AI technologies such as OpenAI Generative Pre-trained Transformer (GPT) models for text classification and resume information extraction as well as the Doc2Vec Natural Language Processing (NLP) algorithm for applicant match scoring.

By harnessing the power of AI with automation, the app helps to expedite the screening process of large volumes of job applications in organisations while maintaining a high standard of accuracy, consistency, and fairness in evaluating the potential of candidates across various job postings. Organisations using the app will experience lower manpower costs, reduced hiring time, and better-informed hiring decisions.

<br />

## Instructions for Basic Setup
> Step 1: Download the app

```bash
git clone https://github.com/YoongWK/ApplicantScreener.git
cd ApplicantScreener
```

> Step 2: Create the Python virtual environment

```bash
python -m venv .venv
```

> Step 3: Set the execution policy of the current user to unrestricted

```bash
Set-ExecutionPolicy -ExecutionPolicy Unrestricted  -Scope CurrentUser
```

> Step 4: Activate the virtual environment

```bash
.venv\Scripts\activate
```

> Step 5: Install the required libraries into the virtual environment

```bash
pip install -r requirements.txt
```

> Step 6: Add your company email account to your Microsoft 365 Outlook app

> Step 7: Sign in to Orchestrator in UiPath Studio

> Step 8: Open the 'IdentifyAppliedJobPosition.xaml' workflow in UiPath Studio, click on the configure option of the HTTP Request activity, and replace the Authorization parameter with

```bash
Bearer [Your OpenAI API Key]
```

<br />

## Additional Instructions to Setup Simulated Job Application Emails in Company Email Account
> Step 1: Add your applicant email account to your Microsoft 365 Outlook app

> Step 2: Open the 'EmailApplications.xlsx' file in the 'Sample Job Applications' folder and replace the values in the 'To' column with your company email account

> Step 3: Run the 'SendSampleJobApplicationEmails.xaml' workflow in in the 'Sample Job Applications' folder in UiPath Studio

<br />

## Instructions to Run the Applicant Screener App
> Step 1: Update the 'JobPosting.xlsx' file with your company's job postings

> Step 2: Run the 'Main.xaml' workflow in UiPath Studio

<br />

## Expected Outputs
1. Invalid job application emails are replied with instructions for resubmission and moved to the 'Invalid' folder in the company's email Inbox
2. Valid job application emails are move to their respective job position folders
3. A 'JobApplication_[Date]_[Time].xlsx' file is created with all the extracted job applicant details in their respective job position sheets, sorted by descending match score
4. Resumes of all job applicants are stored in their respective job position subfolders in the 'Resumes' folder