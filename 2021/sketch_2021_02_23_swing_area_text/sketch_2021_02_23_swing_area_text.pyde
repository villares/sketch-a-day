# https://docs.oracle.com/javase/tutorial/uiswing/components/dialog.html#create

s = 0

def setup():
    background(0)

def draw():
    global s
    circle(50, 50, s)
    s += 1
    if s > 100:
        s = 0

def keyPressed():
    print(input('Text Area', default='Some Text\ngoes here'))


def input(title='', default=''):
    from javax.swing import JOptionPane, JScrollPane, JTextArea
    ta = JTextArea(20, 20)
    ta.setText(default)
    result = JOptionPane.showConfirmDialog(None,
                                           JScrollPane(ta),
                                           title,
                                           JOptionPane.OK_CANCEL_OPTION,
                                           JOptionPane.PLAIN_MESSAGE,
                                           # JOptionPane.QUESTION_MESSAGE
                                           )
    if result == JOptionPane.OK_OPTION:
        return ta.getText()
    else: 
        return default

"""
messageType - Defines the style of the message. The Look and Feel manager may lay out the dialog differently depending on this value, and will often provide a default icon. The possible values are:

JOptionPane.ERROR_MESSAGE
JOptionPane.INFORMATION_MESSAGE
JOptionPane.WARNING_MESSAGE
JOptionPane.QUESTION_MESSAGE # question mark
JOptionPane.PLAIN_MESSAGE  # No icon

optionType - Defines the set of option buttons that appear at the bottom of the dialog box:
JOptionPane.DEFAULT_OPTION
JOptionPane.YES_NO_OPTION
JOptionPane.YES_NO_CANCEL_OPTION
JOptionPane.OK_CANCEL_OPTION 
# 2:OK/Cancel 0:Yes/No  1:Y/N/Cancel -1:OK

Results:
JOptionPane.YES_OPTION
JOptionPane.NO_OPTION
JOptionPane.CANCEL_OPTION
JOptionPane.OK_OPTION
JOptionPane.CLOSED_OPTION 
"""
