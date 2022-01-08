#include <iostream>
using namespace std;

int main()
{
    // declaring variables for subjects
    float sub1, sub2, sub3, sub4, sub5, sub6;
    // declaring variables for credit hours
    float credit_hour_1, credit_hour_2, credit_hour_3, credit_hour_4, credit_hour_5, credit_hour_6, total_credit_hours, total;
    // declaring variables for grade points
    float grade_point_1, grade_point_2, grade_point_3, grade_point_4, grade_point_5, grade_point_6, cgpa;

    // subject 1 section
    cout << "Enter marks of subject 1: ";
    // taking marks of subject 1
    cin >> sub1;
    cout << "Enter credit hours of subject 1: ";
    // taking credit hours of subjec 1
    cin >> credit_hour_1;

    if (sub1 < 100)
    {
        if (sub1 >= 84.5)
        {
            cout << "your grade is A+";
            grade_point_1 = 4;
        }
    }
    if (sub1 < 84.5)
    {
        if (sub1 >= 79.5)
        {
            cout << "your grade is A";
            grade_point_1 = 3.7;
        }
    }
    if (sub1 < 79.5)
    {
        if (sub1 >= 74.5)
        {
            cout << "your grade is B+";
            grade_point_1 = 3.3;
        }
    }
    if (sub1 < 74.5)
    {
        if (sub1 >= 69.5)
        {
            cout << "your grade is B";
            grade_point_1 = 3;
        }
    }
    if (sub1 < 69.5)
    {
        if (sub1 >= 64.5)
        {
            cout << "your grade is B-";
            grade_point_1 = 2.5;
        }
    }
    if (sub1 < 64.5)
    {
        if (sub1 >= 59.5)
        {
            cout << "your grade is c+";
            grade_point_1 = 2;
        }
    }
    if (sub1 < 59.5)
    {
        if (sub1 >= 54.5)
        {
            cout << "your grade is C";
            grade_point_1 = 1.5;
        }
    }
    if (sub1 < 54.5)
    {
        if (sub1 >= 49.5)
        {
            cout << "your grade is D";
            grade_point_1 = 1;
        }
    }
    if (sub1 < 49.5)
    {
        cout << "your grade is F";
        grade_point_1 = 0;
    }

    //subject 2 section
    cout << "\nEnter marks of subject 2: ";
    cin >> sub2;
    cout << "Enter credit hours of subject 2: ";
    cin >> credit_hour_2;
    if (sub2 < 100)
    {
        if (sub2 >= 84.5)
        {
            cout << "your grade is A+";
            grade_point_2 = 4;
        }
    }
    if (sub2 < 84.5)
    {
        if (sub2 >= 79.5)
        {
            cout << "your grade is A";
            grade_point_2 = 3.7;
        }
    }
    if (sub1 < 79.5)
    {
        if (sub2 >= 74.5)
        {
            cout << "your grade is B+";
            grade_point_2 = 3.3;
        }
    }
    if (sub2 < 74.5)
    {
        if (sub2 >= 69.5)
        {
            cout << "your grade is B";
            grade_point_2 = 3;
        }
    }
    if (sub2 < 69.5)
    {
        if (sub2 >= 64.5)
        {
            cout << "your grade is B-";
            grade_point_2 = 2.5;
        }
    }
    if (sub2 < 64.5)
    {
        if (sub2 >= 59.5)
        {
            cout << "your grade is c+";
            grade_point_2 = 2;
        }
    }
    if (sub2 < 59.5)
    {
        if (sub2 >= 54.5)
        {
            cout << "your grade is C";
            grade_point_2 = 1.5;
        }
    }
    if (sub2 < 54.5)
    {
        if (sub2 >= 49.5)
        {
            cout << "your grade is D";
            grade_point_2 = 1;
        }
    }
    if (sub2 < 49.5)
    {
        cout << "your grade is F";
        grade_point_2 = 0;
    }
    //subject section 3
    cout << "\nEnter marks of subject 3: ";
    cin >> sub3;
    cout << "Enter credit hours of subject 3: ";
    cin >> credit_hour_3;
    if (sub3 < 100)
    {
        if (sub3 >= 84.5)
        {
            cout << "your grade is A+";
            grade_point_3 = 4;
        }
    }
    if (sub3 < 84.5)
    {
        if (sub3 >= 79.5)
        {
            cout << "your grade is A";
            grade_point_3 = 3.7;
        }
    }
    if (sub3 < 79.5)
    {
        if (sub3 >= 74.5)
        {
            cout << "your grade is B+";
            grade_point_3 = 3.3;
        }
    }
    if (sub3 < 74.5)
    {
        if (sub3 >= 69.5)
        {
            cout << "your grade is B";
            grade_point_3 = 3;
        }
    }
    if (sub3 < 69.5)
    {
        if (sub3 >= 64.5)
        {
            cout << "your grade is B-";
            grade_point_3 = 2.5;
        }
    }
    if (sub3 < 64.5)
    {
        if (sub3 >= 59.5)
        {
            cout << "your grade is c+";
            grade_point_3 = 2;
        }
    }
    if (sub3 < 59.5)
    {
        if (sub3 >= 54.5)
        {
            cout << "your grade is C";
            grade_point_3 = 1.5;
        }
    }
    if (sub3 < 54.5)
    {
        if (sub3 >= 49.5)
        {
            cout << "your grade is D";
            grade_point_3 = 1;
        }
    }
    if (sub3 < 49.5)
    {
        cout << "your grade is F";
        grade_point_3 = 0;
    }
    //subject 4 section
    cout << "\nEnter marks of subject 4: ";
    cin >> sub4;
    cout << "Enter credit hours of subject 4: ";
    cin >> credit_hour_4;
    if (sub4 < 100)
    {
        if (sub4 >= 84.5)
        {
            cout << "your grade is A+";
            grade_point_4 = 4;
        }
    }

    if (sub4 < 84.5)
    {
        if (sub4 >= 79.5)
        {
            cout << "your grade is A";
            grade_point_4 = 3.7;
        }
    }
    if (sub4 < 79.5)
    {
        if (sub4 >= 74.5)
        {
            cout << "your grade is B+";
            grade_point_4 = 3.3;
        }
    }
    if (sub4 < 74.5)
    {
        if (sub4 >= 69.5)
        {
            cout << "your grade is B";
            grade_point_4 = 3;
        }
    }
    if (sub4 < 69.5)
    {
        if (sub4 >= 64.5)
        {
            cout << "your grade is B-";
            grade_point_4 = 2.5;
        }
    }
    if (sub4 < 64.5)
    {
        if (sub4 >= 59.5)
        {
            cout << "your grade is c+";
            grade_point_4 = 2;
        }
    }
    if (sub4 < 59.5)
    {
        if (sub4 >= 54.5)
        {
            cout << "your grade is C";
            grade_point_4 = 1.5;
        }
    }
    if (sub4 < 54.5)
    {
        if (sub4 >= 49.5)
        {
            cout << "your grade is D";
            grade_point_4 = 1;
        }
    }
    if (sub4 < 49.5)
    {
        cout << "your grade is F";
        grade_point_4 = 0;
    }

    //subject 5 section
    cout << "\nEnter marks of subject 5: ";
    cin >> sub5;
    cout << "Enter credit hours of subject 5: ";
    cin >> credit_hour_5;
    if (sub5 < 100)
    {
        if (sub5 >= 84.5)
        {
            cout << "your grade is A+";
            grade_point_5 = 4;
        }
    }

    if (sub5 < 84.5)
    {
        if (sub5 >= 79.5)
        {
            cout << "your grade is A";
            grade_point_5 = 3.7;
        }
    }
    if (sub5 < 79.5)
    {
        if (sub5 >= 74.5)
        {
            cout << "your grade is B+";
            grade_point_5 = 3.3;
        }
    }
    if (sub5 < 74.5)
    {
        if (sub5 >= 69.5)
        {
            cout << "your grade is B";
            grade_point_5 = 3;
        }
    }
    if (sub5 < 69.5)
    {
        if (sub5 >= 64.5)
        {
            cout << "your grade is B-";
            grade_point_5 = 2.5;
        }
    }
    if (sub5 < 64.5)
    {
        if (sub5 >= 59.5)
        {
            cout << "your grade is c+";
            grade_point_5 = 2;
        }
    }
    if (sub5 < 59.5)
    {
        if (sub5 >= 54.5)
        {
            cout << "your grade is C";
            grade_point_5 = 1.5;
        }
    }
    if (sub5 < 54.5)
    {
        if (sub5 >= 49.5)
        {
            cout << "your grade is D";
            grade_point_5 = 1;
        }
    }
    if (sub5 < 49.5)
    {
        cout << "your grade is F";
        grade_point_5 = 0;
    }

    //subject 6 section
    cout << "\nEnter marks of subject 6: ";
    cin >> sub6;
    cout << "Enter credit hours of subject 6: ";
    cin >> credit_hour_6;
    if (sub6 < 100)
    {
        if (sub6 >= 84.5)
        {
            cout << "your grade is A+";
            grade_point_6 = 4;
        }
    }
    if (sub6 < 84.5)
    {
        if (sub6 >= 79.5)
        {
            cout << "your grade is A";
            grade_point_6 = 3.7;
        }
    }
    if (sub6 < 79.5)
    {
        if (sub6 >= 74.5)
        {
            cout << "your grade is B+";
            grade_point_6 = 3.3;
        }
    }
    if (sub6 < 74.5)
    {
        if (sub6 >= 69.5)
        {
            cout << "your grade is B";
            grade_point_6 = 3;
        }
    }
    if (sub6 < 69.5)
    {
        if (sub6 >= 64.5)
        {
            cout << "your grade is B-";
            grade_point_6 = 2.5;
        }
    }
    if (sub6 < 64.5)
    {
        if (sub6 >= 59.5)
        {
            cout << "your grade is c+";
            grade_point_6 = 2;
        }
    }
    if (sub6 < 59.5)
    {
        if (sub6 >= 54.5)
        {
            cout << "your grade is C";
            grade_point_6 = 1.5;
        }
    }
    if (sub6 < 54.5)
    {
        if (sub6 >= 49.5)
        {
            cout << "your grade is D";
            grade_point_6 = 1;
        }
    }
    if (sub6 < 49.5)
    {
        cout << "your grade is F";
        grade_point_6 = 0;
    }

    // this total is the numerator in the formula of cgpa
    total = (grade_point_1 * credit_hour_1) + (grade_point_2 * credit_hour_2) + (grade_point_3 * credit_hour_3) + (grade_point_4 * credit_hour_4) + (grade_point_5 * credit_hour_5) + (grade_point_6 * credit_hour_6);

    // calculating total credit hours
    total_credit_hours = credit_hour_1 + credit_hour_2 + credit_hour_3 + credit_hour_4 + credit_hour_5 + credit_hour_6;

    // this is the formula of calculating cgpa
    // cgpa = no_of_subjects * (grade_point * credit_hour) / total_credit_hours
    cgpa = total / total_credit_hours;

    // this is the print statement for printing cgpa
    cout << "\nYour CGPA is :" << cgpa;

    return 0;
}