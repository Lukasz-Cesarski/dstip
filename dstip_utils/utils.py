from IPython.display import HTML, display
from itertools import zip_longest

def yes_no_table(yes_no_dict):
    data = [["When TO USE", "When NOT TO USE"]]
    for yes_arg, no_arg in zip_longest(yes_no_dict['yes'], yes_no_dict['no'], fillvalue=''):
        data.append([yes_arg, no_arg])

    display(HTML(
   '<table><tr>{}</tr></table>'.format(
       '</tr><tr>'.join(
           '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in data)
       )))
