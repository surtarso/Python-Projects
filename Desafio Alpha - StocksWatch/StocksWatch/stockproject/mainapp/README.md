Em ["templates/mainapp"](templates/mainapp) os templates foram separados por função dentro da aplicação para melhor modularidade.
Assim como também o "views.py" foi repartido e separado em [views](views) de acordo com sua área de atuação.

[Consumers](consumers.py) e [routing](routing.py) foram tirados diretamente da documentação do Celery com pouca modificação necessária.

Os formuários foram feitos em ModelForm fazendo assim o uso de classes e suas propriedades para manipulação da DB.

<h5>Admin Panel:</h5>
<img src="../../shots/admin_home.png" width=545 height=410>

<h5>Hierarquia: User ManyToMany Alertas OneToMany Ativos ManyToOne Mercado</h5>
<img src="../../shots/admin_alerta.png" width=545 height=410>