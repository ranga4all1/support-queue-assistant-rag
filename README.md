# Support Queue Assistant

This is your friendly customer-support-queue assistant which is a RAG application built with LLM.

<img src="images/banner.jpg"  width="600" height="300">

<!-- ![Support Queue Assistant](images/banner.jpg) -->

## Problem Description

**Support Queue Assistant** aims to address a common issue faced by B2B SaaS companies—managing high volumes of customer support inquiries efficiently and accurately. Customers frequently have questions related to account management, billing, technical issues, and general inquiries, and manually handling these queries can be resource-intensive for support teams.

#### Key Challenges:

- **Scalability**: As the number of customers grows, the volume of support queries increases, which can overwhelm support teams.
- **Response Time**: Customers expect quick and accurate responses, but delays can occur if support teams are overloaded.
- **Consistency**: Ensuring that responses are consistent and accurate across different customer interactions can be challenging.

To solve these problems, **Support Queue Assistant** leverages a Retrieval-Augmented Generation (RAG) application that provides relevant, real-time responses to customer inquiries by retrieving data from a pre-defined knowledge base and generating accurate, context-specific responses.

## Project overview

#### What Does the Support Queue Assistant Do?

The **Support Queue Assistant** helps users by providing immediate and accurate answers to common support questions. Key functionalities include:

- **Real-Time Assistance**: Users can chat with the assistant to ask questions like "How do I reset my password?" or "What payment methods do you accept?".
- **Knowledge Base Retrieval**: The system pulls relevant information from the knowledge base to generate helpful responses.
- **Consistency and Accuracy**: Responses are based on predefined categories and intents, ensuring users receive consistent answers across similar inquiries.
- **Improved Response Time**: By automating common support queries, the assistant reduces the response time and workload on the human support team.

## Dataset

The dataset for this project is designed to address frequent customer support queries and contains 125 records. Each record includes information about the customer query, its category, intent, and a recommended response, along with related articles and tags for better searchability.

Here’s the structure of the dataset:

| Column              | Description                                                                            |
|---------------------|----------------------------------------------------------------------------------------|
| `id`                | Unique identifier for each query.                                                      |
| `question`          | The question posed by the customer.                                                    |
| `category`          | Broad category of the query (e.g., Account, Billing, Technical, General Inquiry).       |
| `subcategory`       | Specific subcategory within the broader category (e.g., Password Management, Integrations). |
| `intent`            | The intent of the query (e.g., Password Recovery, Payment Information, API & Integrations). |
| `product_feature`   | The product feature related to the query (e.g., Authentication & Security, Billing & Invoicing). |
| `response`          | The automated response provided to the user based on the query.                         |
| `related_articles`  | Links to related help articles that provide more detailed information.                  |
| `tags`              | Keywords to aid in search and retrieval of similar queries.                             |


## Running the application



## Using the application



## Code




## Experiments

### Retrieval evaluation

The basic approach - using 'minsearch' without any boosting - gave the following metrics:

- Hit rate: 96%
- MRR: 83%

The improved version (with tuned boosting):

- Hit rate: 97%
- MRR: 87%

The best boosting parameters:
```
boost = {
    'question': 2.32,
    'category': 0.34,
    'subcategory': 1.20,
    'intent': 1.52,
    'product_feature': 1.16,
    'response': 2.51,
    'related_articles': 0.24,
    'tags': 1.66,
}
```

### RAG flow evaluation

We used the `LLM-as-a-Judge metric` to evaluate the quality of our RAG flow.

For `gpt-4o-mini`, in a sample with 200 records, we had:

- 188 (94%) `RELEVANT`
- 11 (5.5%) `PARTLY_RELEVANT`
- 1 (.05%) `NON_RELEVANT`

We also tested `gpt-4o`:

- 189 (94.5%) `RELEVANT`
- 11 (5.5%) `PARTLY_RELEVANT`
- 0 (0%) `NON_RELEVANT`

The difference is minimal, so we opted for `gpt-4o-mini`.


## Monitoring


### Dashboards


## Conclusion

The **Support Queue Assistant** streamlines the customer support process for B2B SaaS companies by automating responses to frequent inquiries, improving response time, and ensuring consistency. The RAG-based approach ensures users get the most relevant and accurate information based on their needs, while freeing up valuable resources for more complex tasks.


## Background


## Acknowledgements


## Next steps