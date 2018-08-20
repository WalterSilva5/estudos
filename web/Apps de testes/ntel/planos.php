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
                        <a class="nav-link h6" href="index.php">Inicio<span class="sr-only">(current)</span></a>
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
    <!-- fim barra de navegação-->

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
    <!-- galeria de preços -->
<!-- galeria de preços -->


<div class="container">
<form action="cadastro.php" method="post">
    <div class="container col-md-12 text-center galeria">
    <p class="h1" style="font-family: 'Rammetto One', cursive;" >Escolha o Melhor Plano Para Você!</p>
    <button type="submit" name="plano" value="3mb" class="btn btn-light botao col-md-3"><img  class="img-fluid anuncio" src="imagens/planos/3mb.png" alt="3mb"></button>
    <button type="submit" name="plano" value="4mb" class="btn btn-light botao col-md-3"><img  class="img-fluid anuncio" src="imagens/planos/4mb.png" alt="3mb"></button>

    <button type="submit" name="plano" value="5mb" class="btn btn-light botao col-md-3"><img  class="img-fluid anuncio" src="imagens/planos/5mb.png" alt="5mb"></button>
    <button type="submit" name="plano" value="6mb" class="btn btn-light botao col-md-3"><img  class="img-fluid anuncio" src="imagens/planos/6mb.png" alt="6mb"></button>
    <button type="submit" name="plano" value="7mb" class="btn btn-light botao col-md-3"><img  class="img-fluid anuncio" src="imagens/planos/7mb.png" alt="7mb"></button>
    <button type="submit" name="plano" value="10mb" class="btn btn-light botao col-md-3"><img  class="img-fluid anuncio" src="imagens/planos/10mb.png" alt="10mb"></button>

    </div>
</form>
</div>
  <!-- fim galeria de preços -->
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