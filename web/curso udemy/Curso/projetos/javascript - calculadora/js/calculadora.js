function buscaNumeros(){
    var na = document.getElementById("VA").value;
    var nb = document.getElementById("VB").value;
    var valores =  Array(na, nb);
    
    return valores;
}
function somar(e){
    var valores = buscaNumeros();
    var resultado = parseInt(valores[0])+ parseInt(valores[1]);
    window.document.getElementById('telaResultado').innerHTML = resultado;
    e.preventDefault();
}   