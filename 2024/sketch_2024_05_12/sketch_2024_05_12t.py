# from pathlib import Path
# 
# for ano in sorted(Path.cwd().parent.parent.iterdir()):
#     if ano.name.isnumeric():
#         for sf in ano.iterdir():
#             for sub in sf.iterdir():
#                 if sub.is_dir():            
#                     print(sf.name, sub.name)

import py5

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
    
print(multiline_pane('hey!', 'text\nhere'))
