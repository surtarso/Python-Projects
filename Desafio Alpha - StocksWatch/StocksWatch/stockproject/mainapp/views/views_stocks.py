from django.shortcuts import render
#multithreading
import queue
from threading import Thread
#error handling
from django.http import HttpResponse
#stocks info
from yahoo_fin.stock_info import *  #data for tables
import yfinance as yf   #data for graphs
#graphs
import plotly.graph_objs as go
#log in/ou register
from django.contrib.auth.decorators import login_required
#models
from mainapp.models import Mercado, CarteiraAtivo





## ------------------------------------------------------STOCK PICKER:
@login_required(login_url='login')
def stockPicker(request):

    mercado = Mercado.objects.get(name="IBOV")
    stock_picker = mercado.ativo_set.all()
    
    contexto = {'stockpicker':stock_picker}
    return render(request, 'mainapp/stocks/stockpicker.html', contexto)



##------------------------------------------------------STOCK TRACKER:
#recebe o submit ou do stockpicker ou do searchbar
@login_required(login_url='login')
def stockTracker(request):

    #pega o resquest (ativo(s)) de name='stockpicker' (searchbar e menu)
    stockpicker = request.GET.getlist('stockpicker')
    #cria um dicionario para os papeis escolhidos
    data = {}
    #checa com os papeis existentes do ibovespa (yahoo-fin)
    available_stocks = tickers_ibovespa()

    #errorcheck
    for i in stockpicker:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Ocorreu um erro: Ativo não identificado neste mercado")
    
    #teste multithreading
    n_threads = len(stockpicker)
    thread_list = []
    que = queue.Queue()

    #adiciona os papeis escolhidos para a tabela (single thread)
    # for i in stockpicker:
    #     #scrape yahoo data
    #     result = get_quote_table(i+'.SA')  ##.SA needed for B3!!
    #     data.update({i: result})

    #adiciona os papeis escolhidos para a tabela (multi thread)
    for i in range(n_threads):
        thread = Thread(
            target = lambda q,
            arg1: q.put({stockpicker[i]: get_quote_table(arg1+'.SA')}),
            args = (que, stockpicker[i])
            )
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()
    #update value
    while not que.empty():
        result = que.get()
        data.update(result)

    contexto = {'data':data, 'room_name':'track'}
    return render(request, 'mainapp/stocks/stocktracker.html', contexto)



##------------------------------------------------------GRAFICOS:
def configGraph(request):

    if request.method == 'GET' and request is not None:
        ticker = request.GET.get('graph')
        data = yf.Ticker(ticker+".SA").history("max")

        fig = go.Figure()

        fig.add_trace(go.Candlestick(
            x = data.index,
            open = data['Open'],
            high = data['High'],
            low = data['Low'],
            close = data['Close'],
            name = 'market data'
            ))

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label='1d', step='day', stepmode='backward'),
                    dict(count=7, label='1wk', step='day', stepmode='backward'),
                    dict(count=14, label='2wk', step='day', stepmode='backward'),
                    dict(count=1, label='1mo', step='month', stepmode='backward'),
                    dict(count=1, label='1y', step='year', stepmode='backward'),
                    dict(step='all')
                    ])
            )
        )

        graph = fig.to_html(full_html=True, default_height=600, default_width=800)
        
        contexto = {'graph': graph, 'ticker':ticker}
        return render(request, 'mainapp/stocks/graph.html', contexto)
    else:
        return HttpResponse('Ocorreu um erro.')



##----------------------------------------------- CARTEIRA ATIVOS:
@login_required(login_url='login')
def showCarteira(request):
    data = {}

    carteira = CarteiraAtivo.objects.all()
    
    for i in carteira:
        if i.user == request.user:  #pega apensas ativos do usuario atual!
            result = get_quote_table(str(i)+'.SA')
            data.update({i: result})

    contexto = {'data':data}
    return render(request, 'mainapp/stocks/carteira.html', contexto)