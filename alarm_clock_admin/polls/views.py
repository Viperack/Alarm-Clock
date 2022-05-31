from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


wakeUpTimes = ["07:00", "07:00", "07:00", "07:00", "07:00", "08:34", "09:00"]

def index(request):
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Alarm clock admin</title>
</head>
<body>
    <form action="validate" method="post">
        <table>
            <tr>
                <th>Day</th>
                <th>Wake up time</th>
            </tr>
            <tr>
                <td>Monday</td>
                <td>
                    <input type="time" name="monday" value="{wakeUpTimes[0]}">

                </td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>
                    <input type="time" name="tuesday" value="{wakeUpTimes[1]}">

                </td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>
                    <input type="time" name="wednesday" value="{wakeUpTimes[2]}">

                </td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>
                    <input type="time" name="thursday" value="{wakeUpTimes[3]}">

                </td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>
                    <input type="time" name="friday" value="{wakeUpTimes[4]}">

                </td>
            </tr>
            <tr>
                <td>Saturday</td>
                <td>
                    <input type="time" name="saturday" value="{wakeUpTimes[5]}">

                </td>
            </tr>
            <tr>
                <td>Sunday</td>
                <td>
                    <input type="time" name="sunday" value="{wakeUpTimes[6]}">

                </td>
            </tr>
        </table>
        <input type="submit" name="submit"> 
    </form>
</body>
</html>'''

    return HttpResponse(html)


def validate(request):
    global wakeUpTimes 

    if request.method == 'POST':
        wakeUpTimes = [request.POST["monday"], request.POST["tuesday"], request.POST["wednesday"], request.POST["thursday"], request.POST["friday"], request.POST["saturday"], request.POST["sunday"]]

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Alarm clock admin</title>
</head>
<body>
    <form action="validate" method="post">
        <table>
            <tr>
                <th>Day</th>
                <th>Wake up time</th>
            </tr>
            <tr>
                <td>Monday</td>
                <td>
                    <input type="time" name="monday" value="{wakeUpTimes[0]}">

                </td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>
                    <input type="time" name="tuesday" value="{wakeUpTimes[1]}">

                </td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>
                    <input type="time" name="wednesday" value="{wakeUpTimes[2]}">

                </td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>
                    <input type="time" name="thursday" value="{wakeUpTimes[3]}">

                </td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>
                    <input type="time" name="friday" value="{wakeUpTimes[4]}">

                </td>
            </tr>
            <tr>
                <td>Saturday</td>
                <td>
                    <input type="time" name="saturday" value="{wakeUpTimes[5]}">

                </td>
            </tr>
            <tr>
                <td>Sunday</td>
                <td>
                    <input type="time" name="sunday" value="{wakeUpTimes[6]}">

                </td>
            </tr>
        </table>
        <input type="submit" name="submit"> 
    </form>
</body>
</html>'''

    return HttpResponse(html)
