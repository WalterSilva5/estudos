<?php
$valor_plano = isset($_POST['plano']) ? $_POST['plano'] : "3mb";
?>





<!DOCTYPE html>
<html lang="pt-br">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Comtible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Normalize CSS -->
    <link rel="stylesheet" href="css/normalize.css">
    <!-- Bootstrap CSS -->
    <link rel="shortcut icon" href="imagens/icone.ico" type="image/x-icon" />
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Acme" rel="stylesheet">    <link rel="stylesheet" href="css/estilo.css">
    <link href="https://fonts.googleapis.com/css?family=Rammetto+One" rel="stylesheet">
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script type="text/javascript" src="js/jquery-3.3.1.min.js"></script>
    <script src="http://code.jquery.com/jquery-2.0.0.js"></script>
    <script src="http://malsup.github.io/jquery.cycle.all.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js"></script>

    <!-- live chat help -->
    <script type="text/javascript">
        var LHCChatboxOptions = {hashchatbox:'empty',identifier:'default',status_text:'Suporte Online'};
        (function() {
            var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
            po.src = '//ntel.000webhostapp.com/chat/index.php/por/chatbox/getstatus/(position)/bottom_right/(top)/230/(units)/pixels/(width)/230/(height)/200/(chat_height)/230/(sc)/true';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
        })();
    </script>
    <!-- fim live chat help -->


    <script>
        $(document).ready(function(){
            $('.slider').bxSlider({
                auto: true,
                stopAutoOnClick: true,
                pager: true,
            })});
    </script>


    <script type="text/javascript">

        $(document).ready(function(){

            $('.btn_mostrar_conteudo').click(function(){

                var carrega_url = this.id;
                carrega_url = carrega_url + ".php";


                $.ajax({

                    url: carrega_url,

                    success: function(data){
                        $('#div_conteudo').html(data);
                    },

                    beforeSend: function(){
                        $('#loader').css({display:"block"});
                    },

                    complete: function(){
                        $('#loader').css({display:"none"});
                    }

                });

            });

        });

    </script>

    <title>NTEL - Telecom</title>
</head>

<body>
<!-- barra de navegação-->
<nav class="navbar navbar-expand-md bg-dark mb-2 fixado">
    <div class="container">
        <a class="navbar-brand" href="#"><img src="imagens/ntel-logo.png" alt="ntel"></a>
        <button class="navbar-toggler bg-warning" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="btn btn-warning" style="font-weight: bold;">Paginas    </span>
        </button>
    </div>
    <div class="container">
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="nav navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="index.php">Inicio<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item h6">
                    <a class="nav-link btn_mostrar_conteudo" id="empresa" href="#">Empresa<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link h6" href="planos.php">Planos<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link h6 btn_mostrar_conteudo" id="cobertura" href="#">Cobertura<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link h6 btn_mostrar_conteudo" id="inscricao" href="#">Cadastre-se<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link h6 btn_mostrar_conteudo" id="tecnologia" href="#">Tecnologia<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link h6 btn_mostrar_conteudo" id="contatos" href="#">Contatos<span class="sr-only">(current)</span></a>
                </li>
            </ul>
        </div>
    </div>
</nav>
<!--fim barra de navegação-->

<!-- slider-->
<a href="cadastro.php">
    <div class="slider">
        <div><img src="imagens/slider/1.png" alt=""></div>
        <div><img src="imagens/slider/2.png" alt=""></div>
        <div><img src="imagens/slider/3.png" alt=""></div>
    </div>
</a>
<!-- fim slider-->
<!-- conteudos do site-->
<div id="div_conteudo">
    <div class="container" style="margin-bottom:30px">
        <div class="page-header">
            <h1>Cadastre-se</h1>
        </div>
        <div class="row">
            <form class = "container recebe-dados"action="http://nteltelecom.com.br/executar.php?acao=assinar" method="post" id="form" onSubmit="return verifica_form(this);">

                <!--div 1 container de organização -->
                <div class="container col-md-12">
                    <!-- data de vencimento da mensalidade-->
                    <div class="block float-left col-md-6">
                        <label for="venc">Dia do vencimento mensal</label>
                        <select name="venc" class="form-control h5" id="venc">
                            <option value="01"> Todo dia 01 </option>
                            <option value="02"> Todo dia 02 </option>
                            <option value="03"> Todo dia 03 </option>
                            <option value="04"> Todo dia 04 </option>
                            <option value="05"> Todo dia 05 </option>
                            <option value="06"> Todo dia 06 </option>
                            <option value="07"> Todo dia 07 </option>
                            <option value="08"> Todo dia 08 </option>
                            <option value="09"> Todo dia 09 </option>
                            <option value="10"> Todo dia 10 </option>
                            <option value="11"> Todo dia 11 </option>
                            <option value="12"> Todo dia 12 </option>
                            <option value="13"> Todo dia 13 </option>
                            <option value="14"> Todo dia 14 </option>
                            <option value="15"> Todo dia 15 </option>
                            <option value="16"> Todo dia 16 </option>
                            <option value="17"> Todo dia 17 </option>
                            <option value="18"> Todo dia 18 </option>
                            <option value="19"> Todo dia 19 </option>
                            <option value="20"> Todo dia 20 </option>
                            <option value="21"> Todo dia 21 </option>
                            <option value="22"> Todo dia 22 </option>
                            <option value="23"> Todo dia 23 </option>
                            <option value="24"> Todo dia 24 </option>
                            <option value="25"> Todo dia 25 </option>
                            <option value="26"> Todo dia 26 </option>
                            <option value="27"> Todo dia 27 </option>
                            <option value="28"> Todo dia 28 </option>
                            <option value="29"> Todo dia 29 </option>
                            <option value="30"> Todo dia 30 </option>
                        </select>
                    </div>
                    <!-- fim data de vencimento da mensalidade-->

                    <!-- Velocidade do Plano -->
                    <div class="block float-left col-md-6">
                        <label for="plano">Velocidade do Plano</label>
                        <select name="plano" class="form-control h5" id="plano">
                            <!--<option value="1_MEGA"> 1_MEGA</option>
                            <option value="2_MEGAS"> 2_MEGAS</option>-->

                            <option value=<?php echo $valor_plano[0]."_MEGAS" ?> selected="yes"><p><?php
                                    if($valor_plano[0]==1){
                                        $pagar = "10";
                                        echo "10 MEGAS R$: 120,00";
                                    }else{
                                        $pagar = $valor_plano[0]+1;
                                        $mostrar = $valor_plano[0]." MEGAS R$ ".$pagar."0,00";
                                        echo $mostrar;
                                    }

                                    ?></p></option>
                            <option value="3_MEGAS"> 3 MEGAS R$: 40,00</option>
                            <option value="4_MEGAS"> 4 MEGAS R$: 50,00</option>
                            <option value="5_MEGAS"> 5 MEGAS R$: 60,00</option>
                            <option value="6_MEGAS"> 6 MEGAS R$: 70,00</option>
                            <option value="10_MEGAS"> 10 MEGAS R$: 120,00</option>
                        </select>
                    </div>
                    <!-- fim Velocidade do Plano -->
                </div>
                <!-- fim da div 1 container de organização -->

                <!-- div 2 container de organização -->
                <div class="container">
                    <!-- login de usuario -->
                    <div class="container float-left col-md-6">
                        <label for="q">Login</label>
                        <input name="q" id="q" value="" class="form-control h5" onKeyUp="buscalogin(this.value)" maxlength="100" df_verificar="sim">
                        <!-- fim login de usuario -->

                        <!-- mensagem caso de erro no login-->
                        <div id="msglogin" class="h4 text-danger"></div>
                    </div>
                    <!-- fim mensagem caso de erro no login -->
                    <!-- senha -->
                    <div class="container float-left col-md-6">
                        <label for="senha">Senha</label>
                        <input name="senha" id="senha" class="form-control" value="" maxlength="32" type="password" df_verificar="sim">
                    </div>
                    <!-- fim senha-->
                </div>
                <!-- fim div 2 container de organização -->

                <!-- div 3 container de organização -->
                <div class="container float-left">
                    <!-- nome completo-->
                    <div class="container">
                        <label for="nome">Nome Completo</label>
                        <input name="nome" id="nome" class="form-control" value="" maxlength="100" type="text" df_verificar="sim">
                    </div>
                    <!-- fim nome completo-->

                    <!-- e mail -->
                    <div class="container">
                        <label for="email">E-Mail</label>
                        <input name="email" id="email" value="" class="form-control" maxlength="100" type="email" df_verificar="sim" df_validar="email">
                    </div>
                    <!-- fim email   -->

                    <!-- cnpj cpf -->
                    <div class="container">
                        <label for="cpf_cnpj">CPF/CNPJ</label>
                        <input name="cpf_cnpj" id="cpf_cnpj" class="form-control" value="" maxlength="100" type="text" df_verificar="sim" df_validar="cpf_cnpj" onKeyUp='this.value=this.value.replace(/[^\d]*/gi,"");'>
                    </div>
                    <!-- fim cnpj cpf -->
                </div>
                <!-- fim div 3 container de organização -->

                <!-- div 4 container de organização -->
                <div class="container">
                    <!-- rg -->
                    <div class="container float-left col-md-4">
                        <label for="rg">RG</label>
                        <input name="rg" id="rg" class="form-control" maxlength="100" value="" type="number" df_verificar="sim" onKeyUp='this.value=this.value.replace(/[^\d]*/gi,"");'>
                    </div>
                    <!-- fim rg -->
                    <!-- data de nascimento-->
                    <div class="container float-left col-md-4">
                        <label for="nascimento">Data de Nascimento</label>
                        <input name="nascimento" id="cli_data_nasc" value="" class="form-control" type="date" df_verificar="sim" onKeyPress="return MaskData(this, event)">
                    </div>
                    <!-- fim data de nascimento-->
                    <!--cep-->
                    <div class="container float-left col-md-4">
                        <label for="cep">CEP</label>
                        <input name="cep" type="text" class="form-control" value="" id="cep" onKeyUp="buscacep(this.value)" maxlength="9" onKeyPress="return MaskCEP(this, event)" />
                    </div>
                    <!--fim cep-->

                    <!-- div 4 container organização -->
                    <div class="container">
                        <!--endereço-->
                        <div class="container float-left col-md-10">
                            <label for="endereco">Endereço</label>
                            <input name="endereco" id="endereco" value="" class="form-control"  type="text" df_verificar="sim">
                        </div>
                        <!--fim endereço-->
                        <!--numero-->
                        <div class="container float-left col-md-2">
                            <label for="numero">Numero</label>
                            <input name="numero" class="form-control" type="text" value="" id="numero" maxlength="10" df_verificar="sim">
                        </div>
                        <!--fim numero-->
                    </div>
                    <!-- fim div 4 container organização -->

                    <!-- div 5 container organização -->
                    <div class="container">
                        <!-- complemento -->
                        <div class="container float-left col-md-6">
                            <label for="complemento">Complemento(Ex.: Andar,  Bloco, etc...)</label>
                            <input name="complemento" id="complemento" value="" class="form-control" type="text">
                        </div>
                        <!-- fim complemento -->
                        <!-- bairro -->
                        <div class="container float-left col-md-6">
                            <label for="bairro">Bairro</label>
                            <input name="bairro" id="bairro" class="form-control" value="" maxlength="100" type="text" df_verificar="sim">
                        </div>
                        <!-- fim bairro -->

                        <!-- Cidade -->
                        <div class="container float-left col-md-6">
                            <label for="cidade">Cidade</label>
                            <input name="cidade" id="cidade" class="form-control" value=""  type="text" df_verificar="sim">
                        </div>
                        <!-- fim cidade -->

                        <!-- estado -->
                        <div class="container float-left col-md-6">
                            <label for="Estado">Estado</label>
                            <select name="estado" class="form-control" id="estado">
                                <option value="AC">Acre</option>
                                <option value="AL">Alagoas</option>
                                <option value="AP">Amap&aacute;</option>
                                <option value="AM">Amazonas</option>
                                <option value="BA">Bahia</option>
                                <option value="CE">Cear&aacute;</option>
                                <option value="DF">Distrito Federal</option>
                                <option value="ES">Esp&iacute;rito Santo</option>
                                <option value="GO">Goias</option>
                                <option value="MA">Maranh&atilde;o</option>
                                <option value="MT">Mato Grosso</option>
                                <option value="MS">Mato Grosso do Sul</option>
                                <option value="MG">Minas Gerais</option>
                                <option value="PA">Par&aacute;</option>
                                <option value="PB">Para&iacute;ba</option>
                                <option value="PR">Paran&aacute;</option>
                                <option value="PE" selected=selected>Pernambuco</option>
                                <option value="PI">Piau&iacute;</option>
                                <option value="RJ">Rio de Janeiro</option>
                                <option value="RN">Rio Grande do Norte</option>
                                <option value="RS">Rio Grande do Sul</option>
                                <option value="RO">Rond&ocirc;nia</option>
                                <option value="RR">Roraima</option>
                                <option value="SC">Santa Catarina</option>
                                <option value="SP">S&atilde;o Paulo</option>
                                <option value="SE">Sergipe</option>
                                <option value="TO">Tocantins</option>
                            </select>
                        </div>
                        <!-- fim estado -->

                        <!-- Telefone -->
                        <div class="container float-left col-md-6">
                            <label for="Telefone">Telefone</label>
                            <input name="telefone" id="telefone" class="form-control" value="" type="text" onKeyPress="return MaskTelefone(this, event)">
                        </div>
                        <!-- fim Telefone -->

                        <!-- celular -->
                        <div class="container float-left col-md-6">
                            <label for="celular">Celular</label>
                            <input name="celular" id="celular" class="form-control" value="" maxlength="20" type="text" onKeyUp="enviacodigo(this.value)" onKeyPress="return MaskCelular(this, event)" df_verificar="sim">
                        </div>
                        <!-- fim celular -->

                        <!-- inputs q n sei pra q serve -->
                        <input name="codigo" type="hidden" id="codigo" value="41EFE412">
                        <input name="token" type="hidden" id="token" value="d39445d40355b625646444e4">
                        <input name="captchax" type="hidden" id="captchax" value="E2J5VA">
                        <input type="hidden" name="token_hotsite" value="26a677e23b95714a953bb5ad17f56a69">
                        <!-- fim inputs q n sei pra q serve -->

                        <!-- codigo promocional -->
                        <div class="container float-left col-md-6">
                            <label for="promocod">Codigo Promicional (caso tenha)</label>
                            <input name="promocod" id="promocod" class="form-control" value="" type="text">
                        </div>
                        <!-- fim codigo promocional -->
                    </div>
                    <!-- fim div 5 container organização -->

                    <!-- aceita cadastrar-->
                    <div class="container text-center float-left h5">
                        <input type="checkbox" name="aceitou" id="aceitou" value="sim">
                        Declaro que li e aceito o <strong><a href="contrato.html" target="_blank" onClick="window.open(this.href, this.target, 'width=740,height=420,scrollbars=yes'); return false;">contrato</a></strong> do provedor.
                    </div>
                    <!-- fim aceita cadastrar-->

                    <!-- cadastrar ou limpar-->
                    <div class="container float-left text-center">
                        <input name="enviar" class="botao btn btn-warning" id="enviar" value="Cadastrar" alt="Enviar" type="submit">
                        <input name="limpar" class="botao btn btn-warning" alt="Limpar" id="limpar" value="Limpar" type="reset">
                    </div>
                    <!-- fim cadastrar ou limpar-->
                </div>
            </form>
        </div>
    </div>
</div>
<!-- fim conteudos do site-->


<!-- central do assinante-->
<div class="container col-md-12">
    <a href="http://nteltelecom.com.br/central/login.php">
        <img class="img-responsive banner_central" src="imagens/central.png"></a>
</div>

<!-- footer -->
<footer id="rodape">
    <div class="container">
        <div class="row">

            <div class="col-md-3">
                <img class="img-fluid" src="imagens/ntel-logo.png" alt="NTEL Telecom">
            </div>

            <div class="col-md-3">
                <h4>Navegação</h4>
                <ul class="nav">
                    <li><a class="nav-link btn_mostrar_conteudo" id="empresa" href="#">Empresa<span class="sr-only">(current)</span></a></li>
                    <li><a class="nav-link h6" href="planos.php">Planos<span class="sr-only">(current)</span></a></li>
                    <li><a class="nav-link h6 btn_mostrar_conteudo" id="cobertura" href="#">Cobertura<span class="sr-only">(current)</span></a></li>
                    <li><a class="nav-link h6 btn_mostrar_conteudo" id="inscricao" href="#">Cadastre-se<span class="sr-only">(current)</span></a></li>
                    <li><a class="nav-link h6 btn_mostrar_conteudo" id="tecnologia" href="#">Tecnologia<span class="sr-only">(current)</span></a></li>
                    <li><a class="nav-link h6 btn_mostrar_conteudo" id="contatos" href="#">Contatos<span class="sr-only">(current)</span></a></li>
                </ul>
            </div>

            <div class="col-md-4">
                <ul class="nav">
                    <li class="item-rede-social"><a href=""><img src="imagens/facebook.png"></a></li>
                    <li class="item-rede-social"><a href=""><img src="imagens/twitter.png"></a></li>
                    <li class="item-rede-social"><a href=""><img src="imagens/instagram.png"></a></li>
                </ul>
            </div>
        </div><!-- /row -->
    </div>
</footer>
    <div class="col-xs-12 text-center h3 bg-dark">
        <a href="https://waltersilva5.github.io" class="badge badge-primary">Feito Por: <spam class="text-warning">Walter Silva</spam></a>
    </div>
<!-- fim do footer -->

<!--scripts necessarios-->
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
</body>

</html>
