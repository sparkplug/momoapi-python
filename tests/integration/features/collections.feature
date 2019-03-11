Feature: Collections
    Scenario: Request a payment from a consumer (Payer)
        Given I have a valid user_id, auth_secret, and collections subscription key
        When I request for a payment with the following payment details
            | note         | amount | message | mobile     | product_id |
            | test payment | 600    | message | 0782631873 | 0001       |

        And  I check for transaction Status
        Then It should be successful

    Scenario: Failed Transfer
        Given I have a valid user_id, auth_secret, and collections subscription key
        When I enter the following payment details
            | note         | amount | message | mobile     | product_id |
            | test payment | 600    | message | 0782631873 | 0001       |

        And  I check for transaction Status
        Then It should be successful

    Scenario: Wrong Currency
        Given I have a valid user_id, auth_secret, and collections subscription key
        When I enter the following payment details
            | note         | amount | message | mobile     | product_id |
            | test payment | 600    | message | 0782631873 | 0001       |

        And  I check for transaction Status
        Then It should be successful

    Scenario: Non Mtn mobile
        Given I have a valid user_id, auth_secret, and collections subscription key
        When I enter the following payment details
            | note         | amount | message | mobile     | product_id |
            | test payment | 600    | message | 0782631873 | 0001       |

        And  I check for transaction Status
        Then It should be successful




