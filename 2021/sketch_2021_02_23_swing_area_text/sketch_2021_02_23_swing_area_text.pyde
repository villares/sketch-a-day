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
    print input("Text Area")


def input(title=''):
    from javax.swing import JOptionPane, JScrollPane, JTextArea
    ta = JTextArea(20, 20)
    ta.setText('default text')
    result = JOptionPane.showConfirmDialog(None,
                                           JScrollPane(ta),
                                           title,
                                           # 2:OK/Cancel 0:Yes/No  1:Y/N/Cancel
                                           # -1:OK
                                           2,
                                           -1,  # -1:Plain message (no icon)
                                           )
    return (result, ta.getText())
