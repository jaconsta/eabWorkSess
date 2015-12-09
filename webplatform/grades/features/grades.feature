Feature: Manage Students grades

    Scenario: Wont find student Charles
        When I access the url "students/averagegrade/?from=Fall%202014&to=Summer%202015&student=Charles"
        Then I expect response status 400
        And I expect content "Student doesnt exists."

    Scenario: Wont find students start_date
        When I access the url "students/averagegrade/?from=Fall%201008&to=Summer%202015&student=Javier"
        Then I expect response status 400
        And I expect content "Start semester name doesnt exists."

    Scenario: Wont find students end_date
        When I access the url "students/averagegrade/?from=Fall%202014&to=Summer%204000&student=Javier"
        Then I expect response status 400
        And I expect content "End semester name doesnt exists."


    Scenario: Julian has no grades
        When I access the url "students/averagegrade/?from=Fall%202014&to=Spring%202015&student=Julian"
        Then I expect response status 400
        And I expect content "Student has no grades."

    Scenario: Grades for Phil who has only one grade
        When I access the url "students/averagegrade/?from=Fall%202014&to=Spring%202015&student=Phil"
        Then I expect response status 200
        And I expect the average grade 5

    Scenario: Get grades for Javier
        When I access the url "students/averagegrade/?from=Fall%202014&to=Spring%202015&student=Javier"
        Then I expect response status 200
        And I expect the average grade 6

    Scenario: Grades for Marc last semester
        When I access the url "students/averagegrade/?from=Fall 2015&to=Fall 2015&student=Marc"
        Then I expect response status 200
        And I expect the average grade 8.5