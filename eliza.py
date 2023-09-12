import re


def regExMagic(pattern, string):
    objectMatch = re.search(pattern, string)
    return objectMatch

    
def getUserInput():    
    patientInput = input("? ")
    problem = " " + patientInput.upper() + "  "
    problem = problem.replace("'","")
    return problem


def findKeyword():
    dataPointer=0
    saveKeywordNumber = -1
    textLocation = ''
    foundKeyword = ''
    for dataPointer in range(0,n1):
        if saveKeywordNumber > -1:
            pass
        elif dataElements[dataPointer] in problem:
            saveKeywordNumber = dataPointer
            textLocation = problem.find(dataElements[dataPointer])
            foundKeyword = dataElements[dataPointer]
    return saveKeywordNumber, textLocation, foundKeyword;


def conjugateString(text, keyword, location):
    dataPointer=36
    startInText = len(text)-len(keyword)-location
    conjugateText = " " + problem[-abs(startInText):len(text)]

    for dp in range(36,(36+n2),2):
            said=dataElements[dp]
            response=dataElements[dp+1]
            if said in conjugateText:
                conjugateText=conjugateText.replace(said, response)
            elif response in conjugateText:
                conjugateText=conjugateText.replace(response, said)
    if conjugateText.startswith(" ",1,2):
        conjugateText=" "+conjugateText.lstrip(" ")
 
    return conjugateText;

# -----INITIALIZATION-----

dataStatements = ['"CAN YOU","CAN I","YOU ARE","YOURE","I DONT","I FEEL"', '"WHY DONT YOU","WHY CANT I","ARE YOU","I CANT","I AM"," IM "', '"YOU","I WANT","WHAT","HOW","WHO","WHERE","WHEN","WHY"', '"NAME","CAUSE","SORRY","DREAM","HELLO","HI","MAYBE"', '"NO","YOUR","ALWAYS","THINK","ALIKE","YES","FRIEND"', '"COMPUTER","NOKEYFOUND"', '" ARE "," AM ","WERE ","WAS "," YOU "," I ","YOUR ","MY "', '" IVE "," YOUVE "," IM "," YOURE "', '"DON\'T YOU BELIEVE THAT I CAN."', '"PERHAPS YOU WOULD LIKE TO BE ABLE TO."', '"YOU WANT ME TO BE ABLE TO*"', '"PERHAPS YOU DON\'T WANT TO*"', '"DO YOU WANT TO BE ABLE TO*"', '"WHAT MAKES YOU THINK I AM*"', '"DOES IT PLEASE YOU TO BELIEVE I AM*"', '"PERHAPS YOU WOULD LIKE TO BE*"', '"DO YOU SOMETIMES WISH YOU WERE*"', '"DON\'T YOU REALLY*"', '"WHY DON\'T YOU*"', '"DO YOU WISH TO BE ABLE TO*"', '"DOES THAT TROUBLE YOU?"', '"TELL ME MORE ABOUT SUCH FEELINGS*"', '"DO YOU OFTEN FEEL*"', '"DO YOU ENJOY FEELING*"', '"DO YOU REALLY BELIEVE I DON\'T*"', '"PERHAPS IN G00D TIME I WILL*"', '"DO YOU WANT ME TO*"', '"DO YOU THINK YOU SHOULD BE ABLE TO*"', '"WHY CAN\'T YOU*"', '"WHY ARE YOU INTERESTED IN WHETHER OR NOT I AM*"', '"WOULD YOU PREFER IF I WERE NOT*"', '"PERHAPS IN YOUR FANTASIES I AM*"', '"HOW DO YOU KNOW YOU CAN\'T*"', '"HAVE YOU TRIED?"', '"PERHAPS YOU CAN NOW*"', '"DID YOU COME TO ME BECAUSE YOU ARE*"', '"HOW LONG HAVE YOU BEEN*"', '"DO YOU BELIEVE IT IS NORMAL TO BE*"', '"DO YOU ENJOY BEING*"', '"WE WERE DISCUSSING YOU-- NOT ME."', '"OH, I*"', '"YOU\'RE NOT REALLY TALKING ABOUT ME. ARE YOU?"', '"WHAT WOULD IT MEAN TO YOU IF YOU GOT*"', '"WHY DO YOU WANT*"', '"SUPPOSE YOU SOON GOT*"', '"WHAT IF YOU NEVER GOT*"', '"I SOMETIMES ALSO WANT*"', '"WHY DO YOU ASK?"', '"DOES THAT QUESTION INTEREST YOU?"', '"WHAT ANSWER WOULD PLEASE YOU THE MOST?"', '"WHAT DO YOU THINK?"', '"ARE SUCH QUESTIONS ON YOUR MIND OFTEN?"', '"WHAT IS IT THAT YOU REALLY WANT TO KNOW?"', '"HAVE YOU ASKED ANYONE ELSE?"', '"HAVE YOU ASKED SUCH QUESTIONS BEFORE?"', '"WHAT ELSE COMES TO MIND WHEN YOU ASK THAT?"', '"NAMES DON\'T INTEREST ME."', '"I DON\'T CARE ABOUT NAMES-- PLEASE GO ON."', '"IS THAT THE REAL REASON?"', '"DON\'T ANY OTHER REASONS COME TO MIND?"', '"DOES THAT REASON EXPLAIN ANYTHING ELSE?"', '"WHAT OTHER REASONS MIGHT THERE BE?"', '"PLEASE DON\'T APOLOGIZE."', '"APOLOGIES ARE NOT NECESSARY."', '"WHAT FEELINGS DO YOU HAVE WHEN YOU APOLOGIZE."', '"DON\'T BE SO DEFENSIVE!"', '"WHAT DOES THAT DREAM SUGGEST TO YOU?"', '"DO YOU DREAM OFTEN?"', '"WHAT PERSONS APPEAR IN YOUR DREAMS?"', '"ARE YOU DISTURBED BY YOUR DREAMS?"', '"HOW DO YOU DO .,. PLEASE STATE YOUR PROBLEM."', '"YOU DON\'T SEEM QUITE CERTAIN."', '"WHY THE UNCERTAIN TONE?"', '"CAN\'T YOU BE MORE POSITIVE?"', '"YOU AREN\'T SURE?"', '"DON\'T YOU KNOW?"', '"ARE YOU SAYING NO JUST TO BE NEGATIVE?"', '"YOU ARE BEING A BIT NEGATIVE."', '"WHY NOT?"', '"ARE YOU SURE?"', '"WHY NO?"', '"WHY ARE YOU CONCERNED ABOUT MY*"', '"WHAT ABOUT YOUR OWN*"', '"CAN\'T YOU THINK OF A SPECIFIC EXAMPLE?"', '"WHEN?"', '"WHAT ARE YOU THINKING OF?"', '"REALLY. ALWAYS?"', '"DO YOU REALLY THINK SO?"', '"BUT YOU ARE NOT SURE YOU."', '"DO YOU DOUBT YOU."', '"IN WHAT WAY?"', '"WHAT RESEMBLANCE DO YOU SEE?"', '"WHAT DOES THE SIMILARITY SUGGEST TO YOU?"', '"WHAT OTHER CONNECTIONS DO YOU SEE?"', '"COULD THERE REALLY BE SOME CONNECTION?"', '"HOW?"', '"YOU SEEM QUITE POSITIVE."', '"ARE YOU SURE?"', '"I SEE."', '"I UNDERSTAND."', '"WHY DO YOU BRING UP THE TOPIC OF FRIENDS?"', '"DO YOUR FRIENDS WORRY YOU?"', '"DO YOUR FRIENDS PICK ON YOU?"', '"ARE YOU SURE YOU HAVE ANY FRIENDS?"', '"DO YOU IMPOSE ON YOUR FRIENDS?"', '"PERHAPS YOUR LOVE FOR FRIENDS WORRIES YOU."', '"DO COMPUTERS WORRY YOU?"', '"ARE YOU TALKING ABOUT ME IN PARTICULAR?"', '"ARE YOU FRIGHTENED BY MACHINES?"', '"WHY DO YOU MENTION COMPUTERS?"', '"WHAT DO YOU THINK MACHINES HAVE TO DO WITH YOUR PROBLEM?"', '"DON\'T YOU THINK COMPUTERS CAN HELP PEOPLE?"', '"WHAT IS IT ABOUT MACHINES THAT WORRIES YOU?"', '"SAY, DO YOU HAVE ANY PSYCHOLOGICAL PROBLEMS?"', '"WHAT DOES THAT SUGGEST TO YOU?"', '"I SEE."', '"I\'M NOT SURE I UNDERSTAND YOU FULLY."', '"COME COME ELUCIDATE YOUR THOUGHTS."', '"CAN YOU ELABORATE ON THAT?"', '"THAT IS QUITE INTERESTING."', '1,3,4,2,6,4,6,4,10,4,14,3,17,3,20,2,22,3,25,3', '28,4,28,4,32,3,35,5,40,9,40,9,40,9,40,9,40,9,40,9', '49,2,51,4,55,4,59,4,63,1,63,1,64,5,69,5,74,2,76,4', '80,3,83,7,90,3,93,6,99,7,106,6']  # List with all of the DATA statememt lines
dataElements = ['CAN YOU', 'CAN I', 'YOU ARE', 'YOURE', 'I DONT', 'I FEEL', 'WHY DONT YOU', 'WHY CANT I', 'ARE YOU', 'I CANT', 'I AM', ' IM ', 'YOU', 'I WANT', 'WHAT', 'HOW', 'WHO', 'WHERE', 'WHEN', 'WHY', 'NAME', 'CAUSE', 'SORRY', 'DREAM', 'HELLO', 'HI', 'MAYBE', 'NO', 'YOUR', 'ALWAYS', 'THINK', 'ALIKE', 'YES', 'FRIEND', 'COMPUTER', 'NOKEYFOUND', ' ARE ', ' AM ', 'WERE ', 'WAS ', ' YOU ', ' I ', 'YOUR ', 'MY ', ' IVE ', ' YOUVE ', ' IM ', ' YOURE ', "DON'T YOU BELIEVE THAT I CAN.", 'PERHAPS YOU WOULD LIKE TO BE ABLE TO.', 'YOU WANT ME TO BE ABLE TO*', "PERHAPS YOU DON'T WANT TO*", 'DO YOU WANT TO BE ABLE TO*', 'WHAT MAKES YOU THINK I AM*', 'DOES IT PLEASE YOU TO BELIEVE I AM*', 'PERHAPS YOU WOULD LIKE TO BE*', 'DO YOU SOMETIMES WISH YOU WERE*', "DON'T YOU REALLY*", "WHY DON'T YOU*", 'DO YOU WISH TO BE ABLE TO*', 'DOES THAT TROUBLE YOU?', 'TELL ME MORE ABOUT SUCH FEELINGS*', 'DO YOU OFTEN FEEL*', 'DO YOU ENJOY FEELING*', "DO YOU REALLY BELIEVE I DON'T*", 'PERHAPS IN G00D TIME I WILL*', 'DO YOU WANT ME TO*', 'DO YOU THINK YOU SHOULD BE ABLE TO*', "WHY CAN'T YOU*", 'WHY ARE YOU INTERESTED IN WHETHER OR NOT I AM*', 'WOULD YOU PREFER IF I WERE NOT*', 'PERHAPS IN YOUR FANTASIES I AM*', "HOW DO YOU KNOW YOU CAN'T*", 'HAVE YOU TRIED?', 'PERHAPS YOU CAN NOW*', 'DID YOU COME TO ME BECAUSE YOU ARE*', 'HOW LONG HAVE YOU BEEN*', 'DO YOU BELIEVE IT IS NORMAL TO BE*', 'DO YOU ENJOY BEING*', 'WE WERE DISCUSSING YOU-- NOT ME.', 'OH, I*', "YOU'RE NOT REALLY TALKING ABOUT ME. ARE YOU?", 'WHAT WOULD IT MEAN TO YOU IF YOU GOT*', 'WHY DO YOU WANT*', 'SUPPOSE YOU SOON GOT*', 'WHAT IF YOU NEVER GOT*', 'I SOMETIMES ALSO WANT*', 'WHY DO YOU ASK?', 'DOES THAT QUESTION INTEREST YOU?', 'WHAT ANSWER WOULD PLEASE YOU THE MOST?', 'WHAT DO YOU THINK?', 'ARE SUCH QUESTIONS ON YOUR MIND OFTEN?', 'WHAT IS IT THAT YOU REALLY WANT TO KNOW?', 'HAVE YOU ASKED ANYONE ELSE?', 'HAVE YOU ASKED SUCH QUESTIONS BEFORE?', 'WHAT ELSE COMES TO MIND WHEN YOU ASK THAT?', "NAMES DON'T INTEREST ME.", "I DON'T CARE ABOUT NAMES-- PLEASE GO ON.", 'IS THAT THE REAL REASON?', "DON'T ANY OTHER REASONS COME TO MIND?", 'DOES THAT REASON EXPLAIN ANYTHING ELSE?', 'WHAT OTHER REASONS MIGHT THERE BE?', "PLEASE DON'T APOLOGIZE.", 'APOLOGIES ARE NOT NECESSARY.', 'WHAT FEELINGS DO YOU HAVE WHEN YOU APOLOGIZE.', "DON'T BE SO DEFENSIVE!", 'WHAT DOES THAT DREAM SUGGEST TO YOU?', 'DO YOU DREAM OFTEN?', 'WHAT PERSONS APPEAR IN YOUR DREAMS?', 'ARE YOU DISTURBED BY YOUR DREAMS?', 'HOW DO YOU DO .,. PLEASE STATE YOUR PROBLEM.', "YOU DON'T SEEM QUITE CERTAIN.", 'WHY THE UNCERTAIN TONE?', "CAN'T YOU BE MORE POSITIVE?", "YOU AREN'T SURE?", "DON'T YOU KNOW?", 'ARE YOU SAYING NO JUST TO BE NEGATIVE?', 'YOU ARE BEING A BIT NEGATIVE.', 'WHY NOT?', 'ARE YOU SURE?', 'WHY NO?', 'WHY ARE YOU CONCERNED ABOUT MY*', 'WHAT ABOUT YOUR OWN*', "CAN'T YOU THINK OF A SPECIFIC EXAMPLE?", 'WHEN?', 'WHAT ARE YOU THINKING OF?', 'REALLY. ALWAYS?', 'DO YOU REALLY THINK SO?', 'BUT YOU ARE NOT SURE YOU.', 'DO YOU DOUBT YOU.', 'IN WHAT WAY?', 'WHAT RESEMBLANCE DO YOU SEE?', 'WHAT DOES THE SIMILARITY SUGGEST TO YOU?', 'WHAT OTHER CONNECTIONS DO YOU SEE?', 'COULD THERE REALLY BE SOME CONNECTION?', 'HOW?', 'YOU SEEM QUITE POSITIVE.', 'ARE YOU SURE?', 'I SEE.', 'I UNDERSTAND.', 'WHY DO YOU BRING UP THE TOPIC OF FRIENDS?', 'DO YOUR FRIENDS WORRY YOU?', 'DO YOUR FRIENDS PICK ON YOU?', 'ARE YOU SURE YOU HAVE ANY FRIENDS?', 'DO YOU IMPOSE ON YOUR FRIENDS?', 'PERHAPS YOUR LOVE FOR FRIENDS WORRIES YOU.', 'DO COMPUTERS WORRY YOU?', 'ARE YOU TALKING ABOUT ME IN PARTICULAR?', 'ARE YOU FRIGHTENED BY MACHINES?', 'WHY DO YOU MENTION COMPUTERS?', 'WHAT DO YOU THINK MACHINES HAVE TO DO WITH YOUR PROBLEM?', "DON'T YOU THINK COMPUTERS CAN HELP PEOPLE?", 'WHAT IS IT ABOUT MACHINES THAT WORRIES YOU?', 'SAY, DO YOU HAVE ANY PSYCHOLOGICAL PROBLEMS?', 'WHAT DOES THAT SUGGEST TO YOU?', 'I SEE.', "I'M NOT SURE I UNDERSTAND YOU FULLY.", 'COME COME ELUCIDATE YOUR THOUGHTS.', 'CAN YOU ELABORATE ON THAT?', 'THAT IS QUITE INTERESTING.', '1', '3', '4', '2', '6', '4', '6', '4', '10', '4', '14', '3', '17', '3', '20', '2', '22', '3', '25', '3', '28', '4', '28', '4', '32', '3', '35', '5', '40', '9', '40', '9', '40', '9', '40', '9', '40', '9', '40', '9', '49', '2', '51', '4', '55', '4', '59', '4', '63', '1', '63', '1', '64', '5', '69', '5', '74', '2', '76', '4', '80', '3', '83', '7', '90', '3', '93', '6', '99', '7', '106', '6']    # List with all of the individual data elements
dataPointer=0
saveKeywordNumber = -1
textLocation = ''
foundKeyword = ''
s = []               # : DIM S(36)
rightReply = []      # : DIM R(36)
n = []               # : DIM N(36)

n1 = 36
n2 = 12    
n3 = 112    

for dataPointer in range(0,(n1+n2+n3)):
    z=str(dataElements[dataPointer])

dataPointer=dataPointer + 1

for x in range(0,n1):
    s.append(int(dataElements[dataPointer])-1) # -1 adj for 0 start
    l = int(dataElements[dataPointer+1])
    rightReply.append(s[x])
    n.append(s[x] + l - 1)
    dataPointer=dataPointer+2


# -----USER INPUT SECTION-----
print("\t\t\t  ELIZA")
print("\t\t    CREATIVE COMPUTING")
print("\t\t  MORRISTOWN, NEW JERSEY")
print("")
print("")
print("")

print("\nHI! I'M ELIZA. WHAT'S YOUR PROBLEM?")

previousProblem = ''

while True:
    problem = getUserInput()
    
    pattern = 'SHUT'

    if str(regExMagic(pattern, problem)) == "None":
        if problem == previousProblem:
            print("PLEASE DON'T REPEAT YOURSELF!")
        else:
            saveKeywordNumber, textLocation, foundKeyword = findKeyword()
            if saveKeywordNumber > -1:
                keywordNumber = saveKeywordNumber
                locationInText = textLocation
                conjugatedString=conjugateString(problem, foundKeyword, locationInText)
            else:
                keywordNumber = 35
            dataPointer=n1+n2
            foundResponse=dataElements[dataPointer+rightReply[keywordNumber]]
            rightReply[keywordNumber]=rightReply[keywordNumber]+1
            if rightReply[keywordNumber]>n[keywordNumber]:
                rightReply[keywordNumber]=s[keywordNumber]

            if foundResponse[len(foundResponse)-1] != "*":
                print(foundResponse)
                previousProblem=problem
            else:
                print(foundResponse.replace("*",conjugatedString))
                previousProblem=problem
            
    else:
        print("OK, I'll SHUT UP...")
        break