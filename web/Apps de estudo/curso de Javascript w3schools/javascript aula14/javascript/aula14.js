function calcular(){
    var formulario = document.getElementById("formulario")
    var kilos = formulario.kilos.value;
    var metros = formulario.metros.value;
    var centimetros = formulario.centimetros.value;

    centimetros = parseInt(centimetros);
    var altura = (metros*100 + centimetros)/100;

    var imc = kilos/(altura*altura);
    formulario.imc.value = imc.toFixed(2);
}