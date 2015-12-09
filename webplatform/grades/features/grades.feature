Feature: Manage Students grades

    Scenario: Get grades 1
        When I access the url "students/averagegrade/?from=Fall%202014&to=Summer%202015&student=Javier"
        Then I expect response status 200