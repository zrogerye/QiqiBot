import random

QiqiLines = [
    'I am Qiqi. I am a zombie. I forgot what comes next.',
    'Did you ask me something? Sorry... I forgot.',
    'Hold my hand please. This wind could blow me away.',
    'I want to build a snowman. Will you help?',
    'I like coconut milk... But, I dont know what it tastes like.',
    'All of this is because of you. Thank you very much. Can you make me a promise? From now on, please, '
    'let me protect you. Do you accept? Yes or no?']


def voicelines(content):
    out = QiqiLines[random.randint(0, len(QiqiLines) - 1)]
    return out
