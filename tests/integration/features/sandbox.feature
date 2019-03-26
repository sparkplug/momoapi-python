Feature: As a new library User, I should be able to create an account on the MOMO sandbox

  Scenario: Adding new account
    Given a user with the domain sparkpl.ug and subscription key 99e9cb10e8c04ea0b788334dc6346f13
    When I run the command "mtnmomo"
    And I fill in the "providerCallBackHost" with "sparkpl.ug"
    And I fill in the "Ocp-Apim-Subscription-Key" with "99e9cb10e8c04ea0b788334dc6346f13"
    Then I should get back the apiKey

  Scenario: Wrong subscription Key
    Given a user with the domain sparkpl.ug and subscription key 99e9cb10e8c04ea0b788334dc6346f13dg
    When I run the command "mtnmomo"
    And I fill in the "providerCallBackHost" with "sparkpl.ug"
    And I fill in the "Ocp-Apim-Subscription-Key" with "f83xx8d8xx6749f19a26e2265aeadg"
    Then I should get the message "Access denied due to invalid subscription key"

