import py5

t = 'hmm'

def setup():
    py5.size(300, 600)
    py5.background(0)

def draw():
    py5.background(0)
    py5.text(t, 20, 20)

def mouse_clicked():
    ask_text()

def ask_text():
    global t
    t = multiline_pane('hey!', 'text\nhere')
    
    
def multiline_pane(title='', default=''):
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
        return str(ta.getText())
    else:
        return default

py5.run_sketch()