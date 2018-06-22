import datetime
import requests
import pprint


def submit_form(id, data):
    url = 'https://docs.google.com/forms/d/e/{}/formResponse'.format(id)

    response = requests.post(url, data=data)

    pprint.pprint(response)
    pprint.pprint(response.text)

    if response.status_code != 200:
        raise Exception('Error submitting form!')


def submit_mentoring_form(
    mentor_email, mentor_name, date, student_email, session_type, duration,
    progress, subjects, student_care, email_receipt
):
    hours, remainder = divmod(duration, datetime.timedelta(hours=1))
    minutes, remainder = divmod(duration, datetime.timedelta(minutes=1))
    seconds = remainder.seconds

    for i in session_type:
        assert i in [
            'Intro',
            'Project inception', 'Middle of project', 'End of project',
            'Interview preparation and career advice', 'Other'
        ]

    assert progress in [
        'Excellent - It\'s going great.',
        'Average - The student is moving at an acceptable pace.',
        'I\'m worried about this student\'s progress.'
    ]

    data = {
        'emailAddress': mentor_email,
        'entry.838873576': mentor_name,
        'entry.1191000917_year': date.year,
        'entry.1191000917_month': date.month,
        'entry.1191000917_day': date.day,
        'entry.1269347964': student_email,
        'entry.1521715512': session_type,
        # Duration
        'entry.775489883_hour': hours,
        'entry.775489883_minute': minutes,
        'entry.775489883_second': seconds,
        'entry.2010663110': progress,
        'entry.1882714143': subjects,
        'entry.401267824': student_care,
        'emailReceipt': email_receipt
    }

    pprint.pprint(data)

    submit_form('1FAIpQLSfUCSyObKZDjjtAhIgc8r5FrA4VSUflq1dMK6QyYMv33LeEDQ', data)


def fill_mentoring_form():
    now = datetime.datetime.now()

    submit_mentoring_form(
        mentor_email='mathijs@mathijsfietst.nl',
        mentor_name='Mathijs de Bruin',
        date=now.date(),
        student_email='student@email.com',
        session_type=['Intro'],
        duration=datetime.timedelta(minutes=15),
        progress='Excellent - It\'s going great.',
        subjects='Code',
        student_care='None',
        email_receipt=True
    )


fill_mentoring_form()
