#create guardrail:
response = client.create_guardrail(
    name='string',
    description='string',
    topicPolicyConfig={
        'topicsConfig': [
            {
                'name': 'string',
                'definition': 'string',
                'examples': [
                    'string',
                ],
                'type': 'DENY'
            },
        ]
    },
    contentPolicyConfig={
        'filtersConfig': [
            {
                'type': 'SEXUAL'|'VIOLENCE'|'HATE'|'INSULTS'|'MISCONDUCT'|'PROMPT_ATTACK',
                'inputStrength': 'NONE'|'LOW'|'MEDIUM'|'HIGH',
                'outputStrength': 'NONE'|'LOW'|'MEDIUM'|'HIGH',
                'inputModalities': [
                    'TEXT'|'IMAGE',
                ],
                'outputModalities': [
                    'TEXT'|'IMAGE',
                ]
            },
        ]
    },
    wordPolicyConfig={
        'wordsConfig': [
            {
                'text': 'string'
            },
        ],
        'managedWordListsConfig': [
            {
                'type': 'PROFANITY'
            },
        ]
    },
    sensitiveInformationPolicyConfig={
        'piiEntitiesConfig': [
            {
                'type': 'ADDRESS'|'AGE'|'AWS_ACCESS_KEY'|'AWS_SECRET_KEY'|'CA_HEALTH_NUMBER'|'CA_SOCIAL_INSURANCE_NUMBER'|'CREDIT_DEBIT_CARD_CVV'|'CREDIT_DEBIT_CARD_EXPIRY'|'CREDIT_DEBIT_CARD_NUMBER'|'DRIVER_ID'|'EMAIL'|'INTERNATIONAL_BANK_ACCOUNT_NUMBER'|'IP_ADDRESS'|'LICENSE_PLATE'|'MAC_ADDRESS'|'NAME'|'PASSWORD'|'PHONE'|'PIN'|'SWIFT_CODE'|'UK_NATIONAL_HEALTH_SERVICE_NUMBER'|'UK_NATIONAL_INSURANCE_NUMBER'|'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER'|'URL'|'USERNAME'|'US_BANK_ACCOUNT_NUMBER'|'US_BANK_ROUTING_NUMBER'|'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER'|'US_PASSPORT_NUMBER'|'US_SOCIAL_SECURITY_NUMBER'|'VEHICLE_IDENTIFICATION_NUMBER',
                'action': 'BLOCK'|'ANONYMIZE'
            },
        ],
        'regexesConfig': [
            {
                'name': 'string',
                'description': 'string',
                'pattern': 'string',
                'action': 'BLOCK'|'ANONYMIZE'
            },
        ]
    },
    contextualGroundingPolicyConfig={
        'filtersConfig': [
            {
                'type': 'GROUNDING'|'RELEVANCE',
                'threshold': 123.0
            },
        ]
    },
    blockedInputMessaging='string',
    blockedOutputsMessaging='string',
    kmsKeyId='string',
    tags=[
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    clientRequestToken='string'
)
