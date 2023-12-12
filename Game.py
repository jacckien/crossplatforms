import re


def is_web():
    return "__BRYTHON__" in globals()

def write(message, end=' '):
    if is_web():
        from browser import document
        console = document.getElementById('console')
        p = document.createElement('p')
        p.textContent = '> ' + message
        console.appendChild(p)
        console.scrollTop = console.scrollHeight
    else:
        print(message, end = end)


async def read():
    if is_web():
        from browser import document, aio
        inp = document.getElementById('input')
        while True:
            event = await aio.event(inp, 'keydown')
            if event.key == 'Enter':
                tmp = event.target.value
                event.target.value = ''
                write(tmp)
                return tmp
    else:
        return input()


def run(function):
    if is_web():
        from browser import aio
        aio.run(function)
    else:
        import asyncio
        asyncio.run(function)


def instr():
    write("I WILL ASK YOU A SERIES OF SHORT QUESTIONS, WHICH YOU WILL\n")
    write("REPLY BY TYPING IN THE CORRESPONDING ANSWER TO THE\n")
    write("QUESTION.\n")
    write("      EXAMPLE: WHAT IS YOUR SEX?\n")
    write("              M=MALE\n")
    write("              F=FEMALE\n")
    write("M AND F ARE THE POSSIBLE REPLIES TO THE QUESTION, ANSWER\n")
    write("LIKE THIS:\n")
    write("          CHOSE ONE OF THE LETTERS ABOVE?\n")
    write("TYPING AN M SIGNIFIES YOU LIKE A MALE.\n")

async def game():
    q = 0
    write("              LIFE EXPECTANCY\n")
    write("             CREATIVE COMPUTING\n")
    write("            MORRISON, NEW JERSEY\n\n\n")
    write("THIS IS A LIFE EXPECTANCY TEST.\n")
    write("DO YOU WISH INSTRUCTIONS 'Y/N'\n")
    i = await read()
    if i != "N":
        instr()
    Q1 = [
        "+++SEX+++",
        "ARE YOU MALE OR FEMALE?",
        "M= MALE.",
        " F= FEMALE.",
        "+++LIFE STYLE+++",
        "WHERE DO YOU LIVE?",
        "G= IF YOU LIVE IN AN URBAN AREA WITH A POPULATION OVER 2 MIL.",
        "K= IF YOU LIVE IN A TOWN UNDER 10,000, OR ON A FARM.",
        " I= NEITHER.",
        "HOW DO YOU WORK?",
        "M= IF YOU WORK BEHIND A DESK.",
        "L= IF YOUR WORK REQUIRES HEAVY PHYSICAL LABOR.",
        " I= NONE OF THE ABOVE.",
        "HOW LONG DO YOU EXERCISE STRENUOUSLY,",
        "(TENNIS, RUNNING, SWIMMING, ETC.)?",
        "F= FIVE TIMES A WEEK FOR AR LEAST A HALF HOUR.",
        "K= JUST TWO OR THREE TIMES A WEEK.",
        " I= DO NOT EXERCISE IN THIS FASHION.",
        "WHO DO YOU LIVE WITH?",
        "N= IF YOU LIVE WITH A SPOUSE, FRIEND, OR IN A FAMILY.",
        "H= IF YOU'VE LIVED ALONE FOR 1-10 YEARS SINCE AGE 25.",
        "G= FOR 11-20 YEARS.",
        "M= FOR 21-30 YEARS.",
        "E= FOR 31-40 YEARS.",
        " D= MORE THAN 40 YEARS.",
        "+++PSYCHE+++",
        "DO YOU SLEEP MORE THAN 10 HOURS A NIGHT?",
        "I= NO.",
        " E=YES.",
        "+++MENTAL STATE+++",
        "M= IF YOU ARE INTENSE, AGGRESSIVE, OR EASILY ANGERED.",
        "L= IF YOU ARE EASY GOING, RELAXED, OR A FOLLOWER.",
        " I= NEITHER.",
        "+++HOW YOU FEEL+++",
        "ARE YOU HAPPY OR UNHAPPY?",
        "J= HAPPY.",
        "G= UNHAPPY.",
        " I= NEITHER.",
        "+++FACTORS+++",
        "HAVE YOU HAD A SPEEDING TICKET IN THE LAST YEAR?",
        "H= YES.",
        " I=NO.",
        "+++INCOME+++",
        "DO YOU EARN MORE THAN $50,000 A YEAR?",
        "G= YES.",
        " I=NO.",
        "+++SCHOOLING+++",
        "J= IF YOU HAVE FINISHED COLLEGE.",
        "L= IF YOU HAVE FINISHED COLLEGE WITH A GRADUATE",
        "OR PROFESSIONAL DEGREE.",
        " I= NOTHING LISTED.",
        "+++AGE+++",
        "ARE YOU 65 OR OLDER AND STILL WORKING?",
        "L= YES.",
        " I= NO.",
        "+++HEREDITY+++",
        "K= IF ANY GRANDPARENTS LIVED TO 85 YEARS OLD.",
        "O= IF ALL FOUR GRANDPARENTS LIVED TO 80 YEARS OLD.",
        " I= NO GRANDPARENTS QUALIFY IN THE ABOVE.",
        "HAS ANY PARENT DIED OF A STROKE OR HEART ATTACK",
        "BEFORE THE AGE OF 50?",
        "E= YES.",
        " I= NO.",
        "+++FAMILY DISEASES+++",
        "ANY PARENT, BROTHER, OR SISTER UNDER 50 HAS (OR HAD) ",
        "CANCER, A HEART CONDITION, OR DIABETES SINCE CHILDHOOD?",
        "M= YES.",
        " I= NO.",
        "+++HEALTH+++",
        "HOW MUCH DO YOU SMOKE?",
        "A= IF YOU SMOKE MORE THAN TWO PACKS A DAY.",
        "C= ONE TO TWO PACKS A DAY.",
        "M= ONE HALF TO ONE PACK A DAY.",
        " I= DON'T SMOKE.",
        "+++DRINK+++",
        "DO YOU DRINK THE EQUIVALENT OF A ",
        "QUARTER BOTTLE OF ALCOHOLIC BEVERAGE A DAY?",
        "H= YES.",
        " I= NO.",
        "+++WEIGHT+++",
        "A= IF YOU ARE OVERWEIGHT BY 50 POUNDS OR MORE.",
        "E= OVER BY 30-50 POUNDS.",
        "G= OVER BY 10-30 POUNDS.",
        " I= NOT OVER WEIGHT.",
        "+++CHECKUPS+++",
        "DO YOU?  IF YOU ARE A MALE OVER 40 HAVE AN ANNUAL CHECKUP?",
        "K= YES.",
        " I= IF NO OR NOT A MALE OR UNDER 40 YEARS OLD.",
        "DO YOU? IF YOU ARE A WOMAN SEE A GYNECOLOGIST ONCE A YEAR?",
        "K= YES.",
        " I= IF NO OR NOT A WOMAN.",
        "+++CURRENT AGE+++",
        "K= IF YOU ARE BETWEEN 30 AND 40 YEARS OLD.",
        "L= BETWEEN 40 AND 50.",
        "F= BETWEEN 50 AND 70.",
        "N= OVER 70.",
        " I= UNDER 30.",
        ""
    ]
    r5 = 1
    living = list()
    perc = list()
    livingPr = ""
    percPr = ""
    string = ""
    m = 0
    n = 0
    P1 = ["26%", "15%", "36%", "20%", "48%", "30%", "61%", "39%"]
    P2 = ["75%", "53%", "87%", "70%", "96%", "88%", "99.9%", "99.6%"]
    z = 72
    counter = 0
    Q = list()
    buff = list()
    c = ""
    a = "ABCDEMGHIJKLFNO"
    for q in range(len(Q1)):
        if Q1[q][0] != ' ':
            write(Q1[q],'\n')
        if Q1[q][1] == '=':
            buff.append(a[a.find(Q1[q][0])])
        if Q1[q][2] == '=':
            buff.append(a[a.find(Q1[q][1])])
        if Q1[q][0] == ' ':
            string = " ".join(buff)
            write(Q1[q], '\n')
            while c not in buff:
                write(string, '\n')
                write("CHOOSE ONE OF THE LETTERS ABOVE\n")
                c = await read()
            buff.clear()
            n = a.find(c)
            m = n - 9
            z += m
            c = ""
            r5 += 1
            if r5 > 21:
                living.append("YOU ARE EXPECTED TO LIVE TO THE AGE OF ")
                living.append(str(z))
                living.append(" YEARS\n")
                write(livingPr.join(living), '\n')
                if z < 60:
                    return 0
                else:
                    for y in range(60, z+1, 5):
                        counter += 1
                    perc.append("OUT LIVING ")
                    perc.append(P1[counter])
                    perc.append(" OF THE MEN AND ")
                    perc.append(P2[counter])
                    perc.append(" OF THE WOMEN.\n")
                    write(percPr.join(perc))
                break

# def main():
#     await game()
run(game())


