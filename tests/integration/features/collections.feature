Feature: Get Payments
    Scenario: Request a payment from a consumer (Payer)
        Given I have a valid collection auth token
        When I enter the following payment details
            | note         | amount | message | mobile     | product_id |
            | test payment | 600    | message | 0782631873 | 0001       |


