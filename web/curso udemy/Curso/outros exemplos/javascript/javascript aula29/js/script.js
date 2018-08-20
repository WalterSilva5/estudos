window.onload = function(){
    carregarPoltronas();
};

var poltronas=[false, true, true, false];
function carregarPoltronas(){
    var imagens= document.getElementsByTagName("img");
    for(var i=0; i<poltronas.length; i++){
        if(poltronas[i]){
        imagens[i].src="cadeiravazia.png";
            }
        else{
            imagens[i].src="cadeiraocupada.png";
        };
    };
}

function selecionarPoltrona(){
    var imagens = document.getElementsByTagName("img");
    for(var i=0; i<poltronas.length; i++){
        if(poltronas[i]){
            imagens[i].src="cadeiraocupada.png";
            quer = confirm("voce quer essa cadeira ?");
            if (quer){
                break;
            } else{
                imagens[i].src="cadeiravazia.png"; 
            }
        }
    }
}