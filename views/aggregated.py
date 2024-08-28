from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from crm.models.aggregated import CRMMontlySnapshot
import plotly.graph_objs as go
from plotly.offline import plot

class GenerateReportView(LoginRequiredMixin, View):
    """
    Vista per generare report basati sui dati CRM mensili.
    Gestisce la visualizzazione dei dati e la generazione di grafici.
    """
    template_name = 'crm/reports/crm_report.html'

    def get_queryset(self, start_date, end_date):
        """
        Recupera il queryset dei dati basato sull'intervallo di date.

        :param start_date: Data di inizio dell'intervallo
        :param end_date: Data di fine dell'intervallo
        :return: QuerySet dei dati filtrati
        """
        return CRMMontlySnapshot.objects.filter(date__range=[start_date, end_date]).order_by('-date')

    def generate_graph(self, data, x_data_key='date', y_data_keys=None, graph_type='lines+markers', title=None, xaxis_title='Date', yaxis_title='Value'):
        """
        Genera un grafico utilizzando Plotly basato sui dati forniti.

        :param data: Lista di oggetti contenenti i dati da visualizzare
        :param x_data_key: Chiave per i dati sull'asse X
        :param y_data_keys: Lista di chiavi per i dati sull'asse Y
        :param graph_type: Tipo di grafico (es. 'lines+markers', 'bars', etc.)
        :param title: Titolo del grafico
        :param xaxis_title: Titolo dell'asse X
        :param yaxis_title: Titolo dell'asse Y
        :return: Div HTML del grafico
        """
        traces = []
        for y_data_key in y_data_keys:
            y_data = [getattr(item, y_data_key) for item in data]
            trace = go.Scatter(
                x=[getattr(item, x_data_key) for item in data],
                y=y_data,
                mode=graph_type,
                name=y_data_key.replace('_', ' ').capitalize()
            )
            traces.append(trace)

        layout = go.Layout(
            title=title or 'CRM Data Report',
            xaxis=dict(title=xaxis_title),
            yaxis=dict(title=yaxis_title),
            template='plotly_dark'
        )

        fig = go.Figure(data=traces, layout=layout)
        graph_div = plot(fig, output_type='div')
        return graph_div

    def get(self, request, *args, **kwargs):
        """
        Gestisce la richiesta GET per generare e visualizzare il report.

        :param request: Oggetto HttpRequest
        :return: Risposta HttpResponse con il contesto del report e il grafico
        """
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        report_data = self.get_queryset(start_date, end_date)
        graph = self.generate_graph(
            report_data,
            x_data_key='date',
            y_data_keys=['total_suppliers', 'total_customers', 'total_leads', 'total_active_customers', 'total_inactive_customers', 'total_loyal_customers'],
            graph_type='lines+markers',  # Cambia questo valore se necessario
            title='CRM Monthly Report',
            xaxis_title='Date',
            yaxis_title='Counts'
        )

        context = {
            'start_date': start_date,
            'end_date': end_date,
            'report_data': report_data,
            'graph': graph
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Gestisce la richiesta POST, se necessario.

        :param request: Oggetto HttpRequest
        :return: Risposta HttpResponse
        """
        # Implementa la logica per le richieste POST se necessario
        pass
