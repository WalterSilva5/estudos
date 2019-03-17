podemos ultilizar o if e else dentro de views
usando a sintaxe blade

para usar if ultilizamos o @if
else: @else

else if: @elseif

no final do ciclo de comparações devemos ter um 

@ endif

podemos ultilizar os comparadores por exemplo
para verificar se um array que esta na tabela de simbolos da view
esta vazio

usando o codigo

@if(isset($arrayDeAlgo))
    <p>esse paragrafo e exibido se o array tiver conteudo</p>
@else
    <p>esse paragrafo e exibido se o array não tiver conteudo</p>
@endif


ou então uma variavel n guarda um numero

@if($n===1)
    <h1>n = 1</h1>
@elseif($n===2)
    <h1>n = 2</h2>
@else
    <h1>n != 1 e n != 2</h1>    
@endif

podemos tambem exibir codigo php por ex
@if($n===1)
    <h1><?php echo "o elemento é 1"?></h1>
@elseif($n===2)
    <h1><?php echo "o elemento é 2"?></h1>
@else
    <h1><?php echo "o elemento é diferente de 1 e 2"?></h1>
@endif