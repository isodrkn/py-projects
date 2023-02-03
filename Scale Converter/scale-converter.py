import PySimpleGUI as sg

sg.theme('DarkGreen6')

layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Combo(['Select a scale' ,'km to mile', 'kg to pound', 'sec to min'],default_value = 'Select a scale', key = '-UNITS-'),
        sg.Button('Convert', key = '-CONVERT-')
    ],
    [sg.Text('Output', key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    
            

    if event == '-CONVERT-':
        
        input_value = values['-INPUT-']

        
        if not input_value.isnumeric():
            
            output_string = f'Enter a number'
            
            window['-OUTPUT-'].update(output_string)
            
        elif input_value.isnumeric():
            
            if values['-UNITS-'] == 'Select a scale':
                output_string = 'Please select a scale.'
                window['-OUTPUT-'].update(output_string)
            
            elif values['-UNITS-'] == 'km to mile':
                output = round(float(input_value) * 0.6214, 2)
                output_string = f'{input_value} km is equal to {output} mile.'
                
            elif values['-UNITS-'] == 'kg to pound':
                output = round(float(input_value) * 2.20, 2)
                output_string = f'{input_value} kg is equal to {output} lbs.'
            
            elif values['-UNITS-'] == 'sec to min':
                output = round(float(input_value) / 60, 2)
                output_string = f'{input_value} sec is equal to {output} min.'
            
            window['-OUTPUT-'].update(output_string)
    
window.close()
