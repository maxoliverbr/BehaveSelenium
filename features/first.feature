# Created by Max at 18/12/2023
Feature: Test Login
  Test all login scenarios

  Scenario: Valid Login
    Given the user is in Disney home page
    When the user clicks on the Sign Up
    Then the app shows an email form
