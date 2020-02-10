from nltk.chat.util import Chat, reflections
pairs=[
    ['my name is (.*)',['hi %1']],
    [('hi|hello|hye'),['hey there','hi there','hey']],
    [('exit|quit'),['Bybye See u','miss u']],
    ['(.) in (.) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)from ?',['intellectoGlobal,Chennai']],
    ['(.) created (.) ?',['sharief created using NLTK python']],
    ['(.) weather in (.)',['the wather in %1 is usual its hot']],
    ['How are (.*) ?',['Im good what about you ?']],
    ['(.)help(.)',['I will Help You']],
    ['(.)lover|lovers(.)',['Google it ;)']],
    ['(.)share(.)',['please tell me which sector share u want? 1.banking 2.automobile 3.power sector']],
    ['(.*) name?',['My name is sharief\nwhats your name? ']]

]
reflections
my_dummy_reflections={
    'go':'gone',
    'exit':'Byebye see u',
    'hello':'hye there'
}
chat=Chat(pairs,my_dummy_reflections)
chat.converse()

