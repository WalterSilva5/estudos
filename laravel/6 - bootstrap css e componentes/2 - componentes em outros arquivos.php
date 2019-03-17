um componente do site (como por exemplo uma div
 ou um paragrafo)
pode ser colocado em outro arquivo.blade.php 
e ser chamado na pagina principal da view

para chamarmos um componente em uma pagina usamos
o metodo @componente

podemos criar uma pasta para componentes
colocar o meuComponente.blade.php dentro dessa pasta 
e importalo no arquivo da view
com o comando
 
@component('components.meuComponente')
@endcomponent


se colocarmos codigo html detntro das duas linhas do comando @component e @endcomponent
o codigo vai ser mostrado na pagina 
por ex: se eu colocar um paragrafo entre essas linhas
esse paragrafo vai ser exibido formatado para o navegador
e adequado ao componente

POREM para fazer isso devemos reservar um parametro entre as linhas do @component
esse parametro/comando é o 

@slot('nomeDoSlot')
    conteudo do slot
@endslot


e dentro do arquivo que guarda o codigo do componente 
devemos passar o comando {{$slot}}

significa que temos um slot reservado para o elemento


ex de codigo:

arquivo componente:
<div class ="alert alert-primary" role="alert">
    <div class="alert-title">{{$titulo}}</div>//essa variavel titulo vem do arquivo principal e esta no slot
    {{$slot}}
</div>

arquivo da pagina/view que chama o componente:

<body>
@component('componentes.meuComponente')
    <strong>Erro:</strong> Mensagem de erro.
    @slot('titulo')
        erro fatal
    @endslot
@endcomponent
</body>

//sera criada uma variavel titulo que guarda o texto dentro do slot

/////////////


ainda no arquivo do componente podemos receber como parametro
o tipo do alert para a classe do bootstrap 

po ex:
no codigo do componente:
<div class ="alert alert-{{$tipo}}" role="alert">
    <div class="alert-title">{{$titulo}}</div>
        {{$slot}}
</div>

e no codigo do view:
<body>
@component('componentes.meuComponente')
    <strong>Erro:</strong> Mensagem de erro.
    @slot('titulo')
        erro fatal
    @endslot
    @slot('tipo')
        primary
    @endslot
@endcomponent
</body>