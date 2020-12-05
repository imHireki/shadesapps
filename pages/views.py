from django.shortcuts import render
import re
from pages.forms import InputForms


def home(request):
    return render(request, 'pages/home.html')


def letras_diferentes(request):
    # Form 
    form = InputForms(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.d = form.cleaned_data['origin']

    # Buttons
    if(request.POST.get('submit')):
        if (request.POST.get('submit')) == 'btn-a':
            form.d_new = ''
            for c in form.d:
                if c in fraktur:
                    c = fraktur[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-b':
            form.d_new = ''
            for c in form.d:
                if c in fraktur_b:
                    c = fraktur_b[c]
                form.d_new += c
        
        elif (request.POST.get('submit')) == 'btn-c':
            form.d_new = ''
            for c in form.d:
                if c in monospace:
                    c = monospace[c]
                form.d_new += c        
        
        return render(request, 'pages/letrasDiferentes.html', context)

    return render(request, 'pages/letrasDiferentes.html', context)

monospace = {
    'A': '\U0001D670',
    'B': '\U0001D671',
    'C': '\U0001D672',
    'D': '\U0001D673',
    'E': '\U0001D674',
    'F': '\U0001D675',
    'G': '\U0001D676',
    'H': '\U0001D677',
    'I': '\U0001D678',
    'J': '\U0001D679',
    'K': '\U0001D67A',
    'L': '\U0001D67B',
    'M': '\U0001D67C',
    'N': '\U0001D67D',
    'O': '\U0001D67E',
    'P': '\U0001D67F',
    'Q': '\U0001D680',
    'R': '\U0001D681',
    'S': '\U0001D682',
    'T': '\U0001D683',
    'U': '\U0001D684',
    'V': '\U0001D685',
    'W': '\U0001D686',
    'X': '\U0001D687',
    'Y': '\U0001D688',
    'Z': '\U0001D689',
    'a': '\U0001D68A',
    'b': '\U0001D68B',
    'c': '\U0001D68C',
    'd': '\U0001D68D',
    'e': '\U0001D68E',
    'f': '\U0001D68F',
    'g': '\U0001D690',
    'h': '\U0001D691',
    'i': '\U0001D692',
    'j': '\U0001D693',
    'k': '\U0001D694',
    'l': '\U0001D695',
    'm': '\U0001D696',
    'n': '\U0001D697',
    'o': '\U0001D698',
    'p': '\U0001D699',
    'q': '\U0001D69A',
    'r': '\U0001D69B',
    's': '\U0001D69C',
    't': '\U0001D69D',
    'u': '\U0001D69E',
    'v': '\U0001D69F',
    'w': '\U0001D6A0',
    'x': '\U0001D6A1',
    'y': '\U0001D6A2',
    'z': '\U0001D6A3',    
}

fraktur = {
    'A': '\U0001D504',
    'B': '\U0001D505',
    'C': '\U0000212D',
    'D': '\U0001D507',
    'E': '\U0001D508',
    'F': '\U0001D509',
    'G': '\U0001D50A',
    'H': '\U0000210C',
    'I': '\U00002111',
    'J': '\U0001D50D',
    'K': '\U0001D50E',
    'L': '\U0001D50F',
    'M': '\U0001D510',
    'N': '\U0001D511',
    'O': '\U0001D512',
    'P': '\U0001D513',
    'Q': '\U0001D514',
    'R': '\U0000211C',
    'S': '\U0001D516',
    'T': '\U0001D517',
    'U': '\U0001D518',
    'V': '\U0001D519',
    'W': '\U0001D51A',
    'X': '\U0001D51B',
    'Y': '\U0001D51C',
    'Z': '\U00002128',
    'a': '\U0001D51E',
    'b': '\U0001D51F',
    'c': '\U0001D520',
    'd': '\U0001D521',
    'e': '\U0001D522',
    'f': '\U0001D523',
    'g': '\U0001D524',
    'h': '\U0001D525',
    'i': '\U0001D526',
    'j': '\U0001D527',
    'k': '\U0001D528',
    'l': '\U0001D529',
    'm': '\U0001D52A',
    'n': '\U0001D52B',
    'o': '\U0001D52C',
    'p': '\U0001D52D',
    'q': '\U0001D52E',
    'r': '\U0001D52F',
    's': '\U0001D530',
    't': '\U0001D531',
    'u': '\U0001D532',
    'v': '\U0001D533',
    'w': '\U0001D534',
    'x': '\U0001D535',
    'y': '\U0001D536',
    'z': '\U0001D537',
}

fraktur_b = {
    'A': '\U0001D56C',
    'B': '\U0001D56D',
    'C': '\U0001D56E',
    'D': '\U0001D56F',
    'E': '\U0001D570',
    'F': '\U0001D571',
    'G': '\U0001D572',
    'H': '\U0001D573',
    'I': '\U0001D574',
    'J': '\U0001D575',
    'K': '\U0001D576',
    'L': '\U0001D577',
    'M': '\U0001D578',
    'N': '\U0001D579',
    'O': '\U0001D57A',
    'P': '\U0001D57B',
    'Q': '\U0001D57C',
    'R': '\U0001D57D',
    'S': '\U0001D57E',
    'T': '\U0001D57F',
    'U': '\U0001D580',
    'V': '\U0001D581',
    'W': '\U0001D582',
    'X': '\U0001D583',
    'Y': '\U0001D584',
    'Z': '\U0001D585',
    'a': '\U0001D586',
    'b': '\U0001D587',
    'c': '\U0001D588',
    'd': '\U0001D589',
    'e': '\U0001D58A',
    'f': '\U0001D58B',
    'g': '\U0001D58C',
    'h': '\U0001D58D',
    'i': '\U0001D58E',
    'j': '\U0001D58F',
    'k': '\U0001D590',
    'l': '\U0001D591',
    'm': '\U0001D592',
    'n': '\U0001D593',
    'o': '\U0001D594',
    'p': '\U0001D595',
    'q': '\U0001D596',
    'r': '\U0001D597',
    's': '\U0001D598',
    't': '\U0001D599',
    'u': '\U0001D59A',
    'v': '\U0001D59B',
    'w': '\U0001D59C',
    'x': '\U0001D59D',
    'y': '\U0001D59E',
    'z': '\U0001D59F',    
}